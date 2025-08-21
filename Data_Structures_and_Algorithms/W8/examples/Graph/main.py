from graph import Graph


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B", 1)
g.add_edge("B", "C", 2)
g.add_edge("C", "D", 3)
g.add_edge("A", "D", 4)
g.add_edge("D", "A", 4)

print(g)

print("BFS from A:")
g.bfs("A")
print("-"*60)
print("DFS from A:")
g.dfs("A")
print("-"*60)
print("DFS Post Order from A:")
g.dfs_post_order("A")

print("-"*60)
print("BFS from C:")
g.bfs("C")
print("-"*60)
print("DFS from C:")
g.dfs("C")
print("-"*60)
print("DFS Post Order from C:")
g.dfs_post_order("C")
