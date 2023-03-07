import queue
q=queue.PriorityQueue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
q.put(100)
while not q.empty():
    print(q.get(),end=' ')
print('####################')
###############################
q=queue.PriorityQueue()
q.put((1,"AAA"))

q.put((3,"CCC"))
q.put((2,"BBB"))
q.put((4,"DDD"))
while not q.empty():
    print(q.get()[1],end=' ')