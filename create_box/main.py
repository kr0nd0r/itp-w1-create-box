"""This is the entry point of the program."""


def create_box(height, width, character):
    
    box = ''
    
    for i in range(height):
        box += (character * width) + '\n'
    return box


if __name__ == '__main__':
    create_box(3, 4, '*')
