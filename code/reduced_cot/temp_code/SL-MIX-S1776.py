from collections import deque

# Initialize state machine
initial_state = 0
snack_queue = deque([2, 4, 1, 5])
current_state = initial_state

# Process each snack purchase
while snack_queue:
    snack_id = snack_queue.popleft()
    current_state = (current_state * 3 + snack_id) % 7

final_state = current_state
print(f"Result: {final_state}")