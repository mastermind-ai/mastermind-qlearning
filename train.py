from environment import Environment
from agent import Agent
import pickle
from qlearning import *
import sys

choice_of_epsilon = float(sys.argv[1])
q_agent = Agent(epsilon = choice_of_epsilon)
print('starting agent training...')
train(q_agent,2000)
print('completed agent training...')
print('saving trained agent...')
with open('agent_state.pkl','wb') as outp:
    pickle.dump(q_agent, outp, pickle.HIGHEST_PROTOCOL)
print('agent saved successfully!')