#A* with the Eucledian Distance Heurisitic
from Heuristic import *
import math
class Eucledian(Heuristic):
    def __init__(self,node):
        super().__init__(node)
        solution = None
        h_cost = 99
    def eucledian_distance(self,node):
        node.printState()
        done = []
        #self.h_cost = math.sqrt(row_differen) 
        sum = 0
        #node.current_state[0][0]
        count  = 0
        x1 = x2 = y1 = y2 = 0
        while True:
            if count == 9:
                break
            value1 = 0
            value2 = 1
            one = False
            for row in node.current_state:
                for c in row:
                    tempValue = c
                    if tempValue not in done:
                        value1 = tempValue
                        x1 = node.current_state.index(row)
                        y1 = row.index(c)
                        one = True
                        break
                if one:
                    break
            two = False
            for row in node.goal:
                for c in row:
                    tempValue = c
                    if tempValue is value1:
                        value2 = tempValue
                        two = True
                        x2 = node.goal.index(row)
                        y2 = row.index(c)
                        break
                if two:
                    break
            if value1 is value2:
                temp = (x2 - x1)**2 + (y2 - y1)**2
                sum = sum + math.sqrt(temp)
                done.append(value1)                
                count = count + 1
        return sum