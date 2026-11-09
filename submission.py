# Gabriele Sanfilippo SM3201617

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

  def search(self):

    # TODO
    
    self.plan = []
    pass