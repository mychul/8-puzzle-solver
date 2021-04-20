from Problems import problems

class node(problems):
    def __init__(self):
        self.parent = None
        self.aboveChild = None
        self.belowChild = None
        self.rightChild = None
        self.leftChild = None
        self.state = state
    def get(self):  return self.obj
    def set(self, obj):     self.obj = obj
    #Node parent = self.obj
