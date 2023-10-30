import numpy as np
from state import next_state, solved_state
from location import next_location, solved_location




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
        return IDS_DFS(init_state)
    
    elif method == 'A*':
        return Astar(init_state, init_location)

    elif method == 'BiBFS':
        ...
    
    else:
        return []
    



def IDS_DFS(init_state):
    final_actions = []
    def depth_DFS(state, d):
        if np.array_equal(state, solved_state()):
            return True
        elif d == 0:
            return False
        else:
            for i in range(1, 13):
                new_state = next_state(state, i)
                if depth_DFS(new_state, d-1):
                    final_actions.append(i)
                    return True
        return False
    limit = 1
    while(True):
        if depth_DFS(state=init_state, d=limit):
            final_actions.reverse()  
            return final_actions
        limit += 1
        

def Astar(state, init_location):
    from queue import PriorityQueue
    q = PriorityQueue()
    count = 0
    visited = {}
    visited[str(state)] = True
    q.put([heuristic(init_location), count, state, init_location, []])
    while not q.empty():
        current = q.get()
        current_state = current[2]
        visited[str(current_state)] = True
        current_loc = current[3]
        if np.array_equal(current_state, solved_state()):
            return current[4]
        for i in range(1, 13):
            next = next_state(current_state, i)
            if str(next) in visited:
                continue
            next_loc = next_location(current_loc, i)
            g = 1+len(current[4])
            h = heuristic(next_loc)
            count += 1
            q.put([g+h, count, next, next_loc, (current[4] + [i])])
        
        


    
def heuristic(location):
    dict = {1 : [0, 0, 0], 2 : [0, 0, 1], 3 : [0, 1, 0], 4 : [0, 1, 1], 5: [1, 0, 0], 6: [1, 0, 1], 7: [1, 1, 0], 8: [1, 1, 1]}
    manhattan = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                manhattan+= np.sum(np.fabs(dict[location[i][j][k]] - np.array([i, j, k])))
    return manhattan / 4







    
        


