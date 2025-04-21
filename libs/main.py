import subprocess
import sys
from libs.__init__ import  Scanner

class LiveIt:
        def LiveCheck(self,host):
                try:
                        subprocess.run(["ping","-c","1",host],stdin = subprocess.PIPE , stderr = subprocess.PIPE,check = True)
                        return True
                except:
                        return False
        def help(self,bin):
                print(f"""
        [Usage]: {bin} -Tp -s <target ip> (OR) {bin} -Tp <target ip> -sP <port> -Ep <port>
                
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
                
