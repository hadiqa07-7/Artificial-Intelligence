# is used for comments
#input:
X=1
#THE INITIAL VALUE OF X IS 1
if X>0:
 print("these are two comments ")  #print a string

#multiple statements on a single line
print("statement 1")
print("statement 2")
print("statement 1");print("statement 2")


#indentation is required
#X=1

if X>0:
print("this statement has no indentation ")
print("this statement has no indentation ")
#error: expected an indented block

#with space indentaton 
x=1
if x>0:
 print("this statement has a single space indentation ")
 print("this statement has a single space indentation ")

#with tab indentation
x=1
if x>0:
    print("this statement has a single tab indentation ")
    print("this statement has a single tab indentation ")


#with tab+space indentation
x=1
if x>0:
     print("this statement has a  tab+space indentation ")
     print("this statement has a  tab+space indentation ")

# DATA TYPES AND TYPE CASTING
# To check the type of any variable  we use the type() function in Python.


a=1452
print(type(a))

b=(-4587)
print(type(b))

c=0
print(type(c))

g=1.03
print(type(g))

h=-11.23
print(type(h))

i=.34
print(type(i))

j=2.12e-10
print(type(j))

k=5E220
print(type(k))

#complex numbers
x=complex(1,2)
print(type(x))

z=1+2j
print(type(z))

z=1+2J
print(type(z))


#boolean(bool)
x=True
print(type(x))

y=False
print(type(y))

#strings 

str1="string 1"  #works within double quote
print(str1)

str1='string 1'  #works within single quote
print(str1)
 
str2 ='string  2" 
print(str2)   #error



#special characters in strings
print("this is backlash (\\) mark")
print("this is a tab \t mark")
print("these are \'single quotes\' ")
print("these are \"double quotes\" ")
print("this is a newline\nNew line")


#string indeces and accessing string elements

str1="python tutorial"
print(str1[0]) #print first character
print(str1[-15])  #print first character
print(str1[14])  # print last character
print(str1[-1]) #print last character



#lists

my_list1=['red',12,112.12]
print(my_list1)


#list indices

color_list=["red " ,"blue" , "green","black"]
print(color_list[0]) #first element
print(color_list[-1])  #last element
print(color_list[-4])  #first element