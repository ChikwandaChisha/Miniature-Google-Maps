# Author: Chikwanda Chisha
# Date: 11/11/2022
# Purpose: SA9
from cs1lib import *
from bfs import *
from random import randint

WIN_H = 811
WIN_W = 1012
WIDTH_STROKE = 3
start = None
goal = None
start_x, start_y = 0, 0
end_x, end_y = 0, 0
vertex_dict = load_graph("dartmouth_graph")


def draw_vert_and_edges():
    for key in vertex_dict:
        vertex_dict[key].draw_vertices(0, 0, 1)  # draws the vertices
        vertex_dict[key].draw_edges(0, 0, 1)  # draws all the edges connecting the vertices


def mouse_movement(mx, my):
    global end_y, end_x
    end_x = mx
    end_y = my


def mouse_click(mx, my):
    global start_y, start_x
    start_x = mx
    start_y = my


def path():
    global start_y, start_x, end_x, end_y, start, goal
    for key in vertex_dict:
        if vertex_dict[key].in_region(start_x, start_y):
            start = key  # start is a key and not an object
            start_x, start_y = vertex_dict[key].x, vertex_dict[key].y
            set_fill_color(1, 0, 0)
            vertex_dict[start].draw_vertices(1, 0, 0)  # draws/highlights the start vertex
        if vertex_dict[key].in_region(end_x, end_y) and start != key:  # to ensure that the start is not the go
            goal = key  # goal is a key and not an object
            end_x, end_y = vertex_dict[key].x, vertex_dict[key].y


def main():
    map = load_image("dartmouth_map.png")
    draw_image(map, 0, 0)
    draw_vert_and_edges()
    path()
    track_vert()


def track_vert():
    track = bfs(start, goal)  # track contains objects

    for i in range(len(track) - 1):
        set_stroke_color(randint(0, 1), randint(0, 1), randint(0, 1))
        set_stroke_width(WIDTH_STROKE)
        track[i].path_vert()
        draw_line(track[i].x, track[i].y, track[i + 1].x, track[i + 1].y)


start_graphics(main, height=WIN_H, width=WIN_W, mouse_press=mouse_click, mouse_move=mouse_movement)
