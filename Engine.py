from Landscape import *
from Player import *

class Engine:
    def __init__(self, filename):
        self.__landscape = Landscape('in.txt')
        self.__player = Player(self.__landscape.get_player_pos())
    
    def loop(self):
        print(self.__landscape)
        while not self.__landscape.win():
            self.__player.move(self.__landscape)
            print(self.__landscape)
    
e = Engine('in.txt')

e.loop()