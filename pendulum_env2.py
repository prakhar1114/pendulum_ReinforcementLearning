#!/usr/bin/env python

"""RandomWalk environment class for RL-Glue-py.
"""
# this is a variant from origininal class to test which value of discrete torque gives good results

from environment import BaseEnvironment
import numpy as np
import gym
# discrete_torque=0.015

class PendulumEnvironment2(BaseEnvironment):
    def env_init(self, env_info={}):
        """
        Setup for the environment called when the experiment first starts.
        """
        self.discrete_torque = env_info.get("discrete_torque")
        
#         print("discrete_torque",self.discrete_torque)
        
        self.env = gym.make("Pendulum-v0")
        self.env.seed(0)

    def env_start(self):
        """
        The first method called when the experiment starts, called before the
        agent starts.

        Returns:
            The first state observation from the environment.
        """        
        
        reward = 0.0
        _ = self.env.reset() 
        observation = self.env.state
                
#         self.reward_obs_term = (reward, observation, is_terminal)
        self.reward_obs_term = (reward, observation,False)
        
        # return first state observation from the environment
        return self.reward_obs_term[1]
#         return self.reward_obs_term[1]    
        
    def env_step(self, action):
        """A step taken by the environment.

        Args:
            action: The action taken by the agent

        Returns:
            (float, state, Boolean): a tuple of the reward, state observation,
                and boolean indicating if it's terminal.
        """

        last_state = self.reward_obs_term[1]
        
        if action==0:
            action=np.array([-self.discrete_torque])
        elif action==1:
            action=np.array([0])
        else:
            action=np.array([self.discrete_torque])
        
        _, reward, is_terminal, _ = self.env.step(action)
        current_state = self.env.state
        
        self.reward_obs_term = (reward, current_state, False)
        
        return self.reward_obs_term