import re
from collections import defaultdict, deque

token_stream = ['[', 'SECTION', ':', 'Introduction', ']', '{', 'BOLD', '(', 'text', ')', '}', '[', '/', 'SECTION', ']']
state_stack = deque(['ROOT'])
nesting_depth = 0
max_depth = 0
state_transitions = {
    'ROOT': {'\[': 'SECTION_TAG', '\{': 'FORMAT_TAG'},
    'SECTION_TAG': {':': 'CONTENT_EXPECTED', '\]': 'ROOT'},
    'CONTENT_EXPECTED': {'[^\[\{\/]+': 'CONTENT', '\[': 'SECTION_TAG', '\{': 'FORMAT_TAG', '\/': 'CLOSING_TAG'},
    'CLOSING_TAG': {']': 'ROOT'},
    'FORMAT_TAG': {'\(': 'FORMAT_CONTENT', '\)': 'ROOT'}
}
current_state = 'ROOT'

for token in token_stream:
    # State machine transition logic
    next_state = None
    for pattern, target_state in state_transitions.get(current_state, {}).items():
        if re.match(pattern, token):
            next_state = target_state
            break
    
    if next_state:
        if next_state in ['SECTION_TAG', 'FORMAT_TAG']:
            state_stack.append(next_state)
            nesting_depth = len(state_stack) - 1  # Exclude ROOT
            max_depth = max(max_depth, nesting_depth)
        elif next_state == 'ROOT' and state_stack:
            state_stack.pop()
            nesting_depth = len(state_stack) - 1
        current_state = next_state
    else:
        # Handle content tokens
        if current_state == 'CONTENT_EXPECTED':
            current_state = 'CONTENT_EXPECTED'  # Remain in same state

# Finalize with maximum depth encountered
nesting_depth = max_depth
print(f"Result: {nesting_depth}")