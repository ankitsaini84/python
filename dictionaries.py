"""
Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and their interesting fact to the screen. Next, change a fact about one of
the people. Also add an additional person and corresponding fact. Display the new list of people
and facts. Run the program multiple times and notice if the order changes.
"""
people = {
    'Ankit' : 'Makes nice tea.',
    'Meenu' : 'Asks Ankit to make tea.'
}

for person in people:
    print('{}: {}'.format(person, people[person]))

people['Meenu'] = 'Studies Python.'
people['Reeta'] = 'Likes to celebrate her birthday.'

for person in people:
    print('{}: {}'.format(person, people[person]))
