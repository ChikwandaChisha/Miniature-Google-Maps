# Author: Chikwanda Chisha
# Date: 11/11/2022
# Purpose: SA9
from cs1lib import *
from random import randint


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adjacent_list = []
        self.r = randint(0, 1)
        self.g = randint(0, 1)
        self.b = randint(0, 1)

        self.stroke_width = 3
        self.radius = 10

    def draw_vertices(self, r, g, b):
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, self.radius)

    def path_vert(self):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x, self.y, self.radius)

    def draw_edges(self, r, g, b):
        set_stroke_color(r, g, b)
        set_stroke_width(self.stroke_width)
        for vert in self.adjacent_list:
            draw_line(self.x, self.y, vert.x, vert.y)

    def in_region(self, x, y):
        check = False
        if abs(self.x - x) <= 10 and abs(self.y - y) <= 10:
            print(x, y)
            check = True
        return check

    def __str__(self):
        vertices = ""
        for vertex in self.adjacent_list:
            if vertex is not self.adjacent_list[len(self.adjacent_list) - 1]:
                vertices += (str(vertex.name) + ", ")
            else:
                vertices += str(vertex.name)

        return f'{self.name}; Location: {self.x},{self.y}; Adjacent vertices: {vertices}'
