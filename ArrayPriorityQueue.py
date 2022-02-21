class ArrayPriorityQueue:

    def __init__(self):
        self.queue = []

    def decrease_key(self, distance, node):
        if node.node_id > len(self.queue):
            self.insert(distance, node)
        else:
            self.queue[node.node_id] = distance

    def delete_min(self):
        lowest = None
        for index in range(len(self.queue)):
            if self.queue[index] >= 0 and (lowest == None or self.queue[index] < self.queue[lowest]):
                lowest = index
        if lowest != None:
            self.queue[lowest] = -2
            self.length -= 1
        return lowest

    def insert(self, distance, node):
        if node.node_id > len(self.queue):
            self.queue.extend([ -1 for i in range(node.node_id - len(self.queue))])
            self.queue.append(distance)
        else:
            self.queue[node.node_id] = distance

    def getLength(self):
        return self.length