from abc import ABC, abstractmethod
from typing import List

class Player(ABC):
    """
    Clase abstracta que define la interfaz para cualquier estrategia de juego.
    """

    def __init__(self, name: str):
        self.name: str = name
        self.history: List[str] = []  # Almacena 'O' (Cooperar) o 'X' (Traicionar)
        self.score: int = 0

    def reset(self) -> None:
        """Reinicia el estado del jugador para un nuevo enfrentamiento."""
        self.history = []
        self.score = 0

    @abstractmethod
    def make_move(self, opponent_history: List[str]) -> str:
        """
        Lógica de decisión de la estrategia.
        Debe devolver 'O' para Cooperar o 'X' para Traicionar.
        """
        pass

    def record_move(self, move: str) -> None:
        """Registra el movimiento realizado en el historial propio."""
        self.history.append(move)

    def __str__(self) -> str:
        return self.name