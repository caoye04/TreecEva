from math import comb

class Node:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

class NetworkAnalyzer:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

network = NetworkAnalyzer()
node_count = 8
for i in range(1, node_count + 1):
    fib_index = fibonacci(i)
    combo_factor = comb(i, min(3, i)) if i >= 3 else 1
    amplification = fib_index * combo_factor
    network.append(amplification)

current = network.head
cumulative_gain = 0
while current:
    cumulative_gain += current.value
    current = current.next

print(f"Result: {cumulative_gain}")