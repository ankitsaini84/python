"""
1.
Create a Python program that captures and displays a person's to­do list. Continually prompt
the user for another item until they enter a blank item. After all the items are entered, display the
to­do list back to the user.
"""
toDoList = []
while True:
    task = input('Enter task: ')
    if task == '':
        break
    toDoList.append(task)

print('Your To-Do List')
print('-'*15)
for task in toDoList:
    print(task)
