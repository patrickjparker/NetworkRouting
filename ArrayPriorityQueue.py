class ArrayPriorityQueue:

    def __init__(self, nodes):
        self.queue = [ -1 for i in range(nodes) ]
        self.length = 0

    def delete_min(self):
        lowest = None
        # Iterate over array and find smallest value
        for index in range(len(self.queue)):
            if self.queue[index] >= 0 and (lowest == None or self.queue[index] < self.queue[lowest]):
                lowest = index
        # If a value is found, "delete" that value
        if lowest != None:
            self.queue[lowest] = -2
            self.length -= 1
        return lowest

    def insert(self, nodeIndex, distance):
        # If index is outside the current array, enlarge the array to fit the index
        if nodeIndex > len(self.queue):
            self.queue.extend([ -1 for i in range(nodeIndex - len(self.queue))])
            self.queue.append(distance)
            self.length += 1
        else:
            if self.queue[nodeIndex] == -1:
                # If setting a unset node, add to length
                self.length += 1
            self.queue[nodeIndex] = distance

    # decrease_key and insert basically do the same thing under the hood
    def decrease_key(self, nodeIndex, distance):
        self.insert(nodeIndex, distance)

    def getLength(self):
        return self.length