#A* with the misplaced tile heuristics 
from Heuristic import *
class Misplaced(Heuristic):
    def __init__(self,problem):
        super().__init__(problem)

