


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
        return self._list[self._index]


class PrimeGraph:

    def __init__(self):
        # build the graph, maybe make this random next time
        self.nodelist = []
        node_1 = {name: 'node 1', nodes: [2, 3]}
        node_2 = {name: 'node 2', nodes: [5, 6]}
        node_3 = {name: 'node 3', nodes: [6, 7, 8]}
        node_4 = {name: 'node 4', nodes: []}
        node_5 = {name: 'node 5', nodes: []}
        node_6 = {name: 'node 6', nodes: []}
        node_8 = {name: 'node 7', nodes: []}

        prime_list = new PrimeList()

    def _build(self):
        # build list of nodes



def print_graph(root):


def next_prime(prime):
    

def print_node():
    pass

if __name__ == "__main__":
    print "main program"    