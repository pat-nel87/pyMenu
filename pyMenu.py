# Patrick Nelson's fedora 34 menu script
# executes on launch of bash terminal
import os
from rich import print
from rich.console import Console
from time import sleep

# A cute little menu script 
# to help speed up access
# to commonly used scripts / applications
# Script is designed to detect any bash scripts
# in my home directory and add them to a menu
# where you can choose to launch the script
# by choosing from menu list

console = Console()
# a kitchy status bar effect just for fun
with console.status("[bold cyan]Scanning Terminal Environment...") as status:
        timer = 2
        while (timer > 0):
            sleep(1)
            timer = timer - 1

x = os.listdir(r"/home/sav-dab87/")
console.print("[bold cyan]Welcome to your Terminal,[/bold cyan] [bold green] Dude![/bold green]", ":smiley:", ":raccoon:",justify="center")
console.print("[bold green]Terminal Scripts List[/bold green]",justify="center")

# a dictionary to hold a numeric key associated with each
# script file to allow user to choose script to launch by number

dictList = {}
j=1
for i in x:
    #searches home directory for .sh files
    if i.endswith(".sh"):
       console.print(str(j) + "." + i, justify="center")
       dictList.update({str(j): i})
       j+=1
# Prompts user for choice 
choice = input("Enter a number to launch script or 0 to quit to terminal---> ")
numChoice = int(choice)
if (choice == 0):
    quit()
elif (numChoice > 0):
    os.system("./" + dictList.get(choice))



#print(f"{dictList}")



