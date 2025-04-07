#question 1
for i in range(1500,2701):
    if(i%7==0 and i%5==0):
        print(i)

       
 #question 2
temp=float(input("enter temperature"))
unit=input("enter unit").lower()
print(temp) #input takes string
print(unit)
if(unit=='c'):
   temp=( 1.8*temp)+32
#    print("temp in faurhenheit is" , temp)
   print(f'temp in faurhenheit is {temp}F')

elif(unit=='f'):
    temp=((temp-32)/1.8)
    print(f'temp in celcius is{temp}F')


#Question 3
guess = 5
num = int(input('enter a number btw 1 to  9'))

while (num != guess):
    print("wrong!")
    num=int(input('enter a number btw 1 to  9'))
    
print("well guessed")


#Question 4
rows = 6
# Increasing pattern
for i in range(1, rows + 1):
    print("*" * i)
# Decreasing pattern
for i in range(rows - 1, 0, -1):
    print("*" * i)

   

#question 5
word = input("Enter a word: ")
reversed_word = word[::-1]  #[::-1] is used for reversing
print("Reversed word:", reversed_word)

#question 6
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0

for num in numbers:
    if num%2 == 0:
        even_count+=1

    else:
        odd_count+=1


print("number of even numbers :",even_count)
print("number of odd numbers :",odd_count)


#question 7
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]


for item in datalist:
    print(f"{item} is of type {type(item)}")


#question 8
for i in range(0,7):
    if( i == 3 or i == 6):
     continue 
    print(i)
    


#question 9
a=0
b=1
while a < 50:
    print(a, end=' ')
    a, b = b, a + b


for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

#question 10
rows = 3
cols = 4
result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * j)
    result.append(row)

print(result)


#question 11
while True:
    line = input( )
    if line == "":
        break
    print(line.lower())

#question 12
binary_input = input("Enter binary numbers: ")  
binary_list = binary_input.split(',') #.split() Splits a string into a list using a separator (like a comma, space, etc.).

result = []
for b in binary_list:
    if int(b, 2) % 5 == 0:
        result.append(b)   #The append() method is used with lists in Python to add a new element at the end of the list.

print(','.join(result))   #Combines a list of strings into a single string


#question 13
text = input("Enter a string: ")

letters = 0
digits = 0

for ch in text:
    if ch.isalpha():     #isalpha()  returns true if character is a letter
        letters += 1
    elif ch.isdigit():   #isdigit()  returns true if character is a digit
        digits += 1

print("Letters", letters)
print("Digits", digits)


#question 14
import re

def validate_password(password):
  
    if len(password) < 6 or len(password) > 16:
        return "Password must be between 6 and 16 characters long."

    
    if not re.search("[a-z]", password):#The re.search() function in Python is used to search for a pattern (specified as a regular expression) in a string. 
        return "Password must contain at least one lowercase letter."

  
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."

   
    if not re.search("[0-9]", password):
        return "Password must contain at least one digit."

   
    if not re.search("[$#@]", password):
        return "Password must contain at least one special character from [$#@]."

    return "Password is valid."

password = input("Enter your password: ")
print(validate_password(password))


