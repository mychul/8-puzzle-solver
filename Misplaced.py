#A* with the misplaced tile heuristics 
from Heuristic import *
class Misplaced(Heuristic):
    def __init__(self,node):
        super().__init__(node)

