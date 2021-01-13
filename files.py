"""
1.
Create a program that opens file.txt. Read each line of the file and prepend it with a line
number.
"""
with open('file.txt', 'r') as r_file:
    for line in r_file:
        print(line.rstrip()) # rstrip removes all trailing whitespaces & newlines

"""
2.
Read the contents of animals.txt and produce a file named animals­sorted.txt that is sorted
alphabetically.
"""
animals = []
with open('animals.txt', 'r') as ra_file:
    for animal in ra_file:
        animals.append(animal)

was_file = open('sorted-animals.txt', 'w')
animals.sort()
for animal in animals:
    was_file.write(animal)
was_file.close()