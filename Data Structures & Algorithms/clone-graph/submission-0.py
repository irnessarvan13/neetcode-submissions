"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:                              # empty graph
            return None

        oldToNew = {}                             # original node → its copy

        def dfs(node):
            if node in oldToNew:                  # already copied? (this also stops cycles)
                return oldToNew[node]             # hand back the copy we already made

            copy = Node(node.val)                 # brand new node, same value, no neighbors yet
            oldToNew[node] = copy                 # save it BEFORE visiting neighbors

            for nei in node.neighbors:            # for each original neighbor...
                copy.neighbors.append(dfs(nei))   # ...attach that neighbor's COPY

            return copy

        return dfs(node)