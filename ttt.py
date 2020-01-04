class BoardNode(object):
    """docstring for BoardNode."""

    def __init__(self, cmdboard):
        super(BoardNode, self).__init__()
        self.board = list(cmdboard)
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, or 'd' for draw, else None if this board is not final
        self.children = [] # all nodes that can be reached with a single move

        self.best_move  # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.moves_to_end  # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.final_state   # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)
        self.WINSPACES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def winner(self):
        for x in self.WINSPACES:
            if self.board[x[0]] == self.board[x[1]] == self.board[x[2]]:
                if self.board[x[0]] == "x":
                    return "x wins"
                elif self.board[x[0]] == "o":
                    return "o wins"
        else:
            if "_" in self.board:
                return "unfinished"
            else:
                return "draw"



d = BoardNode("x___x_o_x")

print(d.winner())
