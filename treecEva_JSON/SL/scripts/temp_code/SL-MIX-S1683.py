from itertools import cycle

def run_beverage_machine(presses):
    states = ['IDLE', 'SELECTING', 'DISPENSING', 'EMPTY']
    current_index = 0
    
    for _ in range(presses):
        if states[current_index] == 'EMPTY':
            break
        current_index = (current_index + 1) % len(states)
    return current_index

# Simulate 7 button presses
final_state_index = run_beverage_machine(7)
print(f'Result: {final_state_index}')