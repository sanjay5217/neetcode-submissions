class DSU:
    parent: list[int]
    rank: list[int]

    def __init__(self) -> None:
        self.parent, self.rank = [], []

    def make(self, node: int) -> None:
        self.parent.append(node)
        self.rank.append(0)
    
    def find(self, node: int) -> None:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        rep1, rep2 = self.find(node1), self.find(node2)
        if rep1 == rep2:
            return False
        if self.rank[rep1] >= self.rank[rep2]:
            self.parent[rep2] = rep1
            if self.rank[rep1] == self.rank[rep2]:
                self.rank[rep1] += 1
        else:
            self.parent[rep1] = rep2
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint_set = DSU()
        for node in range(len(edges) + 1):
            disjoint_set.make(node)
        
        for node1, node2 in edges:
            if not disjoint_set.union(node1, node2):
                return [node1, node2]








        