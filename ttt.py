import sys
import time
import random

class BoardNode(object):
    """docstring for BoardNode."""

    def __init__(self, cmdboard):
        super(BoardNode, self).__init__()
        self.board = list(cmdboard)
        self.end_state = None # if this is a terminal board, end_state == 'x' or 'o' for wins, or 'd' for draw, else None if this board is not final
        self.children = [] # all nodes that can be reached with a single move

        self.best_move = None  # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.moves_to_end = 0  # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.current_state = None   # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)

        self.depth = 0
        self.recent_move = -1
        self.end_state = self.winner()
        self.score = 0

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


    # def winner(self):
    #     WINSPACES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    #     for x in WINSPACES:
    #         if self.board[x[0]] == self.board[x[1]] == self.board[x[2]]:
    #             if self.board[x[0]] == "x":
    #                 return "x"
    #             elif self.board[x[0]] == "o":
    #                 return "o"
    #     else:
    #         if "_" in self.board:
    #             return None
    #         else:
    #             return "d"


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

    def makechildren(self, depth):
        self.current_state = self.winner()
        currboard = []
        for x in self.board:
            currboard.append(x)
        for n, x in enumerate(currboard):
            if x == "_":
                currboard[n] = self.next_move
                child = BoardNode("".join(currboard))
                child.recent_move = n
                self.children.append(child)
                if depth <= 6:
                    # depth = depth + 1
                    child.makechildren(depth + 1)
                    child.depth = depth
                    # depth = depth - 1
                currboard[n] = "_"


    def showallchildren(self, space):
        if self.depth < 100:
            for x in self.children:
                if self.current_state == None:
                    print(space, x, self.recent_move, self.next_move,  "         depth: ", self.depth)
                    pass
                if self.current_state != None:
                    print(space, x, self.recent_move, self.next_move, "      " , self.current_state, "  won      depth: ", self.depth )
                    # print(space, x, current_state)
                x.showallchildren(space + "    ")


    def getbestmoves(self, move):
        if self.depth == 2:
            if self.end_state == "x" and
        else:
            e = 0;
            for child in self.children:
                child.getbestmoves(self.next_move)



d = BoardNode(sys.argv[2])

start = time.time()

d.makechildren(1)
d.showallchildren("")
# m = d.getbestmoves()

# minimax(2, computer)
end = time.time()

print(end - start)
# for x in d.children[0].current_state:
#     print(x)

# print(d.children[0].current_state)

# d.showallminmax("")

# f = open(sys.argv[1], "w")
# f.write(str(m))
# f.close()
