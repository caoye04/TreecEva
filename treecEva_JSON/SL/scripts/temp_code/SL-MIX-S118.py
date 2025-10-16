from functools import reduce

def log_operations(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_operations
def transform_token(token):
    if token == '(':
        return 'L'
    elif token == ')':
        return 'R'
    else:
        return 'O'

# Token stream to process
token_stream = ['(', '(', ')', '(', ')', ')', '(', '(', ')']

# Initialize state machine components
stack_depth = 0
mismatch_counter = 0
processing_stack = []
state_transitions = {'start': {'L': 'open', 'R': 'error'},
                     'open': {'L': 'nested', 'R': 'closing', 'O': 'other'},
                     'nested': {'L': 'deep', 'R': 'pop', 'O': 'other_nested'},
                     'deep': {'R': 'pop_deep', 'O': 'other_deep'},
                     'closing': {'R': 'error', 'L': 'open', 'O': 'other_closed'},
                     'pop': {'R': 'pop', 'L': 'nested', 'O': 'other_pop'},
                     'pop_deep': {'R': 'pop', 'L': 'deep', 'O': 'other_pop_deep'},
                     'error': {'L': 'open', 'R': 'error', 'O': 'other_error'},
                     'other': {},
                     'other_nested': {},
                     'other_deep': {},
                     'other_closed': {},
                     'other_pop': {},
                     'other_pop_deep': {},
                     'other_error': {}}

current_state = 'start'

# Process each token
for token in token_stream:
    transformed = transform_token(token)
    
    # State transition
    if transformed in state_transitions[current_state]:
        next_state = state_transitions[current_state][transformed]
    else:
        next_state = current_state
    
    # Handle state actions
    if next_state == 'open' or next_state == 'nested' or next_state == 'deep':
        processing_stack.append(transformed)
        stack_depth += 1
    elif next_state == 'pop' or next_state == 'pop_deep':
        if processing_stack:
            processing_stack.pop()
            stack_depth -= 1
        else:
            mismatch_counter += 1
    elif next_state == 'error':
        mismatch_counter += 1
    
    current_state = next_state
    
    # Early termination check
    if mismatch_counter > 2:
        break

# Account for unclosed brackets
remaining_brackets = set(processing_stack)
if 'L' in remaining_brackets:
    mismatch_counter += len([x for x in processing_stack if x == 'L'])

print(f"Result: {mismatch_counter}")