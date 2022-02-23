#!/usr/bin/python3


from CS312Graph import *
from ArrayPriorityQueue import *
from HeapPriorityQueue import *
import time


class NetworkRoutingSolver:
    def __init__( self):
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0
        node = self.network.nodes[destIndex]
        while node is not self.network.nodes[self.source]:
            # Grab the edge the leads from the current node to the previous node
            edge, *wrong = [ edge for edge in self.prev[node.node_id].neighbors if edge.dest is node ]
            path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
            total_length += edge.length
            node = edge.src
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        nodes = self.network.getNodes()
        # Create array setting everything equal to the unvisited values
        self.dist = [ -1 for i in nodes ]
        self.prev = [ None for i in nodes ]
        if use_heap:
            pq = HeapPriorityQueue(len(nodes))
        else:
            pq = ArrayPriorityQueue(len(nodes))
        self.dist[srcIndex] = 0
        pq.decrease_key(srcIndex, 0)
        while pq.getLength() > 0:
            nodeIndex = pq.delete_min()
            # Search through all edges for any node that hasn't been visited or
            # or whose distance can be shortened through this node
            for edge in nodes[nodeIndex].neighbors:
                dest_id = edge.dest.node_id
                new_distance = self.dist[nodeIndex] + edge.length
                if self.dist[dest_id] == -1 or self.dist[dest_id] > new_distance:
                    self.dist[dest_id] = new_distance
                    self.prev[dest_id] = nodes[nodeIndex]
                    pq.decrease_key(dest_id, new_distance)
        t2 = time.time()
        return (t2-t1)
