import hashlib

token_stream = ['BEGIN', 'FUNC', 'VAR', 'BEGIN', 'LOOP', 'END', 'END']
symbol_table = {}
scope_stack = []
active_scope_depth = 0

hash_token = lambda t: hashlib.md5(t.encode()).hexdigest()[:8]

for token in token_stream:
    token_hash = hash_token(token)
    if token.startswith('BEGIN'):
        scope_stack.append(token_hash)
        active_scope_depth = len(scope_stack)
    elif token.startswith('END'):
        if scope_stack:
            popped = scope_stack.pop()
            active_scope_depth = len(scope_stack)
    else:
        if token not in symbol_table:
            symbol_table[token] = 0
        symbol_table[token] += 1
        
# Process a special directive outside the main loop
special_tokens = [t for t in token_stream if len(t) > 3 and t != 'BEGIN' and t != 'END']
for st in special_tokens:
    if st in symbol_table:
        symbol_table[st] *= 2
    
final_hash = hash_token('FINAL')
scope_stack.append(final_hash)
active_scope_depth = len(scope_stack)

print(f"Result: {active_scope_depth}")