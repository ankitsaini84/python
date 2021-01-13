"""
Create a list of airports that includes a series of tuples containing an airport's name and its code.
Loop through the list and utilize tuple assignment. Use one variable to hold the airport name and
another variable to hold the airport code. Display the airport's name and code to the screen
"""
airports = [
    ('IGI Airport', 'DEL'),
    ('Shivaji Airport', 'MUM'),
    ('Bangalore Airport', 'BLR')]

for (name, code) in airports:
    print('The code for \'{}\' is \'{}\'.'.format(name, code))