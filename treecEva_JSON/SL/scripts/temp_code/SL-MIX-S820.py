from collections import deque
import statistics

# Bakery batch stack (using deque as a stack)
batch_stack = deque()

# Push daily batches onto the stack
batch_stack.append(24)
batch_stack.append(36)
batch_stack.append(28)
batch_stack.append(42)
batch_stack.append(30)

# Calculate average loaves per batch
loaves_list = list(batch_stack)
average_loaves = statistics.mean(loaves_list)

print(f'Result: {average_loaves}')