from collections import deque
import math

def calculate_subtree_sum(node):
    if not node:
        return 0
    return node['value'] + calculate_subtree_sum(node['left']) + calculate_subtree_sum(node['right'])

def apply_correction_factor(node):
    if not node:
        return 0
    subtree_sum = calculate_subtree_sum(node)
    correction = math.log(abs(subtree_sum) + 1) if subtree_sum != 0 else 0
    left_correction = apply_correction_factor(node['left'])
    right_correction = apply_correction_factor(node['right'])
    return correction + left_correction + right_correction

def process_transactions(transaction_tree):
    stack = deque()
    stack.append(transaction_tree)
    total_adjustment = 0
    
    while stack:
        current = stack.pop()
        if current:
            # Apply bitwise operation to node value
            adjusted_value = current['value'] ^ (current['value'] >> 2)
            current['value'] = adjusted_value
            
            # Add children to stack
            if current['left']:
                stack.append(current['left'])
            if current['right']:
                stack.append(current['right'])
            
            # Accumulate adjustment
            total_adjustment += adjusted_value & 0xF
    
    # Apply recursive correction
    correction_factor = apply_correction_factor(transaction_tree)
    final_adjustment = int(total_adjustment * correction_factor)
    return final_adjustment

# Transaction tree structure
transaction_tree = {
    'value': 100,
    'left': {
        'value': -50,
        'left': {'value': 25, 'left': None, 'right': None},
        'right': {'value': -10, 'left': None, 'right': None}
    },
    'right': {
        'value': 75,
        'left': {'value': -30, 'left': None, 'right': None},
        'right': {'value': 40, 'left': None, 'right': None}
    }
}

final_adjustment = process_transactions(transaction_tree)
print(f"Result: {final_adjustment}")