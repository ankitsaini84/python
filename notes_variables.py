# String functions
"""
str(string)         converts number to string
len(string)         returns length of the string
string.format()     formats the string
string.upper()      converts string to uppercase
string.lower()      converts string to lowercase
"""
fruit = 'apple'
print('String {}'.format(fruit))
print('String length: {}'.format(len(fruit)))
print('Uppercase string: {}'.format(fruit.upper()))
print('Lowercase string: {}'.format(fruit.lower()))

# Formatting Strings & Printing Variables
first = 'I'
second = 'love'
third = 'Python'
forth = '3'
print('{} {} {}'.format('I', 'love', 'Python'))
print('{0} {1} {2} & {2} {1}s me.'.format('I', 'love', 'Python'))
print('{} {} {}-{}'.format(first, second, third, forth))

# Formatting width
# {<var. #> : <formatting parameters>}
# < align Left
# > align right
# ^ align center
print('-'*23)   # prints '-', 23 times.
print('| {0:^8} | {1:^8} |'.format('Fruit', 'Quantity'))
print('-'*23)
print('| {0:<8} | {1:>8} |'.format('Apples', 3))
print('| {0:<8} | {1:>8} |'.format('Oranges', 5))
print('-'*23)

# Formatting floating integers
print('-'*23)
print('| {0:^8} | {1:^8} |'.format('Fruit', 'Quantity'))
print('-'*23)
# {<var. #> : <alignment>.<floating point precesion>}
print('| {0:<8} | {1:>8.2f} |'.format('Apples', 3.4444))
print('| {0:<8} | {1:>8.2f} |'.format('Oranges', 5))
print('-'*23)

# Accept user input
name = input('Your name please? : ')
print('Hello {}, you just learned how to format strings & accept user-input, in Python.'.format(name.upper()))

