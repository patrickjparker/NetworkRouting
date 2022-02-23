import random
import math

from which_pyqt import PYQT_VER

if PYQT_VER == 'PYQT5':
	from PyQt5.QtWidgets import *
	from PyQt5.QtGui import *
	from PyQt5.QtCore import *
elif PYQT_VER == 'PYQT4':
	from PyQt4.QtGui import *
	from PyQt4.QtCore import *
elif PYQT_VER == 'PYQT6':
	from PyQt6.QtWidgets import *
	from PyQt6.QtGui import *
	from PyQt6.QtCore import *
else:
	raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))

from CS312Graph import *
from NetworkRoutingSolver import *

NUM_OF_TRIALS = 5
SIZES = [ 100, 1000, 10000, 100000 ]
LAST_SIZE = 1000000

def generateGraph(size):
    SEED = 23
    RANGE = 100
    random.seed( SEED * size )
    ptlist = []
    xr = RANGE
    yr = RANGE
    npoints = size
    while len(ptlist) < npoints:
        x = random.uniform(0.0,1.0)
        y = random.uniform(0.0,1.0)
        xval = xr*x
        yval = yr*y
        ptlist.append( QPointF(xval,yval) )
    OUT_DEGREE = 3
    edgeList = {}
    for u in range(size):
        edgeList[u] = []
        pt_u = ptlist[u]
        chosen = []
        for i in range(OUT_DEGREE):
            v = random.randint(0,size-1)
            while v in chosen or v == u:
                v = random.randint(0,size-1)
            chosen.append(v)
            pt_v = ptlist[v]
            uv_len = math.sqrt( (pt_v.x()-pt_u.x())**2 + \
                                (pt_v.y()-pt_u.y())**2 )
            edgeList[u].append( (v,100.0*uv_len) )
        edgeList[u] = sorted(edgeList[u], key=lambda n:n[0])
    return CS312Graph(ptlist, edgeList)

def getComputTime(size, use_heap):
    network = generateGraph(size)
    solver = NetworkRoutingSolver()
    solver.initializeNetwork(network)
    return solver.computeShortestPaths(0, use_heap)

def getAverageComputTime(size, use_heap):
    totalTime = 0
    for i in range(NUM_OF_TRIALS):
        totalTime += getComputTime(size, use_heap)
    return totalTime / NUM_OF_TRIALS

def main():
    for size in SIZES:
        heapTime = "{:.6f}".format(getAverageComputTime(size, True))
        arrayTime = "{:.6f}".format(getAverageComputTime(size, False))
        print("{0}: (array) {1}  -  (heap) {2}".format(size, arrayTime, heapTime))
    heapTime = "{:.6f}".format(getAverageComputTime(LAST_SIZE, True))
    print("{0}: (heap) {1}".format(LAST_SIZE, heapTime))


if __name__ == '__main__':
    main()