#A* with the Eucledian Distance Heurisitic
from Node import *

class Eucledian:
     def __init__(self,problem):
        start = problem
        explored = [start.initial_state]
        solution = None
        if start.checkGoal():
            

def checkSet(self,node):
    if node.current_state in self.explored: 
        return True
    else:
        return False