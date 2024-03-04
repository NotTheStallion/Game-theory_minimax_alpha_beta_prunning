class Board():
    def __init__(self, dimensions) -> None:
        self.board = [["." for i in range(dimensions)]
                      for i in range(dimensions)]

        mid = int(dimensions/2)
        mid_1 = int(dimensions/2 - 1)
        self.board[mid_1][mid_1] = "W"
        self.board[mid][mid] = "W"
        self.board[mid][mid_1] = "B"
        self.board[mid_1][mid] = "B"
        self.dimensions = dimensions

    def get_possible_moves(self, letter):
        """Returns the list of possible moves by current player"""
        possible_moves = []  # list of tuples of possible moves
        possible_starts = self.get_indexes_of(letter)
        directions = [(1, 1), (1, 0), (1, -1), (0, -1),
                      (-1, -1), (-1, 0), (-1, 1), (0, 1)]

        for start in possible_starts:
            for dire in directions:
                new_pos = self.advance_direction(
                    dire[0], dire[1], letter, start)
                if new_pos != start and self.board[new_pos[0]][new_pos[1]] == '.':
                    possible_moves.append(new_pos)

        return list(dict.fromkeys(possible_moves))

    def advance_direction(self, i, j, letter, start):
        posi = start[0]+i
        posj = start[1]+j
        if self.is_index_in_board_limits(posi, posj) and self.board[posi][posj] != "." and self.board[posi][posj] != letter:
            while self.is_index_in_board_limits(posi, posj) and self.board[posi][posj] != letter and self.board[posi][posj] != ".":
                posi += i
                posj += j
            if (not self.is_index_in_board_limits(posi, posj)):
                return start
            else:
                return (posi, posj)
        else:
            return start

    def is_index_in_board_limits(self, posi, posj):
        """determine if [posi,posj] is within board limits. Returns True if so ; False otherwise."""
        return posi >= 0 and posj >= 0 and posi < self.dimensions and posj < self.dimensions

    def get_indexes_of(self, letter):
        """Returns a list of the positions of letter in the board."""
        indexes = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == letter:
                    indexes.append((i, j))
        return indexes

    def apply_move(self, move, letter):
        """Changes the board according to the new move."""
        # move =  coordinates of new pawn
        directions = [(1, 1), (1, 0), (1, -1), (0, -1),
                      (-1, -1), (-1, 0), (-1, 1), (0, 1)]

        pawns_in_direction = []

        for dire in directions:
            new_pos = self.advance_direction(
                dire[0], dire[1], letter, move)
            if new_pos != move and self.board[new_pos[0]][new_pos[1]] != '.':
                pawns_in_direction.append(dire)

        for pawn in pawns_in_direction:
            start = list(move)
            iteration = 0
            # si vide à l'itération 0 ?
            while self.board[start[0]][start[1]] != letter or iteration == 0:
                self.board[start[0]][start[1]] = letter
                start[0] = start[0] + pawn[0]
                start[1] = start[1] + pawn[1]
                iteration += 1

    def get_score(self):
        """Returns the score : (score_player0, score_player1)"""
        count_W = 0
        count_B = 0

        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if self.board[i][j] == 'B':
                    count_B += 1
                elif self.board[i][j] == 'W':
                    count_W += 1

        return (count_B, count_W)
