from libs.main import  LiveIt
from colorama import Fore
result = LiveIt()
status , msg  = result.argvcheck()
if(status):
        print(f"\t\t\t {Fore.BLUE}SUCCESSFULLY SCANNED THE NETWORK   (IF IT'S EMPTY,NO PORT'S ARE OPENED)")
else:
        print(f"{Fore.BLUE}-ERROR={msg}")
