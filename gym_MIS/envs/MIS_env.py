import gym
import numpy as np

# sample graph
# optimal solution is {0, 2, 3}
N = 4
SAMPLE_GRAPH = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
])

class MISEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    def __init__(self):
        # not implemented!
        # self.action_space = N
        # self.observation_space = []
        # self.reward_range = []
        self.reset()

    def reset(self):
        self.A = SAMPLE_GRAPH
        self.ans = []
        self.reward = 0  # number of vertices already counted in the solution
        return self.A

    def step(self, action):  # action: index of a vertex
        self.ans.append(action)
        # delete neighbors
        remain = self.A[action] == 0
        # delete itself
        remain[action] = False
        self.A = self.A[remain][:, remain]
        self.reward += 1
        assert self.A.shape[0] == 0 or self.A.shape[0] == self.A.shape[1]
        return self.A, self.reward, self.A.shape[0] == 0, {}

    def render(self, mode='human', close=False):
        print(self.A)

    def seed(self, seed=None):
        pass