import numpy as np

import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
#from keyboard import KeyboardController, KeyLogger
#from mouse import MouseController, MouseLogger
from utilities import DataGrabber
import cv2
import mss

class Imitation(gym.Env):

    def __init__(self):
        self.env = None
        self.viewer = None
        self.info = None
        self.reward = None
        self.done = False
        self.state = None
        self.action_space = None
        self.observation_space = None
        self.steps_beyond_done = None
        self.seed()
        self.configure()
        self.data_grabber = DataGrabber()


    def __del__(self):
        pass

    def configure(self, display=None):
        self.display = display

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        self.action = action
        self.state = self.data_grabber.get_screen_array(0, 0, 800, 640)
        self.render()
        self.data_grabber.get_screen_array(0 ,0 , 800, 640)
        self.next_state = self.state
        self.reward = self.get_reward()
        self.done = self.get_done()
        return self.next_state, self.reward, self.done
        
        if self.done:
            pass
        return self.next_state, self.reward, self.done, self.info

    def reset(self):
        self.state = self.data_grabber.get_screen_array(0, 0, 800, 640)
        #self.render()
        return self.state

    def is_game_over(self):
        pass
        return

    def render(self, mode="human", close=False):
        cv2.imshow("OpenCV/Numpy normal", self.state)
        #cv2.imshow('image',img)
        #sleep(0.1)
        cv2.waitKey(25)
        return 

    def get_reward(self):
        return None

    def get_done(self):
        return None

test = Imitation()
test.reset()
for i in range(100):
    test.step(None)