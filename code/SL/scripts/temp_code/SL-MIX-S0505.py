class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def enqueue(self, val):
        new_node = Node(val)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if not self.front:
            return None
        val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

# Priority scoring lambda with bitwise logic
priority_score = lambda x, y: (x & y) | (x << 2) if x > y else (y ^ x) >> 1

# Task management sets
urgent_tasks = {12, 15, 9, 22}
active_tasks = {9, 7, 22, 5}
completed_tasks = {3, 9, 15}

# Stack and Queue initialization
scheduler_stack = Stack()
scheduler_queue = Queue()

# Populate structures
for t in list(urgent_tasks)[:3]:
    scheduler_stack.push(t)

for t in list(active_tasks)[:3]:
    scheduler_queue.enqueue(t)

# Process stack and queue with logical conditions
stack_values = []
queue_values = []

while True:
    s_val = scheduler_stack.pop()
    q_val = scheduler_queue.dequeue()
    if s_val is None or q_val is None:
        break
    stack_values.append(s_val)
    queue_values.append(q_val)

# Logical chain with short-circuit evaluation
score_accumulator = 0
index = 0

while index < len(stack_values) and index < len(queue_values):
    s = stack_values[index]
    q = queue_values[index]
    # Short-circuit with comparison
    if s >= 10 and q <= 10:
        temp_score = priority_score(s, q)
        score_accumulator += temp_score if temp_score > 5 else 0
    index += 1

# Final calculation with set operations
remaining_urgent = urgent_tasks - completed_tasks
common_active = active_tasks & remaining_urgent

final_priority_score = score_accumulator
if len(common_active) > 1:
    final_priority_score *= max(common_active)
else:
    final_priority_score -= sum(common_active)

print(f"Result: {final_priority_score}")