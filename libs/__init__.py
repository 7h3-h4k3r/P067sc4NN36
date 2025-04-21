
import socket
import time
import sys
import subprocess
from colorama import Fore
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

ports = {
        "20": "FTP (File Transfer Protocol)",
        "21": "FTP (File Transfer Protocol)",
        "22": "SSH (Secure Shell)",
        "23": "Telnet",
        "25": "SMTP (Simple Mail Transfer Protocol)",
        "53": "DNS (Domain Name System)",
        "67": "DHCP (Dynamic Host Configuration Protocol)",
        "68": "DHCP (Dynamic Host Configuration Protocol)",
        "69": "TFTP (Trivial File Transfer Protocol)",
        "80": "HTTP (Hypertext Transfer Protocol)",
        "110": "POP3 (Post Office Protocol version 3)",
        "119": "NNTP (Network News Transfer Protocol)",
        "123": "NTP (Network Time Protocol)",
        "143": "IMAP (Internet Message Access Protocol)",
        "161": "SNMP (Simple Network Management Protocol)",
        "162": "SNMP (Simple Network Management Protocol)",
        "179": "BGP (Border Gateway Protocol)",
        "443": "HTTPS (HTTP Secure)",
        "445": "SMB (Server Message Block)",
        "465": "SMTPS (Secure SMTP)",
        "514": "Syslog",
        "587": "SMTP (with encryption)",
        "631": "IPP (Internet Printing Protocol)",
        "993": "IMAPS (Secure IMAP)",
        "995": "POP3S (Secure POP3)",
        "1080": "SOCKS Proxy",
        "1433": "Microsoft SQL Server",
        "1521": "Oracle Database",
        "1723": "PPTP (Point-to-Point Tunneling Protocol)",
        "1883": "MQTT (Message Queuing Telemetry Transport)",
        "2049": "NFS (Network File System)",
        "2375": "Docker (unencrypted)",
        "2376": "Docker (encrypted)",
        "3306": "MySQL/MariaDB",
        "3389": "RDP (Remote Desktop Protocol)",
        "5432": "PostgreSQL",
        "5900": "VNC (Virtual Network Computing)",
        "6379": "Redis",
        "8080": "HTTP Alternative",
        "8443": "HTTPS Alternative",
        "9092": "Apache Kafka"
    }  
class Scanner:
    def __init__(self,ip,sp=1,ep=65535):
        self.host = ip
        self.max_work=100
        self.banner()
        self.run_scan(sp,ep)

    def result(self,port,time):
        data = list(ports)
        for i  in range(len(ports)-1):
            if int(data[i]) == port:
                print(f"{Fore.GREEN}{port}{ports.get(data[i])} Scanned sec {time:.2f} Mille sec {time*1000}")
                break
            elif(i==39):
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
        with ThreadPoolExecutor(max_workers=self.max_work) as executor:
            futures = [executor.submit(self.scan_port, port) for port in range(startRange,port_range)]
            for future in as_completed(futures):
                port, is_open ,duration = future.result()
                if is_open:
                    self.result(port,duration)         
    def banner(self): 
        os.system('cls' if os.name == 'nt' else 'clear')
 
        art = f"""
{Fore.RED}   ____                      , 
  /---.'.__             {Fore.WHITE}____//{Fore.RED}
       '--.\\           {Fore.WHITE}/.---'{Fore.RED}
  _______  \\         {Fore.WHITE}//{Fore.RED}
/.------.\\  \\|      .'/  {Fore.WHITE}______{Fore.RED}
//  ___  \\ \\  ||/|\\  //  {Fore.WHITE}_/_----.{Fore.RED}\\__
|/  /.-.\\  \\ \\:|< >|// _/{Fore.BLACK}.'..\\   '--'{Fore.RED} \t\t\t D3v 3y SriDharaniTharan (version 2.0)
   //   \\'. | \\'.|.'/ /_/ /  \\\\
  //     \\ \\_\\/" ' ~\\-'.-'    \\\\
 //       '-._| :S: |'-.__     \\\\
{Fore.BLACK}//           (/'==='/)'-._\\     {Fore.RED}||
{Fore.WHITE}||                        \\\\    \\|
{Fore.WHITE}||       P067 SC4NN36      \\\\    '
{Fore.WHITE}|/                          \\\\
                            ||
                            ||
                            \\\\
"""

        print(art)

    
        
        

class LiveIt:
        def LiveCheck(self,host):
                try:
                        subprocess.run(["ping","-c","1",host],stdin = subprocess.PIPE , stderr = subprocess.PIPE,check = True)
                        return True
                except:
                        return False
        def help(self,bin):
                print(f"""
        Usage {bin} -Tp -s <target ip> OR {bin} -Tp <target ip> -sP <port> -Ep <port>
                
        -h  or --help

                Show User Manual Page (version of the Scanner V:1.0)      
        -Tp 
                (Tp) Target ip Address (Ex: -Tp 192.168.0.1)      
        -s 
                Scan to start a all Available Port (Ex : - Tp -s 192.168.0.1)
        -sP 
                Starting Port short form of -sP  
        -Ep 
                Ending Port short form of -Ep
                                                                                                                                
        """)

        def argvcheck(self):
                print(len(sys.argv))
                if(len(sys.argv) == 4 and sys.argv[1]=="-Tp" and sys.argv[2] == "-s" and self.LiveCheck(sys.argv[3])):
                       Scanner(sys.argv[3])   
                       return True   
                elif(len(sys.argv)== 7 and sys.argv[1]=="-Tp" and sys.argv[3] == "-sP" and sys.argv[5]=="-Ep"):
                        if(int(sys.argv[4])> 0 and  int(sys.argv[6])>int(sys.argv[4]) and int(sys.argv[6])<=65535 and self.LiveCheck(sys.argv[2])):
                              Scanner(sys.argv[2],int(sys.argv[4]),int(sys.argv[6]))
                              return True
                        else:
                                self.help(sys.argv[0])
                                return False
                else:
                        self.help(sys.argv[0])
                        return False
                
