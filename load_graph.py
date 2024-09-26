# Author: Chikwanda Chisha
# Date: 11/11/2022
# Purpose: SA9
from vertex import Vertex


def load_graph(filename):
    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for line in file:
        section_split = line.split(";")
        vertex_name = section_split[0].strip()
        coordinates = section_split[2].strip().split(",")
        x_coordinate = coordinates[0]
        y_coordinate = coordinates[1]

        vertex_obj = Vertex(vertex_name, x_coordinate, y_coordinate)
        vertex_dict[vertex_name] = vertex_obj

    file.close()

    file = open(filename, "r")

    for line in file:
        section_split = line.split(";")
        adjacent_vertices = section_split[1].strip().split(",")
        adjacent = []
        for a in adjacent_vertices:
            adjacent.append(a.strip())
        line_split = line.split(";")
        vert_name = line_split[0].strip()
        for vertex in adjacent:
            vertex_dict[vert_name].adjacent_list.append(vertex_dict[vertex])
            # print(vertex_dict[vert_name].adjacent_list)
    file.close()
    return vertex_dict


d = load_graph("dartmouth_graph")

