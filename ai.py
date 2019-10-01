def maxvalue(state, depth):
    if not state.actions() or depth == 0:
        return state.score(), None
    value, bestAction = float("-inf"), None
    for action in state.actions():
        nextState = state.result(action)
        nextValue = expectedvalue(nextState, depth - 1)
        if nextValue > value:
            value, bestAction = nextScore, action
    return value, bestAction

def expectedvalue(state, depth):
    """
    Returns the tuple (score, bestMove).
    """
    if not state.actions() or depth == 0:
        return state.score(), None
    scores = []
    for action in state.actions():
        nextState = state.result(action)
        nextValue = maxvalue(nextState, depth - 1)
        scores.append(nextValue)
    return sum(scores) / float(len(scores)), None

def expectimax(state, depth):
    return maxvalue(state, depth)[1]
