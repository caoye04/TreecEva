from collections import defaultdict

token_stream = ['def', 'func', '(', 'x', ')', ':', 'if', 'x', '>', '0', ':', 'return', 'x', '*', 'func', '(', 'x', '-', '1', ')', 'else', ':', 'return', '1']
state_transitions = {
    'INIT': {'alpha': 'WORD', 'symbol': 'SYMBOL'},
    'WORD': {'alpha': 'WORD', 'symbol': 'BOUNDARY'},
    'SYMBOL': {'alpha': 'BOUNDARY', 'symbol': 'SYMBOL'},
    'BOUNDARY': {'alpha': 'WORD', 'symbol': 'SYMBOL'}
}
char_type = lambda c: 'alpha' if c.isalnum() or c == '_' else 'symbol'
state = 'INIT'
hash_registry = defaultdict(int)
current_lexeme = ''
boundary_counter = 0

for token in token_stream:
    token_hash = hash(token) % 1000
    hash_registry[token_hash] += 1
    
    if len(token) > 1 or token.isalnum():
        input_type = 'alpha'
    else:
        input_type = 'symbol'
        
    if state in state_transitions and input_type in state_transitions[state]:
        next_state = state_transitions[state][input_type]
        if next_state == 'BOUNDARY':
            boundary_counter += 1
        state = next_state
    else:
        state = 'INIT'
        
    if hash_registry[token_hash] > 1:
        boundary_counter += 2

# Execution point Y
print(f"Result: {boundary_counter}")