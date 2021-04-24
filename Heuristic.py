#Base class for heuristic searches
from Node import *
class Heuristic:

    def __init__(self,node):
        start = node
        explored={copy.deepcopy(start.initial_state)}
        expanded=0
        max_size=0

    #helper function to help print steps in between    
    def expand(self,g,h,node):
        print("The best state to expand with g(n) = " + g + " and h(n) = " + h + " is...")
        node.printState()
        print("Expanding this node...")

    #helper function to check if node up for consideration has already been previously explored or not
    def checkSet(self,node):
        if node.current_state in self.explored:
            return True
        else:
            return False
    #helper function to display max amount of nodes
    def checkMax(self,curr_size):
        if len(curr_size) > self.max_size:
            self.maxsize = len(curr_size)
        return

    #helper function that traces route to solution node and saves into a list        
    def traceSolution(self,node):
        cur = node
        solution=[]
        while (cur.spawnMethond is not None):
            solution.add(node.spawnMethod)
            cur = cur.parent

        return solution

    #Results routine: Print path, print number of nodes expanded, print max nodes
    def goalReached(self):
        path = self.traceSolution()
        path.reverse()
        self.expanded = len(path)
        for x in path:
            print (path[x])
        print ("To solve this problem the serach algorithm expanded " + self.expanded + " nodes.")
        print ("The maximum number of nodes at any one time was: " + self.max_size)
