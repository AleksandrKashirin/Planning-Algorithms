#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# this are the set of possible actions admitted in this problem
action_space = []
action_space.append((-1,0))
action_space.append((0,-1))
action_space.append((1,0))
action_space.append((0,1))


def plot_joint_enviroment(env, x_e, x_p, goal):
    """
    env is the grid enviroment
    x_e is the state of the evader
    x_p is the state of the pursuer
    """
    dims = env.shape    
    current_env = np.copy(env)
    # plot evader
    current_env[x_e] = 0.8 #yellow

    # plot pursuer
    current_env[x_p ] = 0.6 #cyan-ish
    # plot goal
    current_env[goal] = 0.3
    return current_env

def transition_function(env,x,u):
    """Transition function for states in this problem
    x: current state, this is a tuple (i,j)
    u: current action, this is a tuple (i,j)
    env: enviroment
    
    Output:
    new state
    True if correctly propagated
    False if this action can't be executed
    """
    xnew = np.array(x) + np.array(u)
    xnew = tuple(xnew)
    #print('xnew',xnew)
    if state_consistency_check(env,xnew):
        return xnew, True
    return x, False

def state_consistency_check(env,x):
    """Checks wether or not the proposed state is a valid state, i.e. is in colision or our of bounds"""
    # check for collision
    if x[0] < 0 or x[1] < 0 or x[0] >= env.shape[0] or x[1] >= env.shape[1] :
        #print('out of bonds')
        return False
    if env[x] >= 1.0-1e-4:
        #print('Obstacle')
        return False
    return True

def pursuer_policy(x_e, x_p):
    """Returns the pursuer action"""
    ds = np.array(x_e) - np.array(x_p)
    theta = np.arctan2(ds[1], ds[0])
    theta = (theta+np.pi)/np.pi*2
    u_index = np.floor(theta)
    delta = theta - u_index
    #print('tehtas: ', theta, delta)
    if np.random.rand() < delta:
        #print('randomness')
        u_index += 1
    if u_index == 4:
        u_index = 0 # this is due to action 0  equals action 4 in this particular order of th action space
    #print('u index', u_index)    
    return int(u_index)
    
def pursuer_transition(env,x_e, x_p):
    """compact function for the transition function and policy for the pursuer"""
    iters = 1
    if np.random.rand() < 0.002:
        iters = 2
    for i in range(iters):
        u_p = pursuer_policy(x_e, x_p)
        x_p, _ = transition_function(env,x_p,action_space[u_p])
    return x_p
