from Landscape import Landscape

class Player:
    def __init__(self, coords):
        self.__x, self.__y = coords
    
    def move(self, landscape):
        directions = landscape.get_available_directions((self.__x, self.__y))
        print('Input a direction (\'W\', \'A\', \'S\', \'D\'): ', end = '')
        direction = input()
        while direction not in directions:
            print('Input a direction (\'W\', \'A\', \'S\', \'D\'): ', end = '')
            direction = input()
        self.__x, self.__y = landscape.move((self.__x, self.__y), direction)