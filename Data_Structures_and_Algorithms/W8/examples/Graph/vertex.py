from edge import Edge


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

    def add_edge(self, target_vertex, weight):
        self.edges.append(Edge(target_vertex, weight))

    def remove_edge(self, target_vertex):
        self.edges = [e for e in self.edges if e.target != target_vertex]
        # edges = []
        # for e in self.edges:
        #     if e.target != target_vertex:
        #         edges.append(e)
        # self.edges = edges

    def __str__(self):
        st = ""
        for edge in self.edges:
            st += f"[{self.label}] -> ({edge.weight}) [{edge.target.label}]\n"
        return st
            