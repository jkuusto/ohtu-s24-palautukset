import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    nationality = "FIN"

    players_nationality = filter(lambda player: player.nationality ==
                                 nationality, players)
    players_points = sorted(players_nationality, key=lambda player:
                            player.points, reverse=True)

    print(f"Players from {nationality}:\n")

    for player in players_points:
        print(player)

if __name__ == "__main__":
    main()
