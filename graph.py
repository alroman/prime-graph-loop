


''' 
    Toy program to demonstrate how one can find loops in a graph structure
    using properties of prime numbers.  
'''

class PrimeList:
    ''' 
        Class to generate an array of primes from a text list 
    '''

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

    # dequeue the list
    def get(self):
        self._index+=1
        return self._list[self._index]


# @todo: need a better graph structure (with OO nice stuff)
class PrimeGraph:
    '''
        Simple graph data structure.  This is simply a list with a 
        list of nodes that are connected to it.
    '''
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
            BFS traversal

            start at the root node, then explore as far as possible
            on each branch before back tracking
        '''
        # call recursive method
        GraphTraverser._bfs(graph, 0, 1)

    @staticmethod
    def _bfs(graph, node, accum):
        
        # Check if we have a loop.  This is true whenever the id 
        # of the node (which is a prime number) divides without remainder
        if accum % graph[node]['id'] == 0:
            print "found duplicate"
            return

        # Save prime
        accum *= graph[node]['id']

        # Keep going down the tree
        if len(graph[node]['n']):
            for n in graph[node]['n']:
                GraphTraverser._bfs(graph, n, accum)
        else:
            print "leaf: " + graph[node]['name']


if __name__ == "__main__":

    # Generate prime graph
    p = PrimeGraph()

    # Do BFS traversal
    GraphTraverser.bfs(p.nodelist)