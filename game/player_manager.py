import json
import os
from .player_stats import PlayerStats

class PlayerManager:
    def __init__(self):
        self.players = {}
        self.save_file = "player_data.json"
        self.load_players()
        
    def load_players(self):
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    data = json.load(f)
                    for username, stats in data.items():
                        self.players[username] = PlayerStats.from_dict(stats)
            except:
                print("Error loading player data")
                
    def save_players(self):
        data = {username: stats.to_dict() for username, stats in self.players.items()}
        try:
            with open(self.save_file, 'w') as f:
                json.dump(data, f, indent=2)
        except:
            print("Error saving player data")
            
    def get_player(self, username):
        if username not in self.players:
            self.players[username] = PlayerStats(username)
        return self.players[username]
    
    def update_player_stats(self, username, points_scored, won):
        player = self.get_player(username)
        player.update_stats(points_scored, won)
        self.save_players()
        
    def get_leaderboard(self):
        return sorted(
            self.players.values(),
            key=lambda p: (p.games_won, p.highest_score),
            reverse=True
        )