import os
from colorama import Fore
def banner(): 
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