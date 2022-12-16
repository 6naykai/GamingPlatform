import sys
import warnings
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from games import *
from core import *

# if __name__ == '__main__':
#     from core import *
# else:
#     from .core import *

class CPGames():
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.supported_games = self.initialize()
    '''执行对应的小程序'''
    def execute(self, game_type=None, config={}):
        assert game_type in self.supported_games, 'unsupport game_type %s...' % game_type
        qt_games = ['tetris', 'gobang']
        if game_type in qt_games:
            print("test")
            pass
            # app1 = QApplication(sys.argv)
            # client = self.supported_games[game_type](**config)
            # client.show()
            # sys.exit(app1.exec_())
        else:
            client = self.supported_games[game_type](**config)
            client.run()
    '''初始化'''
    def initialize(self):
        supported_games = {
            'maze': MazeGame,
            'gobang': GobangGame,
            'tetris': TetrisGame,
            'gemgem': GemGemGame,
            'sokoban': SokobanGame,
            'pingpong': PingpongGame,
            'flappybird': FlappyBirdGame,
            'aircraftwar': AircraftWarGame,
            'greedysnake': GreedySnakeGame,
            'twozerofoureight': TwoZeroFourEightGame,
            #'playwithaiui':PlayWithAIUI,
        }
        return supported_games
    '''获得所有支持的游戏信息'''
    def getallsupported(self):
        all_supports = {}
        for key, value in self.supported_games.items():
            all_supports[value.game_type] = key
        return all_supports
    '''str'''
    def __str__(self):
        return 'Welcome to use Games!'