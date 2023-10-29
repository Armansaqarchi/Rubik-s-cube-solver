import numpy as np
from state import next_state, solved_state
from location import next_location


final_actions = []

def solve(init_state, init_location, method):
    """
    Solves the given Rubik's cube using the selected search algorithm.
 
    Args:
        init_state (numpy.array): Initial state of the Rubik's cube.
        init_location (numpy.array): Initial location of the little cubes.
        method (str): Name of the search algorithm.
 
    Returns:
        list: The sequence of actions needed to solve the Rubik's cube.
    """

    # instructions and hints:
    # 1. use 'solved_state()' to obtain the goal state.
    # 2. use 'next_state()' to obtain the next state when taking an action .
    # 3. use 'next_location()' to obtain the next location of the little cubes when taking an action.
    # 4. you can use 'Set', 'Dictionary', 'OrderedDict', and 'heapq' as efficient data structures.

    if method == 'Random':
        return list(np.random.randint(1, 12+1, 10))
    
    elif method == 'IDS-DFS':
        return IDS_DFS(init_state=init_state)
    
    elif method == 'A*':
        ...

    elif method == 'BiBFS':
        ...
    
    else:
        return []
    



def IDS_DFS(init_state):
    limit = 0
    while(True):
        actions = []
        depth_DFS(state=init_state, d=limit, actions=actions)
        if(len(final_actions) != 0):
            return final_actions
        limit += 1
        

    
def depth_DFS(state, d, actions):
    if np.array_equal(state, solved_state()):
        global final_actions
        final_actions = actions
    elif d == 0:
        return
    else:
        for i in range(1, 13):
            updated_actions = actions.copy()
            updated_actions.append(i)
            new_state = next_state(state, i)
            depth_DFS(new_state, d-1, updated_actions)
    
        


