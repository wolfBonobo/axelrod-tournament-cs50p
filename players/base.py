from abc import ABC, abstractmethod
from typing import List

class Player(ABC):
    """
    Abstract class that defines the interface for any game strategy.
    """

    def __init__(self, name: str):
        self.name: str = name
        self.history: List[str] = []  # Stores 'O' (Cooperate) or 'X' (Defect)
        self.score: int = 0

    def reset(self) -> None:
        """Resets the player's state for a new match."""
        self.history = []
        self.score = 0

    @abstractmethod
    def make_move(self, opponent_history: List[str]) -> str:
        """
        Strategy decision logic.
        Must return 'O' to Cooperate or 'X' to Defect.
        """
        pass

    def record_move(self, move: str) -> None:
        """Records the executed move in its own history."""
        self.history.append(move)

    def __str__(self) -> str:
        return self.name