import random
from environment import Environment
from agent import Agent
import pickle
import matplotlib.pyplot as plt
import pickle
import os 
from qlearning import *


q_agent = Agent(epsilon = 0.7)
print('starting agent training...')
train(q_agent,2000)
print('completed agent training...')
print('saving trained agent...')
with open('agent_state.pkl','wb') as outp:
    pickle.dump(q_agent, outp, pickle.HIGHEST_PROTOCOL)
print('agent saved successfully!')