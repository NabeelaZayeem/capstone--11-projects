class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
        print(self.items)
    def pop(self):
       return self.items.pop()
       print(self.items)
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
s=Stack()
s.push(5)
# s.push(15)
# s.push(500)
s.pop()
# print(items[])