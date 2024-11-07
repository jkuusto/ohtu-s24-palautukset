class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()

        unique_players = {}
        for player in players:
            if player.nationality == nationality:
                unique_players[player.id] = player

        players_nationality = list(unique_players.values())
        
        players_points = sorted(players_nationality, key=lambda player:
                                player.points, reverse=True)
        
        return players_points

    def nationalities(self):
        players = self._reader.get_players()

        nationalities = sorted({player.nationality for player in players})

        nationalities = f"[{'/'.join(nationalities)}]"

        return nationalities
