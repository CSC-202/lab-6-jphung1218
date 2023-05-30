class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    #raise NotImplementedError("List.initialize() not defined")
    return List()


def isEmpty(data: List) -> bool:
    #raise NotImplementedError("List.isEmpty() not defined")
    return data.first is None


def addAtIndex(data: List, index: int, value: int) -> List:
    #raise NotImplementedError("List.addAtIndex() not defined")
    i = 0
    # make recursive helper function..............
    def helper(node, i, index, value):
        if index == 0:
            addToFront(data, value)
        elif i == index - 1:
            new = Node(value, node.next)
            node.next = new
        else:
            helper(node.next, i+1, index, value)
    
    if data.first is None:
        return None
    else:
        helper(data.first, i, index, value)

    return data


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    #raise NotImplementedError("List.removeAtIndex() not defined")
    i = 0

    def helper(node, i, index):
        if i == index - 1:
            rn = node.next
            node.next = node.next.next
        else:
            helper(node.next, i+1, index)
        
        return rn
    
    if data.first is None:
        return None
    else:
        rn = helper(data.first, i, index)

    return (rn, data)


def addToFront(data: List, value: int) -> List:
    #raise NotImplementedError("List.addToFront() not defined")
    if data.first is None:
        new = Node(value, None)
        data.first = new
    else:
        node = data.first
        new = Node(value, node)
        data.first = new
    return data


def addToBack(data: List, value: int) -> List:
    #raise NotImplementedError("List.addToBack() not defined")
    def helper(node, value):
        if node.next is None:
            new = Node(value, None)
            node.next = new
        else:
            helper(node.next, value)
    
    if data.first is None:
        return None
    else:
        helper(data.first, value)

    return data


def getElementAtIndex(data: List, index: int) -> Node:
    #raise NotImplementedError("List.getElementAtIndex() not defined")
    i = 0
    def helper(node, i, index):
        if i == index - 1:
            return node
        else:
            helper(node.next, i+1, index)
    
    if data.first is None:
        return None
    else:
        n = helper(data.first, i, index)
    return n


def clear(data: List) -> List:
    #raise NotImplementedError("List.clear() not defined")
    data.head = None
    return data
