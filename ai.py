def maxvalue(state, gameover, score, agentActions, gameActions, result, depth):
    if gameover(state) or depth == 0:
        return score(state), None
    value, bestAction = float("-inf"), None
    for action in agentActions(state):
        nextState = result(state, action)
        nextValue = expectedvalue(nextState, depth - 1)
        if nextValue > value:
            value, bestAction = nextScore, action
    return value, bestAction

def expectedvalue(state, gameover, score, agentActions, gameActions, result, depth):
    """
    Returns the tuple (score, bestMove).
    """
    if depth == 0:
        return score(state), None
    scores = []
    for action in gameActions(state):
        nextState = result(state, action)
        nextValue = maxvalue(nextState, depth - 1)
        scores.append(nextValue)
    return sum(scores) / float(len(scores)), None

def expectimax(state, gameover, score, actions, result, depth):
    return maxvalue(state, depth)[1]
