#while loop:
count = 0
while (count < 3):
 count = count + 1 
 print("Hello Geek")

 # Single statement while block count = 0
while (count == 0): print("Hello Geek")

#for in Loop:
print("List Iteration")
l = ["geeks", "for", "geeks"] 
for i in l:
    print(i)


print("\nTuple Iteration")
t = ("geeks", "for", "geeks") 
for i in t:
    print(i)


# Iterating by index
list = ["geeks", "for", "geeks"] 
for index in range(len(list)):
      print (list[index])



# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
       if letter == 'e' or letter == 's':
               continue
       print ('Current Letter :',letter)

var = 10


#Creating a Function
def my_function(): 
  print("Hello from a function")

#Calling a Function
def my_function(): 
  print("Hello from a function")
my_function()


#parameters
def my_function(fname):
   print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(country="Norway"):   #Norway is default value 
   print("i am from "+country )
my_function("UK")
my_function("US")
my_function("Ireland")

#Passing a List as a Parameter
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)



#return value
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))




#This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
      print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#class
class MyClass: x = 5
p1 = MyClass() 
print(p1.x)


#init function
class Person:

 def __init__(self, name, age): 
   self.name = name
   self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

class Person:

 def __init__(self, name, age): 
   self.name = name
   self.age = age

   
 def myfunc(self):
  print("Hello my name is " + self.name)
p1 = Person("John", 36) 
p1.myfunc()