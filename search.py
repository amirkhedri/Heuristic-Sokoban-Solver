from collections import deque
import heapq
from env.sokoban import PUSH_COST, MOVE_COST

# -------------------------------------------------------------------
# 1. BFS – Breadth‑First Search (shortest action sequence)
# -------------------------------------------------------------------
def bfs_solve(game):
    start_state = game.get_initial_state()
    if game.is_goal(start_state):
        return []

    frontier = deque()
    frontier.append((start_state, []))
    visited = {start_state}

    while frontier:
        state, actions = frontier.popleft()
        for action, next_state, _ in game.get_successors(state):
            if next_state in visited:
                continue
            if game.is_goal(next_state):
                return actions + [action]
            visited.add(next_state)
            frontier.append((next_state, actions + [action]))
    return None

