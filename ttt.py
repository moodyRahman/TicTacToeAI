
class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, or 'd' for draw, else None if this board is not final
        self.children = [] # all nodes that can be reached with a single move

        self.best_move  # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.moves_to_end  # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.final_state   # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)
