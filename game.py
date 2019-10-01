import ai
import copy
import random

class Engine:
    def __init__(self, depth=3):
        self.depth = depth
        self.state = Game()
        self.player = 0

    def nextAction(self):
        if self.state.player == 0:
            return ai.expectimax(self.state, self.depth)
        else:
            return random.choice(self.state.gameActions())

    def get_next(self):
        action = self.nextAction()
        print("action:", action)
        self.state = self.state.result(action)
        return self.state.board

class Game:
    def __init__(self, width=4, height=4):
        self.width, self.height = width, height
        self.board = [[0 for i in range(width)] for j in range(height)]
        self.player = 0

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return not self == other

    def score(self):
        """
        Returns the integer value of a given state. The current implementation
        returns highest number present.
        """
        return max(map(max, self.board))

    def actions(self):
        return self.playerActions() if self.player == 0 else self.gameActions()

    def playerActions(self):
        return [("shift", direction)
                for direction in ["up", "left", "down", "right"]
                if self.result(("shift", direction)) != self]

    def gameActions(self):
        return [("place", (x, y), n)
                for x in range(self.width)
                for y in range(self.height)
                for n in [2, 4]
                if self.board[x][y] == 0]

    def result(self, action):
        self.player = (self.player + 1) % 2
        return self


# def result(state, action):
    # if action is None:
        # return state
    # elif action[0] is "place":
        # x, y = action[1]
        # newstate = copy.deepcopy(state)
        # newstate[x][y] = action[2]
        # return newstate
    # elif action[0] is "shift":
        # return shift(state, action[1])
    # else:
        # raise Exception("Received illegal action: " + str(action))

# def shiftrow(row):
    # return row

# def shift(state, direction):
    # if direction is "up":
        # transpose = list(zip(*state))
        # newtranspose = shift(transpose, "left")
        # return list(zip(*transpose))
    # if direction is "down":
        # transpose = list(zip(*state))
        # newtranspose = shift(transpose, "right")
        # return list(zip(*transpose))
    # if direction is "left":
        # reverse = list(map(list, map(reversed, state)))
        # newreverse = shift(reverse, "right")
        # return list(map(list, map(reversed, state)))
    # if direction is "right":
        # return list(map(shiftrow, state))
