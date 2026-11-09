# Gabriele Sanfilippo SM3201617

from .environment import PASSENGER_WAITING, PASSENGER_IN_TAXI
from itertools import count
import heapq

class Agent():

  def __init__(self, env): #! Not changed
    self.env = env # this is an instance of TaxiWorld
    self.plan = []
    self.search()

  def act(self): #! Not changed
    """Core function called from the runner in order to take an action."""
    # It is assumed that self.search has been already called
    if self.plan:
      return self.plan.pop(0)
    return 0 # Fallback

  def heuristic(self, state):
    x, y, status, p_loc, d_loc = state

    px, py = self.env.stations[p_loc]["pos"] # passenger station
    dx, dy = self.env.stations[d_loc]["pos"] # destination station

    if status == PASSENGER_WAITING:
        to_passenger = abs(x - px) + abs(y - py)
        to_destination = abs(px - dx) + abs(py - dy)
        # + distance passenger -> destination, + dropoff
        return to_passenger + 1 + to_destination + 1   # +1 pickup, +1 dropoff

    if status == PASSENGER_IN_TAXI:
        # distance taxi -> destination, + dropoff
        return abs(x - dx) + abs(y - dy) + 1


    # delivered
    return abs(x - dx) + abs(y - dy)

  def search(self):
    # Using A* search
    env = self.env
    start = env.get_state()

    tie = count()
    frontier = [(self.heuristic(start), next(tie), 0, start)]
    best_g = {start: 0} # cheapest known cost to reach each state
    parent = {start: None} # state -> (previous state, action taken)
    closed = set() # states already expanded


    while frontier:
      f, _, g, state = heapq.heappop(frontier)

      if state in closed:
          continue
      closed.add(state)

      if env.is_goal(state):
        actions = []
        while parent[state] is not None:
          state, action = parent[state]
          actions.append(action)
        actions.reverse()    # collected from goal to start, so reverse
        self.plan = actions
        return

      for action in env.get_possible_actions(state):
        nxt = env.get_successor(state, action)
        if nxt in closed:
          continue

        new_g = g + env.get_action_cost(state, action)

        if new_g < best_g.get(nxt, float("inf")):
          best_g[nxt] = new_g
          parent[nxt] = (state, action)
          heapq.heappush(
            frontier,
            (new_g + self.heuristic(nxt), next(tie), new_g, nxt),
          )

    self.plan = []  # no solution found
