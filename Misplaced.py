#A* with the misplaced tile heuristics 
from Heuristic import *
class Misplaced(Heuristic):
    def __init__(self,node):
        super().__init__(node)
    def misplace_distance(self,node):
        misplaced_cnt = 0
        rIndex = 0
        cIndex = 0
        for row in node.current_state:
            for c in row:
                if c is not node.current_state[rIndex][cIndex]:
                    misplaced_cnt = misplaced_cnt + 1
                cIndex = cIndex + 1
            rIndex = rIndex + 1
        return misplaced_cnt

    def AStarSearch(self):
        self.frontier.put((self.f, self.nodeCounter, self.cur))
        while not self.frontier.empty():
            self.cur = self.frontier.get()[2]
            self.cur.spawnChild()
            if self.cur.leftChild is not None:
                if(self.cur.leftChild.checkGoal()):
                    self.cur = self.cur.leftChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.misplace_distance(self.cur.leftChild)
                f = h + self.cur.leftChild.g
                self.frontier.put((f, self.nodeCounter, self.cur.leftChild)) 
            if self.cur.rightChild is not None:
                if(self.cur.rightChild.checkGoal()):
                    self.cur = self.cur.rightChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.misplace_distance(self.cur.rightChild)
                f = h + self.cur.rightChild.g
                self.frontier.put((f, self.nodeCounter, self.cur.rightChild)) 
            if self.cur.aboveChild is not None:
                if(self.cur.aboveChild.checkGoal()):
                    self.cur = self.cur.aboveChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.misplace_distance(self.cur.aboveChild)
                f = h + self.cur.above.g
                self.frontier.put((f, self.nodeCounter, self.cur)) 
            if self.cur.belowChild is not None:
                if(self.cur.belowChild.checkGoal()):
                    self.cur = self.cur.belowChild
                    self.goalFlag = True
                    break
                self.nodeCounter = self.nodeCounter + 1
                h = self.misplace_distance(self.cur.belowChild)
                f = h + self.cur.belowChild.g
                self.frontier.put((f, self.nodeCounter, self.cur.belowChild)) 
        if(self.goalflag):
            return self.goalFlag
        return self.goalFlag
