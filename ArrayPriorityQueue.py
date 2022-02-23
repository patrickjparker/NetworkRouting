class ArrayPriorityQueue:

    def __init__(self, nodes):
        self.queue = [ -1 for i in range(nodes) ]
        self.length = 0

    def decrease_key(self, nodeIndex, distance):
        self.insert(nodeIndex, distance)

    def delete_min(self):
        lowest = None
        for index in range(len(self.queue)):
            if self.queue[index] >= 0 and (lowest == None or self.queue[index] < self.queue[lowest]):
                lowest = index
        if lowest != None:
            self.queue[lowest] = -2
            self.length -= 1
        return lowest

    def insert(self, nodeIndex, distance):
        if nodeIndex > len(self.queue):
            self.queue.extend([ -1 for i in range(nodeIndex - len(self.queue))])
            self.queue.append(distance)
        else:
            self.queue[nodeIndex] = distance

    def getLength(self):
        return self.length