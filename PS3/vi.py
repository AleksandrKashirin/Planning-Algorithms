#!/usr/bin/python

import numpy as np
from utils import action_space, transition_function

def vi(env, goal, N=100):
    """
    env is the grid enviroment
    goal is the goal state
    N - limit of iterations
    """
    # Initialize action cost
    action_cost = 1
    # Initialize G graph
    G = np.zeros(env.shape)
    G[:] = np.inf
    G[goal] = 0
    # Initialize counter
    counter = 0
    # Initialize flag of G change
    flag = True
    # While there is a change in G graph
    while flag == True:
        # If the G graph was not changed
        if flag == False:
            # Then break the cycle
            break
        # Increment the counter
        counter += 1
        # If counter reached it is limit
        if counter == N:
            # Then break the cycle
            break
        # Set flag to False
        flag = False
        # Calculate G
        # For each X<Y
        for x_line in env:
            for y in x_line:
                # Check if G[X,Y] != inf
                if G[x_line, y] != np.inf:
                    # Assign the state
                    state = (x_line, y)
                    # For each action
                    for action in action_space:
                        # Calculate new state
                        new_state, is_action = transition_function(env, state, action)
                        # If action is possible
                        if is_action:
                            # Than compare current cost in the cell of new_state 
                            # with the cost of previous step + action cost
                            G[new_state] = min(G[new_state], G[state] + action_cost)
            
    return G


def policy_vi(G):
    """
    G: optimal cot-to-go function

    Заменяем числа в матрице на направление стрелок, ищем наименьшее число и в направлении этого числа ставим стрелку условную
    """
    
    return policy
