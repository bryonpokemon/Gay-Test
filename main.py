import os
from colorama import Fore
import time
def clear():
    os.system("cls")
    print(f'\n\t\t\t\t\u001b[38;5;127m╔═╗┬ ┬┬┬┌┐┌┬┌─┬┌┐ ┌─┐┬\n\t\t\t\t\u001b[38;5;128m║  ├─┤│││││├┴┐│├┴┐│ ││\n\t\t\t\t\u001b[38;5;129m╚═╝┴ ┴┴┴┘└┘┴ ┴┴└─┘└─┘┴{Fore.RESET}\n\n\n')
    print(f"{Fore.RED}The Gay {Fore.YELLOW}Test")
    print(f"{Fore.YELLOW}Let {Fore.GREEN}your computer {Fore.CYAN}history {Fore.BLUE}talk for{Fore.MAGENTA} you!:{Fore.RESET}")
def main():
    yes = "Yes, you are gay!"
    no = "Wrong, you are pretty gay!"
    error = "Type an actual answer"
    yeslist = ["ye", "yes", "maybe", "not really", "yea", "yeah", "fuck you", "y"]
    nolist = ["no", "nah", "exit", "", "n"] 
    answer = input("are you gay? ")
    clear()
    print("Checking history, Please wait")
    time.sleep(3)
    if answer in yeslist:
        print(yes)
    elif answer in nolist: 
        print(no)
    else:
        print(error),
        print("Restarting")
        time.sleep(4)
        clear()
        main()
    restart = input("would you like to restart: ")
    if restart in yeslist:
        clear()
        main()
    else:
        print(f"{Fore.RED}Thank {Fore.YELLOW}you {Fore.GREEN}for {Fore.CYAN}taking {Fore.BLUE}the {Fore.MAGENTA}test{Fore.RESET}")
        exit()
clear()
main()