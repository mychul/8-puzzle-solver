import queue

mypq = queue.PriorityQueue()
mypq.put((2,0,"happy"))
mypq.put((1,1,"sad"))
mypq.put((1,2,"confused"))
print(mypq.get()[2])
#cur = mypq.get()[2]