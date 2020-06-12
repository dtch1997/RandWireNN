import networkx as nx
import os
from graph import base

class Graph(base.Graph):
    """An Erdos-Renyi graph; each edge exists independently with probability p"""
    def __init__(self, node_num: int, p: float, seed: int = None):
        super(Graph, self).__init__(node_num, seed)
        self.p = p
        
    def make_graph(self):
        return nx.generators.random_graphs.erdos_renyi_graph(self.node_num, self.p, seed)