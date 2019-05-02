import numpy as np

import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from keyboard import KeyboardController, KeyLogger
from mouse import MouseController, MouseLogger

class Imitation(gym.Env):

    def __init__(self):
        self.env = None
        self.viewer = None
        self.info = None
        self.reward = None
        self.done = False
        self.state = None
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space
        self.steps_beyond_done = None
        self.seed()
        self.configure()

    def __del__(self):
        pass

    def configure(self, display=None):
        self.display = display

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        self.state = self.env.generate_number()
        #self.env.display()
        action = None
        self.next_state = None
        self.next_state, self.reward, self.done, info = self.env.step(action)
        
        if self.done:
            pass
        return self.next_state, self.reward, self.done, info

    def reset(self):
        self.state = None
        self.done = False
        return self.state, self.done

    def is_game_over(self):
        pass
        return

    def render(self, mode="human", close=False):

        pass

        return 

