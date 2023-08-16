class WeightedQU:
    # Weighted quick-union algorithm implementation 
    def __init__(self, n):
        # id[i] is the parent for i-th element
        self.id = [i for i in range(n)]
        # sz[i] is number of elements in tree rooted in element i
        self.sz = [1 for i in range(n)]

    def root(self, i):
        # Search through all parents of element i updating i to its parent until i become the root of the tree
        while i != self.id[i]:
            i = self.id[i]
        return i            

    def is_connected(self, i, j):
        # Are two elements connected = are they have the same root/in the same tree
        return self.root(i) == self.root(j)

    def union(self, i, j):
        # Connect two elements' parents in one tree with the root of the larger tree become pather for root of the smaller 
        p = self.root(i)
        q = self.root(j)
        if i == j: return
        if self.sz[p] >= self.sz[q]:
            self.id[q] = p
            self.sz[p] += self.sz[q]
        else: 
            self.id[p] = q
            self.sz[q] += self.sz[p]

