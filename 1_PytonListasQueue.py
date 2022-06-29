# By :- Om Nai
# Date :- 27 June 2022


class Queue:
    def __init__(self):
        self.q = []
        pass

    def isEmpty(self):
        if self.q == []:
            return True
        else:
            return False
        pass

    def enqueue(self, value):
        self.q.append(value)
        return 'Element insert successfull'
        pass

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            x = self.q[0]
            del self.q[0]
            return x
        pass

    def __str__(self) -> str:
        value = [str(x) for x in self.q]
        return ' '.join(value)
        pass

    def delete(self):
        self.q = None
        pass


customeQueue = Queue()

customeQueue.isEmpty()
customeQueue.enqueue(25)
customeQueue.enqueue(36)
customeQueue.enqueue(54)
customeQueue.enqueue(76)
customeQueue.enqueue(55)
customeQueue.enqueue(88)
customeQueue.enqueue(97)
print(customeQueue)
customeQueue.dequeue()
customeQueue.dequeue()
print(customeQueue)