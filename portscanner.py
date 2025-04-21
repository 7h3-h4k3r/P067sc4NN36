from libs.main import  LiveIt
from colorama import Fore
result = LiveIt()
if(result.argvcheck()):
        print(f"\t\t\t {Fore.BLUE}SUCCESSFULLY SCANNED THE NETWORK   (IF IT'S EMPTY,NO PORT'S ARE OPENED)")
else:
        pass
