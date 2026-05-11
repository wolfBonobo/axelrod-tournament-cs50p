from typing import List, Dict, Any
from players.base import Player
from core.match import Match
class Tournament:
    """Handles a Round-Robin tournament where every player competes against everyone else."""

    def __init__(self, players: List[Player], rounds_per_match: int = 100):
        self.players = players
        self.rounds_per_match = rounds_per_match
        self.total_scores: Dict[str, int] = {player.name: 0 for player in players}
        self.match_logs: List[Dict[str, Any]] = []

    def run(self) -> Dict[str, Any]:
        """Runs the tournament, collects logs, and calculates final rankings."""
        # Reset total scores and match logs in case run() is called multiple times
        for name in self.total_scores:
            self.total_scores[name] = 0
        self.match_logs = []

        # Round-Robin: Every player against every other player
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                p1 = self.players[i]
                p2 = self.players[j]

                # Create and play the match
                match = Match(p1, p2, self.rounds_per_match)
                match_result = match.play()

                # Accumulate total scores for the tournament ranking
                self.total_scores[p1.name] += match_result["p1_final_score"]
                self.total_scores[p2.name] += match_result["p2_final_score"]

                # Store the complete match dictionary in the tournament logs
                self.match_logs.append(match_result)

        # Sort the leaderboard in descending order (highest score first)
        sorted_leaderboard = dict(sorted(self.total_scores.items(), key=lambda item: item[1], reverse=True))

        # Return a comprehensive payload with the final standings and all match data
        return {
            "leaderboard": sorted_leaderboard,
            "matches": self.match_logs
        }