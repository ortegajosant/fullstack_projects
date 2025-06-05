class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleEndedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def initialize_deque(self, new_node):
        self.head = new_node
        self.tail = self.head

    def push_left(self, value):
        new_node = Node(value)
        if not self.head:
            self.initialize_deque(new_node)
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, value):
        new_node = Node(value)
        if not self.tail:
            self.initialize_deque(new_node)
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if not self.head:
            print("Queue is empty.")
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def pop_right(self):
        if not self.tail:
            print("Queue is empty.")
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def print_queue(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


def main():
    deque = DoubleEndedQueue()
    deque.push_left(10)
    deque.push_right(20)
    deque.push_left(5)
    deque.push_right(30)

    print("Current queue:")
    deque.print_queue()

    print("Popped from left:", deque.pop_left())
    print("Current queue after popping from left:")
    deque.print_queue()

    print("Popped from right:", deque.pop_right())
    print("Current queue after popping from right:")
    deque.print_queue()


if __name__ == "__main__":
    main()
