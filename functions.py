"""
1.
Create a fill in the blank word game. Prompt the user to enter a noun, verb, and an adjective.
Use those responses to fill in the blanks and display the story.
Write a short story. Remove a noun, verb, and an adjective.
Create a function to get the input from the user.
Create a function that fills in the blanks in the story you created.
Ensure each function contains a docstring.
After the noun, verb, and adjective have been collected from the user, display the story using
their input.
"""
def getNoun():
    return input('Enter a Noun: ')

def getVerb():
    return input('Enter a Verb: ')

def getAdjective():
    return input('Enter an Adjective: ')

def writeStory():
    """ Show empty story to the user """
    print('Story ~ <noun> <verb> <adjective>.')

    """ Take noun, verb & adjective from the user """
    noun = getNoun()
    verb = getVerb()
    adjective = getAdjective()

    """ Show complete story """
    print('Story ~ {} {} {}.'.format(noun, verb, adjective))

writeStory()