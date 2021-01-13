"""
1.
Write a Python program that uses three variables. The variables in your program will be animal,
vegetable, and mineral. Assign a string value to each one of the variables. Your program should
display "Here is an animal, a vegetable, and a mineral." Next, display the value for animal,
followed by vegetable, and finally mineral. Each one of the values should be printed on their
own line. Your program will display four lines in total.
"""
animal = 'cat'
vegetable = 'broccoli'
mineral = 'gold'

print('Here is an animal, a vegetable, and a mineral.')
print(animal)
print(vegetable)
print(mineral)

"""
2. 
Write a Python program that prompts the user for input and simply repeats what the user
entered.
"""

# inp = input('Please type something and press enter: ')
# print('You entered')
# print(inp)


"""
3. 
Write a Python program that prompts for input and displays a cat "saying" what was provided by
the user. Place the input provided by the user inside a speech bubble. Make the speech bubble
expand or contract to fit around the input provided by the user.
"""
say = input('What will cat say?: ')
say_len = len(say)
print('          {}'.format('_'*say_len))
print('        < {} >'.format(say))
print('          {}'.format('-'*say_len))
print('         /')
print(' /\\_/\\  /')
print('( o.o )')
print(' > ^ <')