from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.table import Table

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.nationalities()

    print(f"[italic bright_black]NHL statistics by nationality"
          f"[/italic bright_black]\n")

    print(f"[bright_black]Select nationality [/bright_black]"
          f"[bright_magenta]{nationalities}[/bright_magenta]"
          f"[bright_black]: [/bright_black]", end="")
    
    while True:
        nationality = input("").upper()
        if nationality in nationalities:
            players = stats.top_scorers_by_nationality(nationality)
            break
        else:
            print(f"[bright_red]Invalid nationality. Try again: [/bright_red]"
                  , end="")
        
    table = Table(title=(f"[italic bright_black]Top scorers of {nationality}"
                         f"[/italic bright_black]"))
    table.add_column("name", style="bright_cyan")
    table.add_column("team", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals),
                      str(player.assists), str(player.points))

    print(table)

if __name__ == "__main__":
    main()
