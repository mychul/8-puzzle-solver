from array import *
from Problems import *
from Node import *
from Misplaced import *
from Eucledian import *
from Uniform import *
pad = [0,0,0]

print("Welcome to 861126014 & 861199635 8 puzzle solver.")    
choice = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\nChoice: ")
choice = int(choice)
if choice == 1:
    choice = input("What difficulty do you want the default puzzle to be: \"1\" for Easy \"2\" for Hard\nChoice: ")
    choice = int(choice)
    if choice == 1: 
        pad = [[1,2,0],[4,5,3],[7,8,6]]
        # for debug 
        # for r in pad:
        #     for c in r:
        #         print(c,end = " ")
        #     print()
    elif choice == 2:
        pad = [[0,1,2],[4,5,3],[7,8,6]]
        # for debug 
        # for r in pad:
        #     for c in r:
        #         print(c,end = " ")
        #     print()
elif choice == 2:
    pad = [[0,0,0],[0,0,0],[0,0,0]]
    print("Enter your puzzle, use a zero to represent the blank")
    i = 0
    if i == 0:
        x, y, z = map(int,input("Enter the first row, use space or tabs between numbers: ").split()) #maps values delimited by space 
        #print("")
        pad[i][0] = x
        pad[i][1] = y
        pad[i][2] = z
    i = 1
    if i == 1:
        x, y, z = map(int,input("Enter the second row, use space or tabs between numbers: ").split())
        # print("")
        pad[i][0] = x
        pad[i][1] = y
        pad[i][2] = z
    i = 2
    if i == 2:
        x, y, z = map(int,input("Enter the third row, use space or tabs between numbers: ").split())
        #print("")
        pad[i][0] = x
        pad[i][1] = y
        pad[i][2] = z
choice = input("\nEnter your choice of algorithm\n1 - Uniform Cost Search\n2- A* with the Misplaced Tile heuristic.\n3 - A* with the Euclidean distance heuristic.\n\nChoice: ")
choice = int(choice)
initial_node = node(pad)

if choice == 1:
    uni = Uniform(initial_node)
    flag = uni.Search()
    if flag:
        uni.goalReached()
    else:
        print("Unsolvable")
if choice == 2:
    mis = Misplaced(initial_node)
    flag = mis.AStarSearch()
    if flag:
        mis.goalReached()
    else:
        print("Unsolvable")
if(choice == 3):
    euc = Eucledian(initial_node)
    flag = euc.AStarSearch()
    if flag:
        euc.goalReached()
    else:
        print("Unsolvable")


#initial_problem = problems(pad) 
#initial_problem.printState()
#testNode= node(pad)
#testNode.spawnChild()
#testNode.printChildren()

    # for debug 
    # for r in pad:
    #     for c in r:
    #         print(c,end = " ")
    #     print()