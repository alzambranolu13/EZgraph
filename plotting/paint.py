import networkx as nx
import matplotlib.pyplot as plt
from graphClasses.DirectedGraph import DirectedGraph
from graphClasses.UndirectedGraph import UndirectedGraph
from graphClasses.DirectedWeightedGraph import DirectedWeightedGraph
from graphClasses.UndirectedWeightedGraph import UndirectedWeightedGraph

def paint_graph(Graph):
    numberOfEdges = Graph.getNumEdges()
    edges_ = Graph.getEdges()
    edges = []
    for edge in edges_:
        edges.append(tuple(edge))

    if type(Graph) == "DirectedGraph" or "DirectedWeightedGraph":
        g = nx.Graph()
        g.add_edges_from(edges)

    elif type(Graph) == "UndirectedGraph" or "UndirectedWeightedGraph":
        g = nx.DiGraph()
        g.add_weighted_edges_from(edges)

    nx.draw_planar(g, with_labels = True)
    
    plt.show()
    