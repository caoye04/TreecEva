from collections import defaultdict

def run_vending_machine():
    states = {'idle': 0, 'selection': 1, 'dispensing': 2, 'change_return': 3}
    transition_sequence = ['idle', 'selection', 'dispensing', 'change_return', 'idle', 'selection']
    
    transition_points = 0
    for state in transition_sequence:
        transition_points += states[state]
    
    return transition_points

points = run_vending_machine()
print(f"Result: {points}")