from Problems import problems
import copy

class node(problems):
    def __init__(self,state):
        super().__init__(state)
        self.parent = None
        self.aboveChild = None
        self.belowChild = None
        self.rightChild = None
        self.leftChild = None
        self.spawnMethod= None
        self.g = 0
    def setParent(self,p):
        #DEBGU
        #print("DEBUGU")
        self.parent = p
        #DEBUG
        #print("DEBUGA")
        #self.printState()
    def spawnChild(self):
        pos = self.identifyBlankPos()
        r = pos[0]
        c = pos[1]
        if pos[2]==1:
            #spawnleft
            dummy = self.current_state[r][c-1] 
            new_state = copy.deepcopy(self.current_state)
            new_state[r][c-1] = 0
            #self.printState() #Debug
            new_state[r][c] = dummy
            #DEBUG BLOCK
            # for a in new_state:
            #     for b in a:
            #         print(b,end = " ")
            #     print()
            self.leftChild = node(new_state)
            # self.leftChild.printState() #debug
            #self.printState() #Debug 
            self.leftChild.setParent(self)  ###################FIX THIS
            #self.printState() #Debug 
            self.leftChild.spawnMethod="Swap Blank Left"
            self.leftChild.g=self.g+1
        new_state=None
        #self.printState() #Debug 
        if pos[3]==1:
            #spawnRight
            dummy = self.current_state[r][c+1]
            new_state = copy.deepcopy(self.current_state)
            new_state[r][c+1]= 0
            new_state[r][c] = dummy
            self.rightChild = node(new_state)
            self.rightChild.setParent(self)
            self.rightChild.spawnMethod="Swap Blank Right"
            self.rightChild.g=self.g+1
        new_state = None
        if pos[4]==1:
            #spawnAbove:
            dummy = self.current_state[r-1][c]
            new_state = copy.deepcopy(self.current_state)
            new_state[r-1][c]= 0
            new_state[r][c] = dummy
            self.aboveChild= node(new_state)
            self.aboveChild.setParent(self)
            self.aboveChild.spawnMethod="Swap Blank Up"
            self.aboveChild.g=self.g+1
        new_state=None
        if pos[5]==1:
            #spawnBelow:
            
            dummy = self.current_state[r+1][c]
            #print(dummy)    #debug
            #self.printState()
            new_state = copy.deepcopy(self.current_state)
            new_state[r+1][c]= 0
            new_state[r][c] = dummy
            #DEBUG BLOCK
            #for a in new_state:
            #    for b in a:
            #        print(b,end = " ")
            #    print()
            self.belowChild= node(new_state)
            self.belowChild.setParent(self)
            self.belowChild.spawnMethod="Swap Blank Down" 
            self.belowChild.g=self.g+1
            #self.belowChild.printState()   #debug         
        return
    def printChildren(self):
        if self.leftChild is not None:
            print("Left Child:")
            self.leftChild.printState()
        if self.rightChild is not None:    
            print("Right Child:")
            self.rightChild.printState()
        if self.aboveChild is not None:    
            print("Above Child:")
            self.aboveChild.printState()
        if self.belowChild is not None:
            print("Below Child:")
            self.belowChild.printState()

    