from functools import reduce

document_content = "The quick brown fox jumps over the lazy dog"
state_transitions = {0: 'start', 1: 'analyze', 2: 'process', 3: 'finalize'}
current_state = 0
max_state = 3

# Process each character's hash through our state machine
char_hashes = [hash(c) for c in document_content]

for h in char_hashes:
    mod_val = h % 4
    if mod_val == 0:  # Stay in current state
        pass
    elif mod_val == 1:  # Move to next state
        current_state = min(current_state + 1, max_state)
    elif mod_val == 2:  # Skip one state
        current_state = min(current_state + 2, max_state)
    else:  # Return to start (mod_val == 3)
        current_state = 0

final_state = current_state
print(f"Result: {final_state}")