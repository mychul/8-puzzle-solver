#A* with the Eucledian Distance Heurisitic
from Heuristic import *
import math
class Eucledian(Heuristic):
    def __init__(self,node):
        super().__init__(node)
        solution = None
        h_cost = 99
    def eucledian_distance(self,node):
        #self.h_cost = math.sqrt(row_differen) 
        sum = 0
        #node.current_state[0][0]
        for row in node.current_state:
            for c in row:
                pass
                #sum = sum + (self.cur.goal[c]] - node.current_state[c])^2
        distance = math.sqrt(sum)
        return distance