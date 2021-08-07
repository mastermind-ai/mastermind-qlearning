import random
from environment import Environment
from agent import Agent
import pickle
import matplotlib.pyplot as plt
import pickle
import os 

def random_agent_performance(secret="1234"):
    """return num of guesses needed to get secret for an random agent"""
    random_agent = Agent()
    random_agent.reset_possible_states()
    guess = random_agent.get_best_action()
    env = Environment(secret)
    num_guess = 1
    while guess != secret:
        random_agent.possible_states.remove(guess)
        guess = random_agent.get_best_action()
        num_guess += 1
    return num_guess


def random_agent_average_performance(num):
    l = []
    for _ in range(num):
        secret = Environment._number_from_index(random.randint(0, 6 ** 4 - 1))
        length = random_agent_performance(secret)
        l.append(length)
    return sum(l) / len(l)


def train(agent, n_episodes):
    """
    Train the agent for n_episodes.
    """
    for _ in range(n_episodes):
        secret = Environment._number_from_index(random.randint(0, 6 ** 4 - 1))
        env = Environment(secret)
        agent.reset_possible_states()
        action = agent.random_action()  # init action

        if action == secret:  # if init guess is crt skip this episode
            continue

        run = True
        while run:
            feedback = env.get_feedback(action)
            reward = env.reward(action)
            agent.learn_from_move(action, feedback, reward)

            if action == secret:
                break  # correct guess stop episode
            else:
                action = agent.random_action()  # else next guess


def num_guesses(agent, secret="1234"):
    """return number of guesses needed by the agent to
    get to the secret"""
    guess_list = []
    state_list = []

    agent.reset_possible_states()
    guess = agent.get_best_action()
    
    env = Environment(secret)
    num_guess = 1
    while guess != secret:
        feedback = env.score(secret, guess)
        guess_list.append(guess)
        state_list.append(feedback)
        agent.restrict_possible_states(guess, feedback)
        guess = agent.get_best_action()
        num_guess += 1
    return num_guess, guess_list, state_list


def avg_num_guesses_needed(agent):
    """average number guesses needed for all the possible secret codes"""

    nums = []

    for idx in range(6 ** 4):
        secret = Environment._number_from_index(idx)
        length,_,_ = num_guesses(agent, secret)
        nums.append(length)

    #     print(nums)
    return sum(nums) / len(nums)


def worst_case_length(agent):
    """num of guesses needed in worst case"""

    nums = []

    for idx in range(6 ** 4):
        secret = Environment._number_from_index(idx)
        length,_,_ = num_guesses(agent, secret)
        nums.append(length)

    #     print(nums)
    return max(nums)

def guess(agent):
    secret = Environment._number_from_index(idx)

def format_state_list(state_list):
    formatted_state_list = []
    
    for each_state in state_list:
        new_state_list =[]
        blacks = each_state[0]
        whites = each_state[1]
        default = 4 - (blacks+whites)
        for i in range(blacks):
            new_state_list.append("black")
        for i in range(whites):
            new_state_list.append("white")
        for i in range(default):
            new_state_list.append("default")
            
        formatted_state_list.append(new_state_list)
    return formatted_state_list

def start(code):
    if os.path.isfile('./agent_state.pkl'):
        print('loading from pickle')
        with open('agent_state.pkl','rb') as inp:
            q_agent = pickle.load(inp)
    else:
        return 
    secret = code
    _, guess_list, state_list = num_guesses(q_agent,secret)
    guess_list = [list(x) for x in guess_list]
    state_list = format_state_list(state_list)

    return guess_list, state_list 






