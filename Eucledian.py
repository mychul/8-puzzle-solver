#A* with the Eucledian Distance Heurisitic
from Heuristic import *
import math
class Eucledian(Heuristic):
    def __init__(self,node):
        super().__init__(node)
        solution = None
        h_cost = 99
    def eucledian_distance(self,node):
        #node.printState()
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

    def AStarSearch(self):
        #if the initial node supplied was the goal state
        if self.cur.checkGoal:
            return True
        #putting our initial node onto frontier
        self.frontier.put((self.f, self.nodeCounter, self.cur))
        self.frontier_list.append((self.cur.convertState(),self.f))
        #run till frontier is empty
        while not self.frontier.empty():
            #get a node from frontier
            self.cur = self.frontier.get()[2]
            self.frontier_list.remove((self.cur.convertState(),self.f))
            #run helper function to generate all possible children
            self.cur.spawnChild()
            #check if left child was generated
            if self.cur.leftChild is not None:
                #check if left child is the goal
                if(self.cur.leftChild.checkGoal()):
                    self.cur = self.cur.leftChild
                    self.goalFlag = True
                    break
                #increment global node counter to guarantee FIFO during collision within priority
                self.nodeCounter = self.nodeCounter + 1
                #calculate h(n) value associated with node using A* euclidian heuristic
                h = self.eucledian_distance(self.cur.leftChild)
                #add h and g to f
                self.f = h + self.cur.leftChild.g
                #check if node state and f value pairing exist within the explored region
                if self.checkSet(self.cur.leftChild) is False:
                    if self.checkFrontier(self.cur.leftChild) is False:
                        self.addFrontier(self.cur.leftChild) 
                    

            if self.cur.rightChild is not None:
                if(self.cur.rightChild.checkGoal()):
                    self.cur = self.cur.rightChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.eucledian_distance(self.cur.rightChild)
                self.f = h + self.cur.rightChild.g
                if self.checkSet(self.cur.rightChild) is False:
                    if self.checkFrontier(self.cur.rightChild) is False:
                        self.addFrontier(self.cur.rightChild)

            if self.cur.aboveChild is not None:
                if(self.cur.aboveChild.checkGoal()):
                    self.cur = self.cur.aboveChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.eucledian_distance(self.cur.aboveChild)
                self.f = h + self.cur.above.g
                if self.checkSet(self.cur.aboveChild) is False:
                    if self.checkFrontier(self.cur.aboveChild) is False:
                        self.addFrontier(self.cur.aboveChild)

            if self.cur.belowChild is not None:
                if(self.cur.belowChild.checkGoal()):
                    self.cur = self.cur.belowChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.eucledian_distance(self.cur.belowChild)
                self.f = h + self.cur.belowChild.g
                if self.checkSet(self.cur.belowChild) is False:
                    if self.checkFrontier(self.cur.belowChild) is False:
                        self.addFrontier(self.cur.belowChild)
            self.addExplored(self.cur) 

        #if we have found the solution escape early
        if(self.goalflag):
            return self.goalFlag
        #if we have explored all there is within the frontier return false
        return self.goalFlag