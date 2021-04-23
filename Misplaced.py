#A* with the misplaced tile heuristics 
from Node import *

def __init__(self,problem):
    start = problem
    explored={start.initial_state}
    solution = None
    if start.checkGoal():
        pass

#helper function to check if node up for consideration has already been previously explored or not
def checkSet(self,node):
    if node.current_state in self.explored:
        return True
    else:
        return False
def traceSolution(self,node):
    pass
def goalReached(self):
    path = self.solution()
    print (path)

