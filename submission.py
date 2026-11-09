# Gabriele Sanfilippo SM3201617

from .environment import PASSENGER_WAITING, PASSENGER_IN_TAXI

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
        return ...

    # delivered
    return ...

  def search(self):

    # TODO
    
    self.plan = []
    pass