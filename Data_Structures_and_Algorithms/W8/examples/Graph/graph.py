from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, label):
        # any -> boolean
        # OR operation
        # If any of the conditions inside ANY true -> true
        # If all conditions inside ANY false -> false
        # flag = False
        # for v in self.verticies:
        #     if v.label == label:
        #         flag = True
        #         break
        # if not flag:
        #     self.vertices.append(Vertex(label))
        if not any(v.label == label for v in self.vertices):
            self.vertices.append(Vertex(label))

    def find_vertex(self, label):
        for v in self.vertices:
            if v.label == label:
                return v
        return None

    def add_edge(self, src, dest, weight):
        src_v = self.find_vertex(src)
        dest_v = self.find_vertex(dest)
        if src_v and dest_v:
            src_v.add_edge(dest_v, weight)

    def remove_edge(self, src, dest):
        src_v = self.find_vertex(src)
        dest_v = self.find_vertex(dest)
        if src_v and dest_v:
            src_v.remove_edge(dest_v)

    def remove_vertex(self, label):
        vertex = self.find_vertex(label)
        if vertex:
            self.vertices = [v for v in self.vertices if v.label != label]
            for v in self.vertices:
                v.remove_edge(vertex)

    def __str__(self):
        st = ""
        for v in self.vertices:
            st += str(v) + "\n"
        return st

    def bfs(self, start_label):
        start_vertex = self.find_vertex(start_label)
        if not start_vertex:
            return
        visited = set()
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex.label not in visited:
                print(vertex.label)
                visited.add(vertex.label)
                for edge in vertex.edges:
                    if edge.target.label not in visited:
                        queue.append(edge.target)

    def dfs(self, start_label):
        start_vertex = self.find_vertex(start_label)
        if not start_vertex:
            return
        visited = set()
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            if vertex.label not in visited:
                print(vertex.label)
                visited.add(vertex.label)
                for edge in reversed(vertex.edges):
                    if edge.target.label not in visited:
                        stack.append(edge.target)

    def dfs_post_order(self, start_label):
        start_vertex = self.find_vertex(start_label)
        if not start_vertex:
            return
        visited = set()
        output = []
        stack = [(start_vertex, False)]
        visited.add(start_vertex.label)
        while stack:
            vertex, to_print = stack.pop()
            if to_print:
                output.append(vertex.label)
            else:
                # Mark to print after children
                stack.append((vertex, True))
                # Push unvisited neighbors
                for edge in reversed(vertex.edges):
                    if edge.target.label not in visited:
                        visited.add(edge.target.label)
                        stack.append((edge.target, False))
        for label in output:
            print(label)
