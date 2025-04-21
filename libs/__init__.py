
import socket
import time
from colorama import Fore
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from libs.ports import ports
from libs.brand import banner
class Scanner:
    def __init__(self,ip,sp=1,ep=65535):
        self.host = ip
        banner()
        self.run_scan(sp,ep)
    def result(self,port,time):
        if port in ports:
                print(f"{Fore.GREEN}{port} {ports[port]} Scanned sec {time:.2f} Mille sec {time*1000}")
        else:
                print(f"{Fore.RED}{port} (Dynamic or private network) Scanned sec {time:.2f} Mille sec {time*1000}")
                
    def scan_port(self, port):
        start_time = time.time()
        duration=0
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((self.host, port))
                duration = time.time() - start_time
                return port, True , duration
        except:
            return port, False , duration

    def run_scan(self, startRange ,port_range):
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(self.scan_port, port) for port in range(startRange,port_range)]
            for future in as_completed(futures):
                port, is_open ,duration = future.result()
                if is_open:
                    self.result(str(port),duration)         
    

    
        
        

