myString = "hello world"
print(myString)

length = len(myString)
print(length)

first_char = myString[0]
print(first_char)

Fname = "Dan"
Lname = "Christie"

print("Hello {} {}, welcome to Python!".format(Fname, Lname))

string_variable = "Hello, World!"
print(string_variable)

multiline_string_variable = """This is a
multiline string."""
print(multiline_string_variable)

substring = string_variable[7:12]
print(substring)

length_of_string = len(string_variable)
print(length_of_string)

stripped_string = string_variable.strip()
print(stripped_string)

uppercase_string = string_variable.upper()
print(uppercase_string)

phrase_check = "Hello" in string_variable
print(phrase_check)
character_check = "z" not in string_variable
print(character_check)

concatenated_string = string_variable + " How are you?"
print(concatenated_string)

escaped_string = "This is an escape character: \nNewline and here's a tab: \tTab"
print("Escaped String:")
print(escaped_string)







# Assign an integer to a variable.
X = 10
# Assign a string to a variable.
UserName = "Abdullah"
# Assign a float to a variable.
Pi = 3.1415
# Use the print() function to print out the variable you assigned.
print("This is a float" , Pi , "This is a String" , UserName , "This is a int" , X)
# Use each of these operators:
print(X + 10)#  + 
print(X * X)#) *
print(X / Pi)# /
X = 20# =
print( X % 4 )# %
Y = 12
# Use each of these logical operators:
# and
if X > 10 and Y > 10:
    print("Both X and Y Conditions Met")
# or
if X > 10 or Y < 10:
    print("One of the Conditions has been Met")

# not
if not X == 10:
    print("X is Not 10")
# Use each conditional statement:
# if
# elif
# else

Temprature = 25

if Temprature > 30:
    print("The Tempraure is Too high ; Turn on AC")
elif Temprature < 20:
    print("The Tempraure is Too low ; Turn off AC")
else:
    print ("The Temprature is ideal")

Temprature = 30
# Use a while loop.
# Use a for loop.
while Temprature > 20:
    Temprature = Temprature - 1
    print(Temprature)
    print("The Temprature is not yet Ideal")
print("The Temprature is now ideal")

for i in range(10):
    Temprature =Temprature + i
    print(Temprature, "degrees")



# Identity operator example
x = [1, 2, 3]
y = x  # y references the same object as x

result = x is y
print(result)  # Output: True because x and y refer to the same object


# Membership operator example
my_list = [1, 2, 3, 4, 5]

result1 = 3 in my_list
result2 = 6 in my_list

print(result1)  # Output: True because 3 is in my_list
print(result2)  # Output: False because 6 is not in my_list


# Bitwise operator example (AND)
a = 5  # Binary: 0101
b = 9  # Binary: 0011

result = a & b  # Bitwise AND: 0001 (Decimal: 1)
print(result)








# Create a list and iterate through that list using a for loop to print each item out on a new line.
nums = [4,2,2,23,2,3,2,31,1,]

for numbers in nums:
    print(numbers)

# Define a function that returns a string variable.

nums.append(2)
print(nums)

nums2 = ['hello','there',2]
nums3 = nums + nums2
print(nums3)
def MyName(Name):
    Answer = ("Hello my Name is " + Name)
    return Answer

print(MyName("Abdullah"))
print(MyName("Zeeshan"))
# Call the function you defined above and print the result to the shell.

print(nums3.reverse())
print(nums3)

# Create a tuple and iterate through it using a for loop to print each item out on a new line.
numst = (4,2,2,23,2,3,2,31,1,)

for numbers in numst:
    print(numbers)
# Tuples operate and behave the same as lists but tuples can not be edited after creation

result = numst.count(2)
print(result)

my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
other_set = {3, 4, 5}
result_set = my_set.difference(other_set)
print(result_set)


my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
name = my_dict.get('name')
my_dict['age'] = 31
my_dict['country'] = 'USA'
nested_dict = {'person1': {'name': 'Alice', 'age': 25},'person2': {'name': 'BOB', 'age': 25}}
print(nested_dict["person1"])

colors = ['red', 'blue', 'green', 'yellow', 'purple']

print(type(4))


if X > 10 and Y > 10:
    print("Both X and Y Conditions Met")
# or
if X > 10 or Y < 10:
    print("One of the Conditions has been Met")

# not
if not X == 10:
    print("X is Not 10")
# Use each conditional statement:
# if
# elif
# else



import datetime

current_date = datetime.date.today()
print(current_date)


import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)

print("Random number:", random_number)




X = 10
Y = 5

if X > Y:
    print("X is greater than Y")
    
    if X == 10:
        print("X is also equal to 10")
    else:
        print("X is not equal to 10")

else:
    print("X is not greater than Y")


# Define a variable
x = 42

# Check if x is even using a condition in an if statement
if x % 2 == 0:
    print("x is even")

if bool(x):
    print("x is truthy")
else:
    print("x is falsy")

if isinstance(x, int):
    print("x is an integer")
else:
    print("x is not an integer")

x = 1
while True:
    x += 1
    if x > 7:
        break
    else:
        print('x is not 7')
        print(x)


# Execute a for loop
for i in range(1, 6):
    print(f"Iteration {i}")

    # Use the break statement within a for loop
    if i == 5:
        print("Breaking the loop at iteration 3")
        break

    # Use the continue statement within a for loop
    if i == 2:
        print("Skipping iteration 2")
        continue
    else:
        print('hello there')

for i in range(len(colors)):
    print(colors[i])

mySentence = "loves the color"
color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name):
    lst  = []
    for color in color_list:
        answer = ("{0} {1} {2}".format(name, mySentence, color))
        lst.append(answer)
    return lst

lst = color_function('adam')
for i in lst:
    print(i)

def get_name():
    go = True
    while go:
        name = input('Please input your name:  ')
        if name == '':
            print('You need to provide a name')
        elif name == 'bob':
            print('bob is not authorized')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


def Say_My_Name():
    print('Heisenberg')

Say_My_Name()
nums.sort()
for i in nums:
    print(i)
print(nums.count(2))