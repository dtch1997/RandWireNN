import networkx as nx
import os
from graph import base

class Graph(base.Graph):
    """A Watts-Strogatz small-world graph"""
    def __init__(self, node_num: int, k: int, p: float, seed: int = None):
        super(Graph, self).__init__(node_num, seed)
        self.p = p
        self.k = k
        
    def make_graph(self):
        # Daniel: Is there some reason why we need a connected WS graph? 
        # This seems slightly different from the implementation in the paper.
        return nx.generators.random_graphs.connected_watts_strogatz_graph(self.node_num, self.k, self.p, seed=self.seed)