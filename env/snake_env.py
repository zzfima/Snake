# compilation of main parts of environment
import gym
import numpy as np


class SnakeEnv(gym.Env):
    """Snake Environment that follows gym interface"""

    def __init__(self):
        super(SnakeEnv, self).__init__()
        self._steps_counter = 0
        self._reward_score = 0
        self._metadata = {'render.modes': ['human']}
        self._action_space = ['left', 'right', 'up', 'down']
        self._observation_space = np.zeros([100, 100])

    def step(self, action):
        """
        executing provided action, calculate reward and return resulting observation
        """
        super().step(action)
        # return observation, reward, done, info

    def reset(self):
        """resetting the environment to the initial state

        Returns:
            np: observation
        """
        super().reset()
        # return observation  # reward, done, info can't be included

    def render(self, mode='human'):
        """render the environment state

        Args:
            mode (str, optional): [description]. Defaults to 'human'.
        """
        pass

    def close(self):
        """closing the rendering
        """
        pass
