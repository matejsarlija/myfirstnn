import gymnasium as gym

# F = Field
# H = Hole
# G = Goal


env = gym.make("FrozenLake-v1")


def value_iteration(env):
    num_states = env.observation_space.n
    num_actions = env.action_space.n
    print(num_actions)

value_iteration(env)
