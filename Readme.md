# Pendulum
The following code solves the problem of balancing a pendulum vertically upwards. It makes use of OpenAi gym's pendulum environment. It specifies a reinforcement learning agent which learns information from the environment to balance the pendulum upright. It considers two cases:
1. Pendulum with discrete actions
2. Pendulum with continuous actions

## Pendulum with discrete actions
In this case, the agent learns the reward maximising action as a function of state. The reward maximising actions are discrete actions, for example, -1, 0 and 1 Nm torque.
Run all the cells of 'pendulum_discrete_actions.ipynb'. The results of running this script is present in 'pendulum_discrete_action_sweep.html'.

## Pendulum with continuous actions
In this case, the agent learns the mean and variance of the normal distribution from which action is drawn as a function of state.

It was found that the performance was better for the case of pendulum with continuous actions which was clear as the avergae number of actions taken to train the agent was less than 2000 which was not in the case of discrete actions. This was also expected.
Run all the cells of 'pendulum_continuous.ipynb'. The results of running this script is present in 'pendulum_continuous.html'.

The agent made use of tile coding for state approximation.

