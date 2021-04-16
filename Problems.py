class problems:
    #initial state should be a two diminesional int array
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.goal= [[1,2,3],[4,5,6],[7,8,0]]
        
        #goal = [1][2][3]
        #       [4][5][6]
        #       [7][8]][0]
    
    def identifyBlankPos(self):
        for row in 2:
            for col in 2:
                if self.origin[row][col] == 0:
                    x = row
                    y = col
    #[Left,Right,Above,Below]    
    #blank is corner
        if x is 0 and y is 0:   #if Top Left  [0,0]
            return [0,1,0,1]    #Allow swapBelow swapRight
        elif x is 2 and y is 0: #if Bottom Left [2,0]
            return [0,1,1,0]    #Allow swapAbove, swapRight 
        elif x is 0 and y is 2: #if Top Right [0,2]
            return [1,0,0,1]    #Allow swapLeft swapBelow
        elif x is 2 and y is 2:  #if Bottom Right [2,2]
            return [1,0,1,0]    #allow swapAbove swapLeft
    #blank is a side
        elif x is 1 and y is 0: #if Left [1,0]
            return [0,1,1,1]    #Above Below Right
        elif x is 0 and y is 1: #if Top [0,1]
            return [1,1,0,1]    #Right Left Below
        elif x is 2 and y is 1: #if Bottom [2,1]
            return [1,1,1,0]    #Above Left Right
        elif x is 1 and y is 2: #if Right  [1,2]
            return [1,0,1,1]    #LeftAboveBelow
    #blank is middle
        elif x is 1 and y is 1: #if middle [1,1]
            return [1,1,1,1]    #AboveBelowLeftRight

    def checkGoal(self):
        if self.goal == self.current_state:
            return True
        else:
            return False