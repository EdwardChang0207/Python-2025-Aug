'Hi, my name is ____, I am ___ years old.'

'''
kevin 18
alan. 30
mary.  7
'''
# print('Hi, my name is kevin, I am 18 years old.')
# print('Hi, my name is alan, I am 30 years old.')
# print('Hi, my name is mary, I am 7 years old.')

name = ['kevin', 'alan', 'mary']
age = [18, 30, 7]
# print('Hi, my name is ',name[0], 'I am', age[0] ,'years old.')
# print('Hi, my name is ',name[1], 'I am', age[1] ,'years old.')
# print('Hi, my name is ',name[2], 'I am', age[2] ,'years old.')

#format
'''
(1)%
    print('Hi, my name is %5s, I am %3d years old.' % (name[0], age[0]))
    print('Hi, my name is %5s, I am %3d years old.' % (name[1], age[1]))
    print('Hi, my name is %5s, I am %3d years old.' % (name[2], age[2]))
    #格式符號
    %s -> str
    %d -> int
    %f -> float
(2).format()
    input().split() . (1)的 (2)對...做...
    print('Hi, my name is {:5s}, I am {:3d} years old.'.format(name[0], age[0]))
    print('Hi, my name is {:5s}, I am {:3d} years old.'.format(name[1], age[1]))
    print('Hi, my name is {:5s}, I am {:3d} years old.'.format(name[2], age[2]))
(3)f-string
#1+1 = 2
print(f'1+1 = {1+1}')
print(f'Hi, my name is {name[0]:5s}, I am {age[0]:3d} years old.')
print(f'Hi, my name is {name[1]:5s}, I am {age[1]:3d} years old.')
print(f'Hi, my name is {name[2]:5s}, I am {age[2]:3d} years old.')
'''

'3.1415926取到小數點後第二位'
pi = 3.1415926
print('%.3f'%pi)