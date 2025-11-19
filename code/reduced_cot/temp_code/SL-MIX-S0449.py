from collections import defaultdict

class ScopeStack:
    def __init__(self):
        self.stack = []
    
    def __enter__(self):
        self.stack.append(defaultdict(int))
        return self.stack[-1]
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.stack:
            self.stack.pop()
    
    def current_scope(self):
        return self.stack[-1] if self.stack else None

scopes = ScopeStack()
active_scope_count = 0
token_hashes = {
    'BEGIN': hash('BEGIN'),
    'END': hash('END'),
    'VAR': hash('VAR'),
    'ASSIGN': hash('ASSIGN')
}

# Token stream: BEGIN VAR x ASSIGN 5 END BEGIN VAR y ASSIGN 10 END
stream = [
    token_hashes['BEGIN'],
    token_hashes['VAR'], hash('x'),
    token_hashes['ASSIGN'], hash('5'),
    token_hashes['END'],
    token_hashes['BEGIN'],
    token_hashes['VAR'], hash('y'),
    token_hashes['ASSIGN'], hash('10'),
    token_hashes['END']
]

i = 0
while i < len(stream):
    if stream[i] == token_hashes['BEGIN']:
        with scopes as scope:
            active_scope_count += 1
            j = i + 1
            # Process until END or end of stream
            while j < len(stream) and stream[j] != token_hashes['END']:
                if stream[j] == token_hashes['VAR'] and j + 2 < len(stream) and stream[j+2] == token_hashes['ASSIGN']:
                    var_name_hash = stream[j+1]
                    value_hash = stream[j+3]
                    scope[var_name_hash] = value_hash
                    j += 4
                else:
                    j += 1
            i = j + 1 if j < len(stream) and stream[j] == token_hashes['END'] else j
    else:
        i += 1

print(f"Result: {active_scope_count}")