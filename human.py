from player import Player

class Human(Player):
    def __init__(self, name) -> None:
        """Initializes the player"""
        super().__init__(name)
    
    def choose_next_move(self, board,letter):
        possible_moves = board.get_possible_moves(letter)
        print("Possible moves are ", possible_moves)
        move = input("Enter your next move in this way : line_number,column_number \n")
        move = tuple(map(int, move.split(',')))
        return move
