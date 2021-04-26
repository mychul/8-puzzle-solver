#Uniform Cost Search
from Heuristic import *
class Uniform(Heuristic):
    def __init__(self,node):
        super().__init__(node)

    def Search(self):
        #if the initial node supplied was the goal state

         ###################
        print(str(self.counter))
        self.counter = self.counter +1
        ########################

        if self.cur.checkGoal():
            return True
        #putting our initial node onto frontier
        ###################
        print(str(self.counter))
        self.counter = self.counter +1

        ########################
        self.frontier.put((self.f, self.nodeCounter, self.cur))
        self.frontier_list.append((self.cur.convertState(),self.f))
        self.checkMax(self.frontier.qsize())

         ###################
        print(str(self.counter))
        self.counter = self.counter +1
        ########################

        #run till frontier is empty
        while not self.frontier.empty():
            
            ###################
            print(str(self.counter))
            self.counter = self.counter +1
            ########################

            #get a node from frontier
            self.cur = self.frontier.get()[2]
            self.frontier_list.remove((self.cur.convertState(),self.f))
            #run helper function to generate all possible children
            self.cur.spawnChild()
            #check if left child was generated

            ###################
            print(str(self.counter))
            self.counter = self.counter +1
            ########################

            if self.cur.leftChild is not None:
                #check if left child is the goal
                if(self.cur.leftChild.checkGoal()):
                    self.cur = self.cur.leftChild
                    self.goalFlag = True
                    break
                #increment global node counter to guarantee FIFO during collision within priority
                self.nodeCounter = self.nodeCounter + 1
                #calculate h(n) value associated with node using A* euclidian heuristic
                h = 0
                #add h and g to f
                self.f = h + self.cur.leftChild.g
                #check if node state and f value pairing exist within the explored region
                if self.checkSet(self.cur.leftChild) is False:
                    if self.checkFrontier(self.cur.leftChild) is False:
                        self.addFrontier(self.cur.leftChild)
                        self.checkMax(self.frontier.qsize())
                        self.expand(self.cur.leftChild.g,h,self.cur.leftChild) 
                    
            if self.cur.rightChild is not None:
                if(self.cur.rightChild.checkGoal()):
                    self.cur = self.cur.rightChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = 0
                self.f = h + self.cur.rightChild.g
                if self.checkSet(self.cur.rightChild) is False:
                    if self.checkFrontier(self.cur.rightChild) is False:
                        self.addFrontier(self.cur.rightChild)
                        self.checkMax(self.frontier.qsize())
                        self.expand(self.cur.rightChild.g,h,self.cur.rightChild)

            if self.cur.aboveChild is not None:
                if(self.cur.aboveChild.checkGoal()):
                    self.cur = self.cur.aboveChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = 0
                self.f = h + self.cur.above.g
                if self.checkSet(self.cur.aboveChild) is False:
                    if self.checkFrontier(self.cur.aboveChild) is False:
                        self.addFrontier(self.cur.aboveChild)
                        self.checkMax(self.frontier.qsize())
                        self.expand(self.cur.aboveChild.g,h,self.cur.aboveChild)

            if self.cur.belowChild is not None:
                if(self.cur.belowChild.checkGoal()):
                    self.cur = self.cur.belowChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = 0
                self.f = h + self.cur.belowChild.g
                if self.checkSet(self.cur.belowChild) is False:
                    if self.checkFrontier(self.cur.belowChild) is False:
                        self.addFrontier(self.cur.belowChild)
                        self.checkMax(self.frontier.qsize())
                        self.expand(self.cur.belowChild.g,h,self.cur.belowChild)
            self.addExplored(self.cur) 

        #if we have found the solution escape early
        if(self.goalflag):
            return self.goalFlag
        #if we have explored all there is within the frontier return false
        return self.goalFlag