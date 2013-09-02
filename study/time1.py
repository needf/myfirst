# about randrange
from random import randrange
num  = input('How many dice? ')
sides =input('How many sides per die ?')
sum = 0
for i in range(num): sum += randrange(sides) + 1
print 'The result is ', sum
