class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()

        players_nationality = filter(lambda player: player.nationality ==
                                 nationality, players)
        
        players_points = sorted(players_nationality, key=lambda player:
                                player.points, reverse=True)
        
        return players_points
