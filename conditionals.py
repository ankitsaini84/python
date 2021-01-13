"""
1.
Create a program that asks the user how far they want to travel. If they want to travel less than
three miles tell them to walk. If they want to travel more than three miles, but less than three
hundred miles, tell them to drive. If they want to travel three hundred miles or more tell them to
fly.
"""
distance = input('How far you want to travel (in miles)?: ')
distance = int(distance)
if distance < 3:
    print('Walk')
elif distance < 300:
    print('Drive')
else:
    print('Fly')