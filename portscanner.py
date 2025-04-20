from libs.__init__ import  InputSanitize
from colorama import Fore
result = InputSanitize()
if(result.argvcheck()):
        print(f"\t\t\t {Fore.BLUE}SUCCESSFULLY SCANNED THE DEVICE   (IF IT'S EMPTY,NO PORT'S ARE OPENED)")
else:
        pass
