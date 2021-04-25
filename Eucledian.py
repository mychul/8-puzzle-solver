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
    def AStarSearch(self):
        f = 0
        self.frontier.put((f, self.nodeCounter, self.cur))
        while not self.frontier.empty():
            self.cur = self.frontier.get()[2]
            self.cur.spawnChild()
            if self.cur.leftChild is not None:
                if(self.cur.leftChild.checkGoal()):
                    self.cur = self.cur.leftChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.eucledian_distance(self.cur.leftChild)
                f = h + self.cur.leftChild.g
                self.frontier.put((f, self.nodeCounter, self.cur.leftChild)) 
            if self.cur.rightChild is not None:
                if(self.cur.rightChild.checkGoal()):
                    self.cur = self.cur.rightChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.eucledian_distance(self.cur.rightChild)
                f = h + self.cur.rightChild.g
                self.frontier.put((f, self.nodeCounter, self.cur.rightChild)) 
            if self.cur.aboveChild is not None:
                if(self.cur.aboveChild.checkGoal()):
                    self.cur = self.cur.aboveChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.eucledian_distance(self.cur.aboveChild)
                f = h + self.cur.above.g
                self.frontier.put((f, self.nodeCounter, self.cur)) 
            if self.cur.belowChild is not None:
                if(self.cur.belowChild.checkGoal()):
                    self.cur = self.cur.belowChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.eucledian_distance(self.cur.belowChild)
                f = h + self.cur.belowChild.g
                self.frontier.put((f, self.nodeCounter, self.cur.belowChild)) 
        if(self.goalflag):
            return self.goalFlag
        return self.goalFlag