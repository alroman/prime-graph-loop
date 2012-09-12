


''' 
    General graph structure 

    This is the simple graph structure that we'll iterate

    node_1 -> node_2 -> ... -> node_n
    node_2 -> node_x -> ... -> node_y
    ...

    node_1 = [2, 3]
    node_2 = [3, 6, 7]
    node_3 is a leaf
    node_4 = []

'''

class PrimeList:

    def __init__(self):
        # some init stuff
        self._list = []
        self._index = 0
        self._build()

    def _build(self):
        f = open('prime_list.txt', 'r')
        for line in f:
            self._list.append(int(line))
        f.close()

    def get(self):
        self._index+=1
        return self._list[self._index]


# @todo: need a better graph structure
class PrimeGraph:

    def __init__(self):
        # build the graph, 
        # @todo: maybe make this random next time
        self.nodelist = [
            {'n': [1, 2]},
            {'n': [3, 4]},
            {'n': [5, 6, 7]},
            {'n': [0]},     # loop
            {'n': []},
            {'n': []},
            {'n': []},
            {'n': []}
        ]

        self._prime_list = PrimeList()
        self._build()

    def _build(self):
        # build list of nodes
        for i, node in enumerate(self.nodelist):
            node['id'] = self._prime_list.get()
            node['name'] = 'node-' + str(i)

        # print self.nodelist

class GraphTraverser:

    @staticmethod
    def bfs(graph):
        '''
            BFS
            start at the root node, then explore as far as possible
            on each branch before back tracking
        '''
        # call recursive method
        GraphTraverser._bfs(graph, 0, 1)

    @staticmethod
    def _bfs(graph, node, accum):
        
        if accum % graph[node]['id'] == 0:
            print "found duplicate"
            return

        # Save prime
        accum *= graph[node]['id']

        # Keep going down the nodes
        if len(graph[node]['n']):
            for n in graph[node]['n']:
                GraphTraverser._bfs(graph, n, accum)
        else:
            print "leaf: " + graph[node]['name']


if __name__ == "__main__":
    print "main program"

    # Generate prime graph
    p = PrimeGraph()
    
    # Do BFS traversal
    GraphTraverser.bfs(p.nodelist)