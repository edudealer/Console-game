from Props import *

class Landscape:
    '''Landscape which represent game field'''

    '''Get coords of player'''
    def get_player_pos(self):
        for y in range(len(self.__fields)):
            for x in range(len(self.__fields[y])):
                if str(self.__fields[y][x]) == Movable.CHARACTER:
                    return (x, y)
        raise Exception('Can\'t find any players!')

    '''Check if ended'''
    def win(self):
        if 'X' not in str(self):
            return True
        return False
    
    '''Get available field to go'''
    def get_available_directions(self, character_pos):
        x0, y0 = character_pos
        if str(self.__fields[y0][x0]) != Movable.CHARACTER:
            raise Exception('Can\'t find character at character_pos!')
        directions = []
        for direction in ('A', 'W', 'D', 'S'):
            x1, y1 = Landscape.destination((x0, y0), direction)
            if str(self.__fields[y1][x1]) in (Immovable.WALL, Movable.CHARACTER):
                continue
            if str(self.__fields[y1][x1]) in (Immovable.SPACE, Immovable.PLACE):
                directions.append(direction)
                continue
            if str(self.__fields[y1][x1]) == Movable.BOX:
                x2, y2 = Landscape.destination((x1, y1), direction)
                if str(self.__fields[y2][x2]) in (Immovable.SPACE, Immovable.PLACE):
                    directions.append(direction)
                    continue
        return directions

    '''Move character at pos in a direction'''
    def move(self, character_pos, direction):
        x0, y0 = character_pos
        x1, y1 = Landscape.destination((x0, y0), direction)
        if str(self.__fields[y0][x0]) != Movable.CHARACTER:
            raise Exception('Can\'t find character at character_pos!')
        if str(self.__fields[y1][x1]) in (Immovable.WALL, Movable.CHARACTER):
            raise Exception('Can\'t move in the ' + direction + ' direction!')
        if str(self.__fields[y1][x1]) in (Immovable.SPACE, Immovable.PLACE):
            self.__fields[y0][x0].move(self.__fields[y1][x1])
            return (x1, y1)
        elif str(self.__fields[y1][x1]) == Movable.BOX:
            x2, y2 = Landscape.destination((x1, y1), direction)
            if str(self.__fields[y2][x2]) in (Immovable.SPACE, Immovable.PLACE):
                self.__fields[y1][x1].move(self.__fields[y2][x2])
                self.__fields[y0][x0].move(self.__fields[y1][x1])
                return (x1, y1)
            else:
                raise Exception('Can\'t move in the ' + direction + ' direction!')
    
    '''Find destination pos within a direction'''
    @staticmethod
    def destination(pos, direction):
        if direction == 'W':
            return (pos[0], pos[1] - 1)
        if direction == 'S':
            return  (pos[0], pos[1] + 1)
        if direction == 'A':
            return (pos[0] - 1, pos[1])
        if direction == 'D':
            return (pos[0] + 1, pos[1])
        raise Exception('Can\'t recognize the direction!')

    '''Load map from filename'''
    def __init__(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        width = len(lines[0]) - 1
        height = len(lines)
        self.__fields = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Field(lines[y][x]))
            self.__fields.append(row)
    
    '''Field to str'''
    def __str__(self):
        s = ''
        for y in range(len(self.__fields)):
            for x  in range(len(self.__fields[y])):
                s = s + str(self.__fields[y][x])
            s = s + '\n'
        return s