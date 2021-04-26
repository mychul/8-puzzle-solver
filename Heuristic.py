#Base class for heuristic searches
from Node import *
import queue
class Heuristic:

    def __init__(self,node):
        self.cur = node
        self.explored = {None}
        self.expanded=0
        self.max_size=0
        self.nodeCounter=0
        self.frontier = queue.PriorityQueue()
        self.goalFlag=False
        self.f = 0
        self.explored_list = []
        self.frontier_list=[]
        if self.cur.checkGoal():
            self.goalReached()
        self.counter=0

    #helper function to help print steps in between    
    def expand(self,g,h,node):
        print("The best state to expand with g(n) = " + str(g) + " and h(n) = " + str(h) + " is...")
        node.printState()
        print("Expanding this node...")

    def checkFrontier(self,node):
        for x in self.frontier_list:
            if node.convertState() == x[0]:
                if self.f > x[1]:
                    return True
        self.frontier_list.append((node.convertState(),self.f))
        return False

    #helper function to check if node up for consideration has already been previously explored or not
    def checkSet(self,node):
        if node.convertState in self.explored:
            for x in self.explored_list:
                if node.convertState() == x[0]:
                    if self.f > x[1]:
                        return True
        
        return False
    def addExplored(self,node):
        self.explored_list.append((node.convertState(),self.f))
        self.explored.add(node.convertState())
    
    def addFrontier(self,node):
        self.frontier.put((self.f, self.nodeCounter, node))

    #helper function to display max amount of nodes
    def checkMax(self,curr_size):
        if curr_size > self.max_size:
            self.maxsize = curr_size


    #helper function that traces route to solution node and saves into a list        
    def traceSolution(self):
        solution=[]
        while (self.cur.spawnMethod is not None):
            solution.append(self.cur.spawnMethod)
            self.cur = self.cur.parent

        return solution

    #Results routine: Print path, print number of nodes expanded, print max nodes
    def goalReached(self):
        path = self.traceSolution()
        if path is not None:
            path.reverse()
            self.expanded = len(path)
            for x in path:
                print (x)
        elif path is None:
            print ("The given state was the goal state.")
        print ("To solve this problem the search algorithm expanded " + str(self.expanded) + " nodes.")
        print ("The maximum number of nodes at any one time was: " + str(self.max_size))
