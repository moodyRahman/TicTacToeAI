import sys

class BoardNode(object):
    """docstring for BoardNode."""

    def __init__(self, cmdboard):
        super(BoardNode, self).__init__()
        self.board = list(cmdboard)
        self.end_state = None # if this is a terminal board, end_state == 'x' or 'o' for wins, or 'd' for draw, else None if this board is not final
        self.children = [] # all nodes that can be reached with a single move

        self.best_move = None  # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.moves_to_end = None  # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.final_state = None   # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)

        self.depth = 0
        self.recent_move = -1
        self.end_state = self.winner()

        cx = 0
        co = 0

        for pos in self.board:
            if pos == "x":
                cx += 1
            elif pos == "o":
                co += 1

        if cx == co:
            self.next_move = "x"
        else:
            self.next_move = "o"


    def __repr__(self):
        return "".join(self.board)


    def winner(self):
        WINSPACES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for x in WINSPACES:
            if self.board[x[0]] == self.board[x[1]] == self.board[x[2]]:
                if self.board[x[0]] == "x":
                    return "x"
                elif self.board[x[0]] == "o":
                    return "o"
        else:
            if "_" in self.board:
                return None
            else:
                return "d"

    def makechildren(self, depth = 0):
        self.final_state = self.winner()
        currboard = []
        for x in self.board:
            currboard.append(x)
        for n, x in enumerate(currboard):
            if x == "_":
                currboard[n] = self.next_move
                child = BoardNode("".join(currboard))
                child.recent_move = n
                self.children.append(child)
                if depth <= 5:
                    depth = depth + 1
                    child.makechildren(depth)
                    child.depth = depth
                    depth = depth - 1
                currboard[n] = "_"


    def showallchildren(self, space):
        for x in self.children:
            if self.final_state == None:
                print(space, x, self.recent_move, "         depth: ", self.depth)
            else:
                print(space, x, self.recent_move, "      " , self.final_state, "  won      depth: ", self.depth )
                # print(space, x, final_state)
            x.showallchildren(space + "    ")






d = BoardNode(sys.argv[2])

d.makechildren()

# for x in d.children[0].final_state:
#     print(x)

# print(d.children[0].final_state)

d.showallchildren("")

f = open(sys.argv[1], "w")
f.write(str(d.children[0].recent_move))
f.close()
