#Uniform Cost Search
from Heuristic import *
class Uniform(Heuristic):
    def __init__(self,node):
        super().__init__(node)

    def Search(self):
        #if the initial node supplied was the goal stat

        if self.cur.checkGoal():
            return True
        #putting our initial node onto frontier

        self.frontier.put((self.f, self.nodeCounter, self.cur))
        self.frontier_list.append((self.cur.convertState(),self.f))
        self.addExplored(self.cur)
        self.checkMax(self.frontier.qsize())

        #run till frontier is empty
        while not self.frontier.empty():

            #get a node from frontier
            self.cur = self.frontier.get()[2]
            if(self.cur.checkGoal()):
                return True
                    
            self.expand(self.cur.g,self.cur.h,self.cur)
            if (self.cur.convertState(),self.f) in self.frontier_list:
                self.frontier_list.remove((self.cur.convertState(),self.f))
            #run helper function to generate all possible children
            self.cur.spawnChild()
            #check if left child was generated

            if self.cur.leftChild is not None:
                
                #increment global node counter to guarantee FIFO during collision within priority
                self.nodeCounter = self.nodeCounter + 1
                #calculate h(n) value associated with node using A* euclidian heuristic
                self.cur.leftChild.h=0
                #add h and g to f
                self.f = self.cur.leftChild.h + self.cur.leftChild.g
                #check if node state and f value pairing exist within the explored region
                if self.checkSet(self.cur.leftChild) is False:
                    if self.checkFrontier(self.cur.leftChild) is False:
                        self.addFrontier(self.cur.leftChild)
                        self.checkMax(self.frontier.qsize())
                        
                    
            if self.cur.rightChild is not None:
                
                self.nodeCounter = self.nodeCounter + 1
                self.cur.rightChild.h = 0
                self.f = self.cur.rightChild.h + self.cur.rightChild.g
                if self.checkSet(self.cur.rightChild) is False:
                    if self.checkFrontier(self.cur.rightChild) is False:
                        self.addFrontier(self.cur.rightChild)
                        self.checkMax(self.frontier.qsize())
                        

            if self.cur.aboveChild is not None:
                
                self.nodeCounter = self.nodeCounter + 1
                self.cur.aboveChild.h = 0
                self.f = self.cur.aboveChild.h + self.cur.aboveChild.g
                if self.checkSet(self.cur.aboveChild) is False:
                    if self.checkFrontier(self.cur.aboveChild) is False:
                        self.addFrontier(self.cur.aboveChild)
                        self.checkMax(self.frontier.qsize())
                        

            if self.cur.belowChild is not None:
                self.nodeCounter = self.nodeCounter + 1
                self.cur.belowChild.h = 0
                self.f = self.cur.belowChild.h + self.cur.belowChild.g
                if self.checkSet(self.cur.belowChild) is False:
                    if self.checkFrontier(self.cur.belowChild) is False:
                        self.addFrontier(self.cur.belowChild)
                        self.checkMax(self.frontier.qsize())
                        
            self.addExplored(self.cur) 

        #if we have found the solution escape early
        if(self.goalFlag):
            return self.goalFlag
        #if we have explored all there is within the frontier return false
        return self.goalFlag