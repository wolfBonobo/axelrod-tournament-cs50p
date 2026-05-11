from typing import Dict, Any
from players.base import Player

class Match:
    """Manages a match between two players over a set number of rounds."""
    
    # Payoff matrix: (Player 1 Score, Player 2 Score)
    # 'O' = Cooperate, 'X' = Defect
    PAYOFFS = {
        ('O', 'O'): (3, 3),  # Reward for mutual cooperation
        ('X', 'X'): (1, 1),  # Punishment for mutual defection
        ('O', 'X'): (0, 5),  # Sucker's payoff and Temptation
        ('X', 'O'): (5, 0)   # Temptation and Sucker's payoff
    }

    def __init__(self, player1: Player, player2: Player, rounds: int = 100):
        self.player1 = player1
        self.player2 = player2
        self.rounds = rounds

    def play(self) -> Dict[str, Any]:
        """Executes the match and returns a comprehensive dictionary with results and logs."""
        self.player1.reset()
        self.player2.reset()

        # Counters for summary statistics
        p1_cooperations = 0
        p1_defections = 0
        p2_cooperations = 0
        p2_defections = 0

        rounds_data = []

        for round_idx in range(self.rounds):
            # Get moves from both players simultaneously
            move1 = self.player1.make_move(self.player2.history)
            move2 = self.player2.make_move(self.player1.history)

            # Record moves in each player's own history
            self.player1.record_move(move1)
            self.player2.record_move(move2)

            # Calculate and update scores
            p1_points, p2_points = self.PAYOFFS[(move1, move2)]
            self.player1.score += p1_points
            self.player2.score += p2_points

            # Update counters for statistics
            if move1 == 'O': p1_cooperations += 1
            else: p1_defections += 1
            
            if move2 == 'O': p2_cooperations += 1
            else: p2_defections += 1

            # Save the exact details of this round
            rounds_data.append({
                "round_number": round_idx + 1,
                "p1_move": move1,
                "p2_move": move2,
                "p1_points": p1_points,
                "p2_points": p2_points,
                "p1_accumulated_score": self.player1.score,
                "p2_accumulated_score": self.player2.score
            })

        # Structure everything into a single dictionary that is easy to process and export (e.g., to JSON or Pandas)
        return {
            "player1_name": self.player1.name,
            "player2_name": self.player2.name,
            "p1_final_score": self.player1.score,
            "p2_final_score": self.player2.score,
            "summary": {
                "p1_cooperations": p1_cooperations,
                "p1_defections": p1_defections,
                "p2_cooperations": p2_cooperations,
                "p2_defections": p2_defections,
            },
            "rounds_data": rounds_data
        }