import gym

from stable_baselines.gail import generate_expert_traj
from keyboard import KeyboardController, KeyLogger
from agent import HumanAgent


class Generate():
    def __init__(self):
        self.env = gym.make("CartPole-v1")
        self.human_agent = HumanAgent()

    def train(self):
g       enerate_expert_traj(human_agent.train(), 'dummy_expert_cartpole', env, n_episodes=10)