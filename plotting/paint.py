import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QDir, QUrl
from graphClasses.DirectedGraph import DirectedGraph
from graphClasses.UndirectedGraph import UndirectedGraph
from graphClasses.DirectedWeightedGraph import DirectedWeightedGraph
from graphClasses.UndirectedWeightedGraph import UndirectedWeightedGraph

from os import environ


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


def render(app):
    app.setStyle('Breeze')
    app.setApplicationDisplayName("Grafo")
    path = QDir.current().filePath('nx.html')
    html = QUrl.fromLocalFile(path)
    view = QWebEngineView()
    width = 520
    heigth = 520
    view.setFixedWidth(width)
    view.setFixedHeight(heigth)
    view.load(html)
    view.show()

    app.exec()
    view.close()


def paint_graph(Graph):
    numberOfEdges = Graph.getNodes()
    edges_ = Graph.getEdges()
    edges = []
    for edge in edges_:
        edges.append(tuple(edge))

    if type(Graph) == DirectedGraph or DirectedWeightedGraph:
        g = nx.DiGraph()
        net = Network("500px", "500px", directed=True)
        if type(Graph) == DirectedWeightedGraph:
            # g.add_weighted_edges_from(edges)

            for n in range(0, numberOfEdges):
                net.add_node(n, label="{}".format(str(n)))
            for edge in edges:
                title = "{}".format(str(edge[2]))
                net.add_edge(edge[0], edge[1], title=title)
        else:

            # g.add_edges_from(edges)
            for n in range(0, numberOfEdges):
                net.add_node(n, label="{}".format(str(n)))
            for edge in edges:
                net.add_edge(edge[0], edge[1])


    elif type(Graph) == UndirectedGraph or UndirectedWeightedGraph:
        g = nx.Graph()
        net = Network("500px", "500px")
        if type(Graph) == UndirectedWeightedGraph:
            # g.add_weighted_edges_from(edges)
            for n in range(0, numberOfEdges):
                net.add_node(n, label="{}".format(str(n)))
            for edge in edges:
                title = "{}".format(str(edge[2]))
                net.add_edge(edge[0], edge[1], title=title)
        else:
            for n in range(0, numberOfEdges):
                net.add_node(n, label="{}".format(str(n)))
            # g.add_edges_from(edges)
            for edge in edges:
                net.add_edge(edge[0], edge[1])

    # net.from_nx(g,default_node_size=16, default_edge_weight=5)
    net.save_graph('nx.html')

    suppress_qt_warnings()
    sys.argv.append("--disable-web-security")
    app = QApplication(sys.argv)
    render(app)

    nx.draw_planar(g, with_labels=True)

    # view.close()
