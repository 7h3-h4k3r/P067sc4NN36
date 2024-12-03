import threading
import socket
import sys
import subprocess
from colorama import Fore

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
class Scanner(threading.Thread):
    def __init__(self,ip,sp=1,ep=65535):
        threading.Thread.__init__(self)
        self.ip = ip
        self.banner()
        self.UserInteraction(sp,ep)
    def UserInteraction(self,sp,ep):
        for i in range(sp,ep):
            Threadingx(self.ip,i).start()
        
    def result(self,port):
        data = list(ports)
        for i  in range(len(ports)-1):
            if int(data[i]) == port:
                print(Fore.GREEN,port,ports.get(data[i]))
                break
            elif(i==39):
                print(Fore.RED,port,"(Dynamic or private network)")
                
    def banner(self):  
        art = f"""
{Fore.RED}   ____                      , 
  /---.'.__             {Fore.WHITE}____//{Fore.RED}
       '--.\\           {Fore.WHITE}/.---'{Fore.RED}
  _______  \\         {Fore.WHITE}//{Fore.RED}
/.------.\\  \\|      .'/  {Fore.WHITE}______{Fore.RED}
//  ___  \\ \\  ||/|\\  //  {Fore.WHITE}_/_----.{Fore.RED}\\__
|/  /.-.\\  \\ \\:|< >|// _/{Fore.BLACK}.'..\\   '--'{Fore.RED} \t\t\t D3v 3y SriDharaniTharan
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

    

class Threadingx(Scanner):
    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.port = port
        self.ip = ip
        self.socket_= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def run(self):
        if(self.socket_.connect_ex((self.ip,self.port))==0):
            self.result(self.port)
            

class InputSanitize:
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
                
