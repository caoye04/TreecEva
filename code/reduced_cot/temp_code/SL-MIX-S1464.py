from collections import deque

class SensorNode:
    def __init__(self, reading, next_node=None):
        self.value = reading
        self.next = next_node

def process_with_context(stack_data):
    total = 0
    while stack_data:
        val = stack_data.pop()
        if val > 0:
            total += val
        else:
            total -= (val * 2)
    return total

# Initialize sensor nodes as a linked list
node_chain = SensorNode(5, SensorNode(-3, SensorNode(7, SensorNode(-2))))

# Stack for contextual processing
context_stack = deque()

# Lambda for conditional transformation
transformer = lambda x: x * 2 if x < 0 else x // 2

accumulator = 0
pointer = node_chain
while pointer:
    raw_value = pointer.value
    processed = transformer(raw_value)
    
    # Logical condition combining AND/OR
    if (processed > 0 and raw_value <= 5) or (processed <= 0 and raw_value > -5):
        context_stack.append(processed)
    else:
        accumulator += processed
    
    pointer = pointer.next

final_output = process_with_context(context_stack) + accumulator
print(f'Result: {final_output}')