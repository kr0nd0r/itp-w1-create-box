"""This is the entry point of the program."""


def create_box(height, width, character):
    
    box = ''
    
    for i in range(height):
        box += (character * width) + '\n'
    return box


if __name__ == '__main__':
    create_box(12, 14, '*')
"""
#Dustin's Solution using nested for loops

def create_box(height, width, character):
    string =''
    for i in range(height):
        for x in range(width):
            string += str(character)
        string += '\n'
    return string
    
"""