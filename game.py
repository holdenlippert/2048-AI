import ai
import copy

class Engine:
    def __init__(self, depth=3):
        self.depth = depth
        self.state = [[0 for i in range(4)] for j in range(4)]

    def get_next(self):
        self.state = result(self.state, nextAction(self.state, self.depth))
        return self.state

def gameover(state):
    return len(playerActions(state)) == 0

def score(state):
    maxvalue = float("-inf")
    for row in state:
        for cell in state:
            maxvalue = max(maxvalue, cell)
    return maxvalue

def playerActions(state):
    actions = []
    for direction in ["up", "down", "left", "right"]:
        action = ("shift", direction)
        newstate = result(state, action)
        if newstate != state:
            actions.append(action)
    return actions

def gameActions(state):
    actions = []
    for x in state:
        for y in state[x]:
            if state[x][y] == 0:
                actions.append(("place", (x, y), 2))
                actions.append(("place", (x, y), 4))
    return actions

def result(state, action):
    if action[0] is "place":
        x, y = action[1]
        newstate = copy.deepcopy(state)
        newstate[x][y] = action[2]
        return newstate
    elif action[1] is "shift":
        return shift(state, direction)
    else:
        raise Exception("Received illegal action: " + action)

def nextAction(state, depth):
    return ai.expectimax(state, gameover, score, playerActions, gameActions, result, depth)

def shiftrow(row):
    return row

def shift(state, direction):
    if direction is "up":
        transpose = zip(*state)
        newtranspose = shift(transpose, "left")
        return zip(*transpose)
    if direction is "down":
        transpose = zip(*state)
        newtranspose = shift(transpose, "right")
        return zip(*transpose)
    if direction is "left":
        reverse = list(map(list, map(reversed, state)))
        newreverse = shift(reverse, "right")
        return list(map(list, map(reversed, state)))
    if direction is "right":
        return list(map(shiftrow, state))
