import random
from typing import List
from .base import Player

# ==========================================
# THE GOOD GUYS
# ==========================================

class TitForTat(Player):
    """Tit for Tat: Cooperates on turn 1, then copies the opponent's last move."""
    def __init__(self):
        super().__init__("TitForTat")

    def make_move(self, opponent_history: List[str]) -> str:
        if not opponent_history:
            return 'O'  
        return opponent_history[-1] 

class TitForTwoTats(Player):
    """Tit for Two Tats: Only defects if the opponent defects twice in a row."""
    def __init__(self):
        super().__init__("TitForTwoTats")

    def make_move(self, opponent_history: List[str]) -> str:
        if len(opponent_history) < 2:
            return 'O'  # Rounds 1 and 2
        
        # If the last two moves of the opponent were defections ('X')
        if opponent_history[-1] == 'X' and opponent_history[-2] == 'X':
            return 'X'
        return 'O'

class GenerousTitForTat(Player):
    """Generous Tit for Tat: Plays Tit for Tat, but forgives 10% of defections."""
    def __init__(self):
        super().__init__("GenerousTitForTat")

    def make_move(self, opponent_history: List[str]) -> str:
        if not opponent_history:
            return 'O' 
        
        last_opponent_move = opponent_history[-1]
        
        if last_opponent_move == 'X':
            # Intentionally forgives 10% of the time
            if random.random() < 0.10:
                return 'O'
            else:
                return 'X'
        return 'O'

# ==========================================
# THE BAD GUYS
# ==========================================

class Joss(Player):
    """Joss: Plays Tit for Tat, but randomly defects 10% of the time."""
    def __init__(self):
        super().__init__("Joss")

    def make_move(self, opponent_history: List[str]) -> str:
        if not opponent_history:
            return 'O' 
        
        # 10% probability of a surprise defection
        if random.random() < 0.10:
            return 'X'
        
        return opponent_history[-1] 

class Graaskamp(Player):
    """Graaskamp: Similar to Joss, but deliberately defects on round 5."""
    def __init__(self):
        super().__init__("Graaskamp")

    def make_move(self, opponent_history: List[str]) -> str:
        # Uses own history (self.history) provided by the base Player class
        # Defects on round 5 
        if len(self.history) == 4:
            return 'X'
            
        if not opponent_history:
            return 'O' 
            
        # Works similarly to Joss (TFT with 10% random defection)
        if random.random() < 0.10:
            return 'X'
            
        return opponent_history[-1]

class Tester(Player):
    """Tester: Starts by defecting. If retaliated against, apologizes and plays TFT. Otherwise, exploits."""
    def __init__(self):
        super().__init__("Tester")

    def make_move(self, opponent_history: List[str]) -> str:
        # Uses self.history to track the current round
        if len(self.history) == 0:
            return 'X'  # Round 1: Defects to test
            
        # Evaluates the opponent's reaction in Round 2 (based on their Round 1 move)
        if len(self.history) == 1:
            if opponent_history[0] == 'X':
                return 'O'  # Apologizes if the opponent retaliated against the first defection
            else:
                return 'X'  # Keeps defecting if the opponent was a pushover (played 'O')
                
        # Subsequent rounds (Round 3 onwards)
        # Checks if the opponent reacted vindictively on the first turn
        if opponent_history[0] == 'X':
            # If they retaliated, play by Tit for Tat rules
            return opponent_history[-1]
        else:
            # If they never retaliated to the initial defection, exploit continuously
            return 'X'

# ==========================================
# THE CHAOTIC GUY
# ==========================================

class RandomPlayer(Player):
    """Random: Flips a coin every turn (50% O, 50% X)."""
    def __init__(self):
        super().__init__("RandomPlayer")

    def make_move(self, opponent_history: List[str]) -> str:
        # random.choice (50/50)
        return random.choice(['O', 'X'])