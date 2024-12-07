import json
import os
from datetime import datetime

class PlayerStats:
    def __init__(self, username):
        self.username = username
        self.games_played = 0
        self.games_won = 0
        self.total_points = 0
        self.highest_score = 0
        self.last_played = None
        self.win_streak = 0
        self.current_streak = 0
        
    def update_stats(self, points_scored, won):
        self.games_played += 1
        self.total_points += points_scored
        self.last_played = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if points_scored > self.highest_score:
            self.highest_score = points_scored
            
        if won:
            self.games_won += 1
            self.current_streak += 1
            if self.current_streak > self.win_streak:
                self.win_streak = self.current_streak
        else:
            self.current_streak = 0
            
    def get_win_rate(self):
        if self.games_played == 0:
            return 0
        return (self.games_won / self.games_played) * 100
    
    def to_dict(self):
        return {
            "username": self.username,
            "games_played": self.games_played,
            "games_won": self.games_won,
            "total_points": self.total_points,
            "highest_score": self.highest_score,
            "last_played": self.last_played,
            "win_streak": self.win_streak,
            "current_streak": self.current_streak
        }
    
    @classmethod
    def from_dict(cls, data):
        stats = cls(data["username"])
        stats.games_played = data["games_played"]
        stats.games_won = data["games_won"]
        stats.total_points = data["total_points"]
        stats.highest_score = data["highest_score"]
        stats.last_played = data["last_played"]
        stats.win_streak = data["win_streak"]
        stats.current_streak = data["current_streak"]
        return stats