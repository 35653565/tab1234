num = []
for i in range(1,100):
    num.append(i)
module_num = filter(lambda n: n % 2 == 1, num)

for item in module_num:
    print(item)


from functools import reduce

total = reduce(lambda bb, n: bb + n, num)
print(total)

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

class web:
    name = 'Lawson'
    password = 35653565
    location = 'Miami, FL'
    sign_up_date = '03/03/25'
    def __init__(self, password):
        self.password = [] + self.password
    def safeWord(self):
        a = int(input('insert password:'))
        if a == self.password:
            print('Welcome Old Friend')
    def logout(self):
        b = input('Type LEAVE if you want to exit')
        if b == 'Leave':
            print('Goodbye')
try:
    name = web.name
    password = web.password
except ValueError:
    print('Incorrect Passwpord. Try Again')
except TypeError:
    print('Username Not Found. Try Again')
else:
    print('Welcome')
finally:
    print('Thanks For Using Program')

e = web('Ashton')
b = web('Lawson')
c = web('Adam')


