# Done

class Immovable:
    '''Type of object that holds immovable items'''

    SPACE = '.'
    PLACE = 'X'
    WALL = '#'

    def __init__(self, symbol):
        if symbol in (Immovable.SPACE, Immovable.PLACE, Immovable.WALL):
            self.__symbol = symbol
        elif symbol in (Movable.BOX, Movable.CHARACTER):
            self.__symbol = '.'
        else:
            raise Exception('Can\'t recognize the symbol!')

    def __str__(self):
        return self.__symbol

class Movable:
    '''Type of object that holds movable items'''

    BOX = 'B'
    CHARACTER = '@'
    EMPTY = ' '

    def __init__(self, symbol):
        if symbol in (Immovable.SPACE, Immovable.PLACE, Immovable.WALL):
            self.__symbol = Movable.EMPTY
        elif symbol in (Movable.BOX, Movable.CHARACTER):
            self.__symbol = symbol
        else:
            raise Exception('Can\'t recognize the symbol!')
    
    def __str__(self):
        return self.__symbol
    
class Field:
    '''Object of landscape'''

    def __init__(self, symbol):
        self.__immovable = Immovable(symbol)
        self.__movable = Movable(symbol)
    
    def __str__(self):
        if str(self.__movable) in (Movable.BOX, Movable.CHARACTER):
            return str(self.__movable)
        else:
            return str(self.__immovable)

    def move(self, to):
        to.__movable = self.__movable
        self.__movable = Movable.EMPTY