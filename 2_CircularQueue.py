# By :- Om Nai
# Date :- 29 June 2022


class Queue:
    def __init__(self, queueSize) -> None:
        self.q = queueSize * [None]
        self.queueSize = queueSize
        self.front = -1
        self.end = -1
        pass

    def __str__(self) -> str:
        value = [str(x) for x in self.q]
        return ' '.join(value)
        pass

    def __isFull(self):
        if ((self.end + 1) % self.queueSize) == self.front:
            return True
        else:
            return False
        pass

    def __isEmpty(self):
        if self.end == -1:
            return True
        else:
            return False
        pass

    def enqueue(self, value):
        if self.__isFull():
            print("Queue is full")
        else:
            if self.front == -1 and self.end == -1:
                self.front = self.end = 0
            else:
                self.end = (self.end + 1) % self.queueSize
            self.q[self.end] = value
        pass

    def dqueue(self):
        if self.__isEmpty():
            print("Queue is empty")
        else:
            x = self.q[self.front]
            self.q[self.front] = None
            if self.front == self.end:
                self.front = self.end = -1
            else:
                self.front = (self.front + 1) % self.queueSize
            return x
        pass

    def peek(self):
        return self.front
        pass

    def delete(self):
        self.front = self.end = -1
        self.q.clear()
        pass


# Creating queue from above class...


customeQueue = Queue(5)

customeQueue.enqueue(95)
customeQueue.enqueue(88)
customeQueue.enqueue(13)
customeQueue.enqueue(45)
customeQueue.enqueue(57)
print(customeQueue)