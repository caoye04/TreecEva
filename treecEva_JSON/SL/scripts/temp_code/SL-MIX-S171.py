from collections import deque

class Operation:
    def __init__(self, name, base_priority):
        self.name = name
        self.base_priority = base_priority

def compute_adjustment(op, factor):
    return op.base_priority * factor + (7 & (op.base_priority >> 1))

operation_stack = []
movement_queue = deque()

op1 = Operation('GRAB', 12)
op2 = Operation('LIFT', 8)
op3 = Operation('ROTATE', 15)

operation_stack.append(op1)
movement_queue.append(op2)
operation_stack.append(op3)

priority_accumulator = 0
adjustment_factor = 3

while operation_stack:
    current_op = operation_stack.pop()
    if movement_queue and current_op.base_priority > 10:
        queued_op = movement_queue.popleft()
        priority_accumulator += compute_adjustment(current_op, adjustment_factor) - queued_op.base_priority
    else:
        priority_accumulator += compute_adjustment(current_op, adjustment_factor) // 2

final_adjustment = priority_accumulator + (len(operation_stack) << 2)
print(f'Result: {final_adjustment}')