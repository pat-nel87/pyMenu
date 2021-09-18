from rich import print
from rich.console import Console
from time import sleep

console = Console()
print("[bold red]Hello[/bold red] ", "[bold green]Patrick[/bold green]", ":vampire:")

with console.status("[bold cyan]Scanning Terminal Environment...") as status:
        timer = 1
        while (timer > 0):
            sleep(1)
            timer = timer - 1

print("[bold cyan] Welcome to your Terminal,[/bold cyan] [bold green] Dude![/bold green]", ":smiley:", ":raccoon:")
