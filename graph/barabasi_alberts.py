import networkx as nx
import os
from graph import base

class Graph(base.Graph):
    """A Barabasi-Alberts scale-free graph"""
    def __init__(self, node_num: int, m: int, seed: int = None):
        super(Graph, self).__init__(node_num, seed)
        self.m = m
        
    def make_graph(self):
        return nx.generators.random_graphs.barabasi_alberts_graph(self.node_num, self.m, self.seed)