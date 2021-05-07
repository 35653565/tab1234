
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
elif menu_selection == '2':
    radius = int(input('Insert radius (leave SI units):'))
    A = math.pi * radius**2
    b = A/ radius
    print(b)
elif menu_selection == '3':
    for i in range(10,50,-1):
         print(i)



