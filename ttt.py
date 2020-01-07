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


    def showallminmax(self, space):
        if self.depth < 100:
            for x in self.children:
                if self.current_state == None:
                    print(space, x, self.recent_move, self.next_move, "      score: ", self.score)
                    pass
                if self.current_state != None:
                    print(space, x, self.recent_move, self.next_move, "      score: ", self.score)
                    # print(space, x, current_state)
                x.showallminmax(space + "    ")

    # def calcminimax(self):
    #     if self.current_state == self.next_move:
    #         self.score = 1
    #     elif self.current_state == "d":
    #         self.score = 0
    #     elif self.current_state == None:
    #         self.score = 0
    #     elif self.current_state != self.next_move:
    #         self.score = -1
    #     for x in self.children:
    #         x.calcminimax()
    #

    def getbestmoves(self):
        for mymove in self.children:
            if mymove.current_state == self.next_move:
                return mymove.recent_move

            for oppmove in mymove.children:
                if (mymove.current_state == "x" and oppmove.current_state == "o") or (mymove.current_state == "o" and oppmove.current_state == "x"):
                    return oppmove.recent_move

                countwinmoves = 0
                for mynextmove in oppmove.children:
                    if mynextmove.current_state == self.next_move:
                        countwinmoves += 1
                if countwinmoves >= 2:
                    return mymove.recent_move

                # countoppwinmoves = 0
                # for mynextmove in oppmove.children:
                #     if (mynextmove.current_state == "x" and oppmove.current_state == "o") or (mynextmove.current_state == "o" and oppmove.current_state == "x"):
                #         countoppwinmoves += 1
                # if countoppwinmoves >= 2:
                #     return oppmove.recent_move
        # def mostwins(self):
        #     winningkids = []
        #     for mymove in self.children:
        #         out = 0
        #         if mymove.current_state == self.next_move:
        #             out+=


        return random.randint(0, len(self.children))

    def minimax(self, depth, player):
        if self.current_state != None or depth == 0:
            return calc_score
        if player == "me":
            bestscore = -9999999
            for child in self.children:
                score = minimax(depth - 1, "them")
                if score > -9999999:
                    bestscore = score
                return bestscore
        else:
            bestscore = 9999999
            for child in self.children:
                score = minimax(depth - 1, "me")
                if score < bestscore:
                    bestscore = score
                return bestscore


# def minimax(depth, player)
#   if gameover || depth == 0
#     return calculated_score
#   end
#   children = all legal moves for player
#   if player is AI (maximizing player)
#     best_score = -infinity
#     for each child
#       score = minimax(depth - 1, opponent)
#       if (score > best_score)
#         best_score = score
#       end
#       return best_score
#     end
#   else #player is minimizing player
#     best_score = +infinity
#     for each child
#       score = minimax(depth - 1, player)
#       if (score < best_score)
#         best_score = score
#       end
#       return best_score
#     end
#   end
# end

#then you would call it like





d = BoardNode(sys.argv[2])

start = time.time()

d.makechildren(1)
# d.calcminimax()
# d.getbestmoves()

minimax(2, computer)
end = time.time()

print(end - start)
# for x in d.children[0].current_state:
#     print(x)

# print(d.children[0].current_state)

# d.showallminmax("")

f = open(sys.argv[1], "w")
f.write(str(d.children[random.randint(0, len(d.children) - 1)].recent_move))
# f.write(str(d.getbestmoves()))
f.close()
