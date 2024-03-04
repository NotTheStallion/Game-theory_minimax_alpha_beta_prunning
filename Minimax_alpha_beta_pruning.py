from player import Player
import copy



class MyPlayer(Player):
    def __init__(self, name):
        self.alpha = -1000000000
        self.beta = 1000000000
        print(name)
        super().__init__(name)

    def choose_next_move(self, board, letter) -> (int, int):
        best_move=(-1,-1)
        best_score= -1000000000
        possible_moves = board.get_possible_moves(letter)

        for move in possible_moves:
            new_board=copy.deepcopy(board) #copy board to simulate a play
            new_board.apply_move(move, letter) #apply the move
            score=self.minimax(new_board, letter,2, -1000000000, 1000000000) #get the best move for a depth of 2

            if score>=best_score: #choosing move and score if the score is the highest we get the best move
                best_score=score
                best_move=move

        return best_move

    def minimax(self, board, letter,depth,alpha,beta):
        if depth==0:
            return len(board.get_indexes_of("B"))-len(board.get_indexes_of("W"))
            
        if letter=="B":
            best_score= -1000000000

            for move in board.get_possible_moves(letter):
                new_board=copy.deepcopy(board)
                new_board.apply_move(move, letter)
                score=self.minimax(new_board,"W",depth-1,alpha,beta)
                best_score=max(best_score, score)
                alpha = max(alpha, best_score)
                
                if alpha>=beta:
                    break

            return best_score

        else:
            best_score = 1000000000

            for move in board.get_possible_moves(letter):
                new_board=copy.deepcopy(board)
                new_board.apply_move(move, letter)
                score=self.minimax(new_board,"B",depth - 1, alpha, beta)
                best_score=min(best_score, score)
                beta = min(beta, best_score)

                if alpha>=beta:
                    break

            return best_score




