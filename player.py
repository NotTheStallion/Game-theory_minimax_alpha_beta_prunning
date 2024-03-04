from board import *
import random
import copy

class Player():
    def __init__(self, name) -> None:
        self.name = name

    def choose_next_move(self, board, letter) -> (int, int):
        pass