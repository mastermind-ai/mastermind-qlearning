from environment import Environment
from agent import Agent
import matplotlib.pyplot as plt
import pickle
from qlearning import *

print("baseline performance:", random_agent_average_performance(50))
q_agent = Agent(epsilon=0.2)
print("worse case length:", worst_case_length(q_agent))
# hyperparameter tuning
for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    q_agent = Agent(epsilon=epsilon)
    train(q_agent, 2000)
    wc_perf = worst_case_length(q_agent)
    avg_perf = avg_num_guesses_needed(q_agent)
    print(f"q-learning with epsilon = {epsilon} worst case performance = {wc_perf}")
    print(f"q-learning with epsilon = {epsilon} average case performance = {avg_perf}")
