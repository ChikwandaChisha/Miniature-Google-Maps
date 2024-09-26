from load_graph import load_graph

vertex_dict = load_graph("dartmouth_graph")

out_file = open("vertices.txt", "w")
for vertex in vertex_dict:
    out_file.write(str(vertex_dict[vertex]) + "\n")
out_file.close()