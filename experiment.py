# Gabriele Sanfilippo SM3201617

# this is a debugging file to experiment with
# the state rapresentation and the search algorithm

from .environment import TaxiWorld, RenderMode
from .submission import Agent


env = TaxiWorld(render_mode=RenderMode.RGB_ARRAY)

state = env.get_state()
print("state:", state)

actions = env.get_possible_actions(state)
print("legal actions:", actions)

agent = Agent(env)
print("h(start) =", agent.heuristic(state))