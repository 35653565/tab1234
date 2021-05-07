import yahoo_fin as yf

"""
****************************************************************
City Academy
ICS4U Midterm Exam
2021-05-05   9:30-12:00


Instructor:  Adam McKillop

Duration: 2.5 Hours

Name:

Score:   / 101
*****************************************************************


Section 1   [/20 KTCA]

1. Using pseudocode (plain language), generate the following algorithms:

    
    a. Greatest Common Factor of two integers, a and b [/5]
    step 1: let a,b be the two numbers 
    step 2: a mod b = R
    step 3 let a = b and b = R
    step 4: repeat 2 and 3 until mod b is greater than 0
    step 5: GCD = b
    b. Factorial of some number, n [/3]
    Step 1: Declare N and F as integer variable.
    Step 2: Initialize F=1.
    Step 2: Enter the value of N.
    Step 3: Check whether N>0, if not then F=1.
    Step 4: If yes then, F=F*N.
    Step 5: Decrease the value of N by 1 .
    Step 6: Repeat step 4 and 5 until N=0
    
    c. Fibonacci sequence with n terms [/3]
    Step 1: Take integer variable A, B, C
    Step 2: Set A = 0, B = 0
    Step 3: DISPLAY A, B
    Step 4: C = A + B
    Step 5: DISPLAY C
    Step 6: Set A = B, B = C
    Step 7: REPEAT from 4 - 6, for n times
2.  What is recursion in the context of computer science? [/3]
    Recursion is when a function calls itself within a function by employing the use of the Software Stack (like a stack of plates) in the Operating System

3.  Describe what the following functions do [/6] and supply some code demonstrating their use [/6]

    a. map() Applies the same function each time in an iterable, storing the result. It often replaces a for loop. 
        e.x., num = [2,3,4,6]
              add_num = map(lambda n:n + n, num)
              #mapp runs all num through the lambda and returns a new list with the addition call add_num  
    b. reduce() reduce uses a function recursively, building each member of the iterable on top of the previous member. 
                runs recursively 2000 times (limit by python), each time adding a number on top
        e.x., 
num = []
for i in range(1,100):
    num.append(i)
from functools import reduce
total = reduce(lambda bb, n: bb + n, num)
print(total)        
    c. filter() applies validation criteria to a iterable -- checks if each of a sequence is true or not. Can be used in list, tuples, or simply any iterartor. Returns an iterator that is already filtered
        e.x., e.x., 
num = []
for i in range(1,100):
    num.append(i)
module_num = filter(lambda n: n % 2 == 1, num)
for item in module_num:
    print(item)
**********************************************************************

Section 2 [/20]

Correct the following code, it is full of bugs

"""
somelist = ['some' 'item','next item','iterable','are','iterables']

somelist.append('well yeah')

for item in somelist:
    print(list(map(lambda word: word.upper(), item)))

message = '{0} and {1} followed by {1} and {1} are {2}'

for j in range(4):
    print(message.format(somelist[j],somelist[j+1],somelist[j+2]))

controls = {'K_UP':'up',
    'K_DOWN':'down',
    'K_LEFT':'left',
    'K_RIGHT':'right'}


direction = 'up'
if direction == controls['K_UP']:
    print(controls['K_LEFT'])

#prints values and keys of controls
print(list(controls.keys()))
print(list(controls.values()))

import time
for i in range(40,100):
    print(('{0:^20} {1:^20} {2:^^30}').format(i,i+1,i+2))
    time.sleep(6/(2*i))
"""
*****************************************************************************

Part 2: Lab Exam

/15
1.  Create a Class definition for a user that accesses a website,  this data object will be eventually passed into
    a database.  When the object is created, the user will input the attributes, use today's date for sign up date

    The user has the following attributes:
        Name
        Password
        Location
        Sign up Date
    The user has the following methods:
        Update -- the user can change their password and location
        Login -- User is prompted for the password, if the password is correct the user gets a welcome message
        Logout -- User gets a goodbye message

    Create 3 user objects.  Be sure to prevent errors or handle them as they occur.
    import datetime

# user class implementation
class User:
    # initialise user
    def __init__(self, name, password, location):
        self.name = name
        self.password = password
        self.location = location
        self.signupdate = datetime.datetime.now().date()

    # the user can change their password and location  
    def update(self, password, location):
        self.password = password
        self.location = location

    # login method for user
    def login(self, password):
        # if the password is correct the user gets a welcome message
        if password == self.password:
            print("Welcome, You have logged in successfully!!")
        else:
            print("Incorrect Password!!")

    # User gets a goodbye message     
    def logout(self):
        print("Good bye!!")


# main function to test user class
def main():
    # create User 
    user = User("Ashton", "35653565", "Miami, Fl")

    # login for the user 
    user.login("304079")  # Incorrect Password
    user.login("35653565")  # correct Password

    # change Password and location
    user.update("3132", "Canada")

    # login again
    user.login("3132")

    # logout 
    user.logout()


if __name__ == '__main__':
    main()

/5
2.  Sort this list of strings alphabetically without using the mt_list.sort() method. 
    Use the following list to demonstrate your solution:
"""
mt_list = ['charlie','tango','foxtrot','x-ray', 'oscar'
               'golf','zulu','uniform','echo','victor','sierra']

