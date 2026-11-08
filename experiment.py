from environment import TaxiWorld, RenderMode


env = TaxiWorld(render_mode=RenderMode.RGB_ARRAY)

state = env.get_state()
print("state:", state)

actions = env.get_possible_actions(state)
print("legal actions:", actions)