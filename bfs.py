# Author: Chikwanda Chisha
# Date: 11/11/2022
# Purpose: SA9
from collections import deque
from load_graph import *


def bfs(start, end):
    vertex_dict = load_graph("dartmouth_graph")
    frontier = deque()
    frontier.append(start)
    backpointer_dict = {start: None}
    while len(frontier) != 0:
        curr_v = frontier.popleft()
        if start != None:
            for adj_v in vertex_dict[curr_v].adjacent_list:
                if adj_v.name not in backpointer_dict:
                    frontier.append(adj_v.name)
                    backpointer_dict[adj_v.name] = curr_v
            if end in backpointer_dict:
                break
    vert_path = []
    v = end
    while v is not None and start is not None:
        vert_path.append(vertex_dict[v])
        v = backpointer_dict[v]

    return vert_path

