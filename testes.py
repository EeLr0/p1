import searchAgents
import util

def uniformCostSearch(problem: searchAgents.SearchProblem):
    """Search the node of least total cost first."""
    queue = util.PriorityQueue()
    visited = set()
    queue.push((problem.getStartState(), []), 0)
    while not queue.isEmpty():
        state, action = queue.pop()
        if problem.isGoalState(state):
            return action
        if state not in visited:
            for newState, newAction, _ in problem.getSuccessors(state):
                new = action + [newAction]
                queue.update((newState, new), problem.getCostOfActions(new))
        visited.add(state)
    return []