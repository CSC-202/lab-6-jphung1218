class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Queue:
    #raise NotImplementedError("Queue.initialize() not defined")
    return Queue()


def isEmpty(data: Queue) -> bool:
    #raise NotImplementedError("Queue.isEmpty() not defined")
    return data.first is None


def enqueue(data: Queue, value: int) -> Queue:
    #raise NotImplementedError("Queue.enqueue() not defined")
    new = Node(value, None)
    def helper(node, value):
        if node.next is None:
            node.next = new
        else:
            helper(node.next, value)
    
    if data.first is None:
        data.first = new
    else:
        helper(data.first, value)
    
    return data


def dequeue(data: Queue) -> tuple[Node, Queue]:
    #raise NotImplementedError("Queue.dequeue() not defined")
    if data.first is None:
        return None
    else:
        front = data.first
        data.first = front.next
        return front, data


def peek(data: Queue) -> Node:
    #raise NotImplementedError("Queue.peek() not defined")
    if data.first is None:
        return None
    else:
        return data.first.value


def clear(data: Queue) -> Queue:
    #raise NotImplementedError("Queue.clear() not defined")
    data.head = None
    return data
