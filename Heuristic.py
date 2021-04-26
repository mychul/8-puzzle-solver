#Base class for heuristic searches
from Node import *
import queue
class Heuristic:

    def __init__(self,node):
        self.cur = node
        self.explored = {}
        self.expanded=0
        self.max_size=0
        self.nodeCounter=0
        self.frontier = queue.PriorityQueue()
        self.goalFlag=False
        self.f = 0
        self.explored_pairs = {}
        
        if self.cur.checkGoal():
            self.goalReached()

    #helper function to help print steps in between    
    def expand(self,g,h):
        print("The best state to expand with g(n) = " + g + " and h(n) = " + h + " is...")
        self.cur.printState()
        print("Expanding this node...")

    def checkFrontier(self,node):
        if node.convertState() in self.frontier_dict.keys():
            return (True, self.frontier_dict.get(node.converState()))
        else:
            return (False,-1)

    #helper function to check if node up for consideration has already been previously explored or not
    def checkSet(self,node):
        
        #dict(nodestate:f)
        #explored set(nodestate)
        #check for collision within the set
        #lookup the pairing of nodestate and f
        #return f
        #><=

        #checking = {self.f,node.convertState()}
        if node.convertState() in self.explored:
            if self.f in explored_pairs and node.convertState() == explored_pairs.get(self.f):
                return True
        else:
            #if it has not been add the node to the explored set and return false in order to consider it
            self.explored.add(node.convertState())
            self.explored_pairs.update({self.f:node.convertState()})
            return False
    #helper function to display max amount of nodes
    def checkMax(self,curr_size):
        if len(curr_size) > self.max_size:
            self.maxsize = len(curr_size)
        return

    #helper function that traces route to solution node and saves into a list        
    def traceSolution(self):
        solution=[]
        while (self.cur.spawnMethond is not None):
            solution.add(node.spawnMethod)
            self.cur = self.cur.parent

        return solution

    #Results routine: Print path, print number of nodes expanded, print max nodes
    def goalReached(self):
        path = self.traceSolution(self.cur)
        if path is not None:
            path.reverse()
            self.expanded = len(path)
            for x in path:
                print (path[x])
        elif path is None:
            print ("The given state was the goal state.")
        print ("To solve this problem the serach algorithm expanded " + self.expanded + " nodes.")
        print ("The maximum number of nodes at any one time was: " + self.max_size)
