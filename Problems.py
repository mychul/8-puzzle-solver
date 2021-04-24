class problems:
    #initial state should be a two diminesional int array
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.goal= [[1,2,3],[4,5,6],[7,8,0]]
        
        #goal = [1][2][3]
        #       [4][5][6]
        #       [7][8]][0]
    
    def identifyBlankPos(self):
        #print("finding blank pos") DEBUG
        for row in range(3):
            for col in range(3):
                #print ("...")  #DEBUG
                if self.current_state[row][col] == 0:
                    x = row
                    y = col
                    #print (x) #Debug
                    #print (y) #Debug
                    #[Rowpos,Colpos,Left,Right,Above,Below]    
                    #blank is corner
                    if x is 0 and y is 0:   #if Top Left  [0,0]
                        #print("Blank is tl")   DEBUG
                        return [x,y,0,1,0,1]    #Allow swapBelow swapRight
                    elif x is 2 and y is 0: #if Bottom Left [2,0]
                        #print("Blank is bl")   #DEBUG
                        return [x,y,0,1,1,0]    #Allow swapAbove, swapRight 
                    elif x is 0 and y is 2: #if Top Right [0,2]
                        #print("Blank is tr") #Debug
                        return [x,y,1,0,0,1]    #Allow swapLeft swapBelow
                    elif x is 2 and y is 2:  #if Bottom Right [2,2]
                        #print("Blank is br")   #debug
                        return [x,y,1,0,1,0]    #allow swapAbove swapLeft
                    #blank is a side
                    elif x is 1 and y is 0: #if Left [1,0]
                        #print("Blank is l")    #DEBUG
                        return [x,y,0,1,1,1]    #Above Below Right
                    elif x is 0 and y is 1: #if Top [0,1]
                        #print("Blank is t")    #DEBUG
                        return [x,y,1,1,0,1]    #Right Left Below
                    elif x is 2 and y is 1: #if Bottom [2,1]
                        #print("Blank is b")    #debug
                        return [x,y,1,1,1,0]    #Above Left Right
                    elif x is 1 and y is 2: #if Right  [1,2]
                        #print("Blank is r")    #DEBUG
                        return [x,y,1,0,1,1]    #LeftAboveBelow
                    #blank is middle
                    elif x is 1 and y is 1: #if middle [1,1]
                        #print("Blank is m")    #DEBUG
                        return [x,y,1,1,1,1]    #AboveBelowLeftRight
        return [0,0,0,0,0,0]

    def checkGoal(self):
        if self.goal == self.current_state:
            return True
        else:
            return False
    def printState(self):  
        for r in self.current_state:
            for c in r:
                print(c,end = " ")
            print()
    #due to lists being a unhashable type we need to convert our lists of lists into a tuple in order to store within our sets
    def convertState(self):
        flatList=[]
        for r in self.current_state:
            for c in r:
                flatList.append(c)
        return tuple(flatList)