for i in range(0,len(mt_list)):
    for j in range(0, len(mt_list)):
        if mt_list[j] > mt_list[j]:
            temp = mt_list[i]
            mt_list[i] = mt_list[j]
            mt_list[j] = temp
print(mt_list)


"""
/33
3.  A user selects from a menu with the following options:
    1. Collect 16 integers and display those that are even [5]
    2. Calculate the area of a circle given a user specified radius, divided by the same radius [5]
    3. Print a count from 10 to 50, then 49 to 10. Every decrement waits .05 seconds [5]
    4. Exit the program [2]

    Create this menu [5] and call a function to perform each selection [2].  Each function returns an
    output from within a print() call [3]. If the user enters anything other than the given options,
    the program will prompt the user a friendly reminder only 1,2,3 and 4 are valid and start over [5].
    Employ error handling strategies (try, except, else, finally) to handle traceback errors[5]

import math

mt_list = ['charlie','tango','foxtrot','x-ray', 'oscar'
               'golf','zulu','uniform','echo','victor','sierra']

for i in range(0,len(mt_list)):
    for j in range(0, len(mt_list)):
        if mt_list[j] > mt_list[j]:
            temp = mt_list[i]
            mt_list[i] = mt_list[j]
            mt_list[j] = temp
print(mt_list)


print('1. Collect 16 integers and display those that are even')
print('2. Calculate the area of a circle given a user specified radius, divided by the same radius')
print('3. Print a count from 10 to 50, then 49 to 10. Every decrement waits .05 seconds')
print('4. Exit the program')
menu_selection = input()
if menu_selection == '1':
    num1 = int(input('enter first number:'))
    num2 = int(input('enter second number:'))
    num3 = int(input('enter third number:'))
    num4 = int(input('enter fourth number:'))
    num5 = int(input('enter first number:'))
    num6 = int(input('enter first number:'))
    num7 = int(input('enter first number:'))
    num8 = int(input('enter first number:'))
    num9 = int(input('enter first number:'))
    num10 = int(input('enter first number:'))
    num11 = int(input('enter first number:'))
    num12 = int(input('enter first number:'))
    num13 = int(input('enter first number:'))
    num14 = int(input('enter first number:'))
    num15 = int(input('enter first number:'))
    num16 = int(input('enter first number:'))
    for num in num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, num16:
        if num % 2 == 0:
            print(num)
    if menu_selection == '2':
        radius = int(input('Insert radius (leave SI units):'))
        A = math.pi * radius**2
        b = A/ radius
        print(b)
    if menu_selection == '3': # think i could use recursion but panicked with time limit (and still ran out of time)
        count1 = range(10,51)
        count2 = range(10,50)
        count3 = range(10,49)
        count4 = range(10,48)
        count5 = range(10,47)
        count6 = range(10,46)
        count7 = range(10, 45)
        count8 = range(10, 44)
        count9 = range(10, 43)
        count10 = range(10,42)
        count11 = range(10,41)
        count12 = range(10,40)
        count13 = range(10,39)
        count14 = range(10,38)
        count15 = range(10,37)
        count16 = range(10,36)
        count17 = range(10,35)
        count18 = range(10,34)
        count19 = range(10,33)
        count20 = range(10,31)
        count21 = range(10,30)
        count22 = range(10,29)
        count23 = range(10,28)
        count24 = range(10,27)

    if menu_selection == '4':
        print('Goodbye')
    if menu_selection != range(1,4):
        raise ValueError
    try:
        value = menu_selection
    except ValueError:
        print('Menu option does not exist')
    else:
        print(menu_selection)
    finally:
        print('Thanks for using the program')



