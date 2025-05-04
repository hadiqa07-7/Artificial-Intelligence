
#question 1:
class stack:
    def __init__(self):   #used to create constructor 
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
 
    def pop(self):     
        if not self.isempty():     #self.stack = [] creates an individual stack (list) for each object you create from the Stack class.

                                    #self is used to refer to the current object (so each object can have its own stack list).

                                    #Without self, you'd have one shared stack for all objects, which is not the behavior you want when dealing with separate object
         return self.stack.pop()#pop() is built in function in python for list that deletes a the top element
        return "stack is empty"
    

    def peek(self):
        if not self.isempty():
          return  self.stack[-1]
        
        return "stack is empty"
    

    def isempty(self):
        return len(self.stack)==0
    

    def display(self):
        print("Stack:", self.stack)




obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.peek()
print(obj.peek())
obj.pop()
obj.display()
obj.pop()
obj.pop()
obj.display()
obj.isempty()
print(obj.isempty())
obj.push("hello")
obj.display()


#question 2:


class Queue:
    def __init__(self):
        self.queue = []  

    def enqueue(self, item):
        self.queue.append(item)  

    def dequeue(self):
        if not self.isempty():
            return self.queue.pop(0)  
        return "Queue is empty"  

    def peek(self):
        if not self.isempty():
            return self.queue[0]  
        return "Queue is empty"  

    def isempty(self):
        return len(self.queue) == 0  

    def display(self):
        print("Queue:", self.queue)  


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek()) 

q.dequeue()  
q.display()  

q.dequeue()  
q.dequeue()  
q.display()  

print(q.isempty())  

q.enqueue("hello")
q.display()  


#Question 3:
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Not found




arr = [2, 5, 8, 12, 16, 23, 38]
target = 23

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")






























