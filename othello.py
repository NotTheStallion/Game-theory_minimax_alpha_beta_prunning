from board import *
from player import *
from minimax import MyPlayer
from human import Human
import random
from termcolor import colored

class Othello:
    def __init__(self, dimensions, player1, player2) -> None:
        """initializes the game with an empty board of size dimensions*dimensions."""
        self.board = Board(dimensions)

        self.dimensions = dimensions

        self.players = [player1, player2]
        self.colors = ['B', 'W']
        self.current_player = self.determine_first_player()

    def determine_first_player(self):
        """The first player is always the one of index 0."""
        return 0

    def get_letter_from_player(self):
        """Returns the color corresponding to the current player. Either returns 'W' of 'B'."""
        return self.colors[self.current_player]

    def is_spot_empty(self, index):
        """determine if space of index index is empty on the board"""
        return self.board.board[index[0]][index[1]] == "."

    def is_game_over(self):
        """Returns True if the game is over, False if not."""
        return len(self.board.get_possible_moves('W')) == 0 and len(self.board.get_possible_moves('B')) == 0

    def change_player(self):
        """Changes current player."""
        self.current_player = abs(self.current_player - 1)

    def get_current_player(self):
        """returns the current player."""
        return self.current_player

    def determine_winner(self, score):
        """returns -1 if its a tie, 0 if B won, 1 if W won"""
        #score = self.get_score()
        if score[0] == score[1]:
            return -1
        elif score[0] > score[1]:
            return 0
        else:
            return 1

    def display_game(self):
        """Displays the game board"""
        print("\t", end='')
        for k in range(self.dimensions):
            print(k, "\t", end='')
        print("\n")
        for i in range(self.dimensions):
            print(i, "\t", end='')
            for j in range(self.dimensions):
                if (self.board.board[i][j] == '.'):
                    print(colored(self.board.board[i][j],
                          "white") + "\t", end='')
                elif (self.board.board[i][j] == 'W'):
                    print(colored(self.board.board[i][j],"magenta" )+ "\t", end='')
                else:
                    print(colored(self.board.board[i][j],"green" )+ "\t", end='')
            print("\n")

    def play(self, verbose=True):
        """Game"""
        if verbose:
            print("The first player is ", self.players[self.current_player].name,
              " and will be playing with B ")

        cheating_detected = 0

        while not self.is_game_over():
            if verbose:
                self.display_game()
            possible_moves =  self.board.get_possible_moves(self.get_letter_from_player())

            if verbose:
                print("It's", colored(self.players[self.current_player].name, "cyan"),
                  "'s turn (", self.colors[self.current_player], ")")
                print(colored("The score is : ", "red"), self.board.get_score())

            if len(possible_moves) > 0:
                # get move
                try:
                    move = self.players[self.current_player].choose_next_move(self.board,self.get_letter_from_player())
                    print(move,"current playing position")
                except Exception as err:
                    cheating_detected = self.current_player + 1
                    if verbose:
                        print("EXCEPTION RAISED BY PLAYER ",
                            colored(self.players[self.current_player].name,"cyan"), "\n")
                        print("Player ", colored(self.players[abs(
                            1 - self.current_player)].name,"cyan"), "won \n")
                    break

                # check that move is in possible moves
                if move not in possible_moves:

                    cheating_detected = self.current_player + 1
                    if verbose:
                        print("WRONG MOVE by ",
                            colored(self.players[self.current_player].name,"cyan"), "\n")
                        print("Player ", colored(self.players[abs(
                            1 - self.current_player)].name,"cyan"), "won \n")
                    break

                # apply move
                self.board.apply_move(move, self.get_letter_from_player())
            else :
                if verbose:
                    print("Aucun coup n'est possible, c'est au joueur opposé de jouer\n")

            # change player
            self.change_player()

        score = self.board.get_score()
        ending = self.determine_winner(score)

        if verbose:
            self.display_game()
        if cheating_detected == 0 and verbose:
            if ending == -1:
                print("It's a tie")
            elif ending == 0:
                print("Player", colored(self.players[0].name,"cyan"),
                      "won, ", score[0], " to ", score[1])
            else:
                print("Player", colored(self.players[1].name,"cyan"),
                      "won, ", score[1], " to ", score[0])
        elif cheating_detected:
            if cheating_detected == 1:
                score = (-500, score[1])
            elif cheating_detected == 2:
                score = (score[0], -500)
        return score





#"""
player1 = MyPlayer("Player1",3)
player2 = MyPlayer("Player2",3)
game = Othello(8, player1, player2)
P1_score,P2_score=game.play(verbose=True)
#"""