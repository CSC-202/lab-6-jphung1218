class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
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


def initialize() -> Stack:
    #raise NotImplementedError("Stack.initialize() not defined")
    return Stack()


def isEmpty(data: Stack) -> bool:
    #raise NotImplementedError("Stack.isEmpty() not defined")
    return data.first is None


def push(data: Stack, value: int) -> Stack:
    #raise NotImplementedError("Stack.push() not defined")
    if data.first is None:
        new = Node(value, None)
        data.first = new
    else:
        old = data.first
        new = Node(value, old)
        data.first = new
    return data


def pop(data: Stack) -> tuple[Node, Stack]:
    #raise NotImplementedError("Stack.pop() not defined")
    if data.first is None:
        return None
    else:
        node = data.first
        p = node
        data.first = node.next
        return p, data


def peek(data: Stack) -> Node:
    #raise NotImplementedError("Stack.peek() not defined")
    if data.first is None:
        return None
    else:
        return data.first.value


def clear(data: Stack) -> Stack:
    #raise NotImplementedError("Stack.clear() not defined")
    data.head = None
    return data
