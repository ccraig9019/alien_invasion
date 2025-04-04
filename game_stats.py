class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Start Alien Invasion in an inactive state
        self.game_active = False

        #High score should never be reset
        with open('high_score.txt') as f:
            lines = f.readline() 
        self.high_score = int(lines)

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
