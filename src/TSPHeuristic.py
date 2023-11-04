import numpy as np
from abc import ABC, abstractmethod


class TSPHeuristic(ABC):
    def __init__(self, distance_matrix) -> None:
        self.distance_matrix = distance_matrix
        self.n = len(distance_matrix)

    @abstractmethod
    def solve():
        pass
    

    def cost(permutation: np.array):
        return

