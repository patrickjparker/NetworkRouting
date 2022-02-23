class HeapPriorityQueue:

    def __init__(self, length):
        self.queue = []
        self.map = [ -1 for i in range(length) ]

    def decrease_key(self, nodeID, value):
        index = self.map[nodeID]
        if index == -1:
            index = len(self.queue)
            self.map[nodeID] = index
            self.queue.append(NodeWrapper(nodeID, value))
        else:
            self.queue[index].distance = value
        self.bubbleUp(index)


    def delete_min(self):
        if self.getLength() < 1: return None
        index = self.queue[0].index
        if self.getLength() > 1:
            self.swap(0, len(self.queue) - 1)
        del self.queue[len(self.queue) - 1]
        self.map[index] = -1
        self.bubbleDown(0)
        return index

    def insert(self, nodeID, value):
        self.decrease_key(nodeID, value)

    def getLength(self):
        return len(self.queue)

    def bubbleDown(self, index):
        queue = self.queue
        firstChild = index * 2 + 1
        secondChild = index * 2 + 2
        if firstChild >= len(queue): return
        if secondChild >= len(queue) or queue[firstChild].distance < queue[secondChild].distance:
            lowest = firstChild
        else:
            lowest = secondChild
        if queue[lowest].distance < queue[index].distance:
            self.swap(lowest, index)
            self.bubbleDown(lowest)

    def bubbleUp(self, index):
        if index == 0: return
        parentIndex = (index - 1) // 2
        if self.queue[index].distance < self.queue[parentIndex].distance:
            self.swap(index, parentIndex)
            self.bubbleUp(parentIndex)

    def swap(self, indexA, indexB):
        queue = self.queue
        queue[indexA], queue[indexB] = queue[indexB], queue[indexA]
        self.map[queue[indexA].index], self.map[queue[indexB].index] = self.map[queue[indexB].index], self.map[queue[indexA].index]

    def __str__(self) -> str:
        string = ""
        for nodeWrapper in self.queue:
            string += "{0}\n".format(str(nodeWrapper))
        return string

class NodeWrapper:

    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __str__(self) -> str:
        return "distance: {0}\nindex: {1}\n".format(self.distance, self.index)