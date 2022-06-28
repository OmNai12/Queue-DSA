# By :- Om Nai
# Date :- 28 June 2022

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        pass


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        pass


class Queue:
    def __init__(self) -> None:
        self.linkedListQueue = LinkedList()
        pass

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedListQueue.head == None:
            self.linkedListQueue.head = newNode
            self.linkedListQueue.tail = newNode
        else:
            self.linkedListQueue.tail.next = newNode
            self.linkedListQueue.tail = newNode
    pass

    def isEmpty(self):
        if self.linkedListQueue.head == None:
            return True
        else:
            return False
        pass

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            x = self.linkedListQueue.head.value
            if self.linkedListQueue.head == self.linkedListQueue.tail:
                self.linkedListQueue.head = None
                self.linkedListQueue.tail = None
            else:
                self.linkedListQueue.head = self.linkedListQueue.head.next
        return x
        pass

    def display(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            tempNode = self.linkedListQueue.head
            while tempNode != None:
                print(tempNode.value, end=" ")
                tempNode = tempNode.next
    pass


customeQueue = Queue()
customeQueue.enqueue(78)
customeQueue.enqueue(95)
customeQueue.enqueue(13)
customeQueue.enqueue(63)
customeQueue.enqueue(88)
customeQueue.display()
print("\nThe element dequeued : ",customeQueue.dequeue())
customeQueue.display()