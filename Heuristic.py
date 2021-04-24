#Base class for heuristic searches
from Node import *
class Heurisitic:

    def __init__(self,problem):
        start = problem
        explored={start.initial_state}
        

    #helper function to check if node up for consideration has already been previously explored or not
    def checkSet(self,node):
        if node.current_state in self.explored:
            return True
        else:
            return False

    #helper function that traces route to solution node and saves into a list        
    def traceSolution(self,node):
        cur = node
        solution=[]
        while (cur.spawnMethond is not None):
            solution.add(node.spawnMethod)
            cur = cur.parent

        return solution

    #runs the trace helper function and reverses the resulting list to print
    def goalReached(self):
        path = self.traceSolution()
        path.reverse()
        for x in path:
            print (path[x])
