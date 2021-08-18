# exercise 97: statistics
'''
statistics('story.txt')
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
import re

def statistics(file):
    with open(file) as f:
        lines = len(f.readlines())
    with open(file) as f:
        words = len(re.split(' |\n',f.read()))
    with open(file) as f:
        characters = len([a for a in f.read()])
    return {'lines': lines, 'words': words, 'characters': characters}


# Solution
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }

# exercise 98: find_and_replace
'''
find_and_replace('story.txt', 'Alice', 'Colt')
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file_name, word, new_word):
    with open(file_name) as f:
        text = f.read()
    with open(file_name, 'w') as f:
        new_text = text.replace(word, new_word)
        f.write(new_text)

# Solution
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate() # Have to truncate becase new text is less characters than before.
