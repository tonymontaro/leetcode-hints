class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.in_progress = False
        self.visited = False
    def __repr__(self):
        return f'Node: {self.val}, {self.in_progress}'

class Solution:
    """O(n) time and space"""
    def canFinish(self, numCourses: int, prerequisites: "list[list[int]]") -> bool:
        if not prerequisites or not prerequisites[0] or numCourses <= 0:
            return True
        nodes = []
        node_set = {}
        for a, b in prerequisites:
            if a not in node_set: 
                node_set[a] = Node(a)
                nodes.append(node_set[a])
            if b not in node_set:
                node_set[b] = Node(b)
                nodes.append(node_set[b])
            node_set[a].children.append(node_set[b])
        for node in nodes:
            if not node.visited and not self.explore(node):
                return False
        return True

    def explore(self, node):
        if node.in_progress:
            return False
        node.visited = True
        node.in_progress = True
        result = True
        for child in node.children:
            result = result and self.explore(child)
        node.in_progress = False
        return result
