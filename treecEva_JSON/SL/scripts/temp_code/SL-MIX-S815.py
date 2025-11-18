import re
from collections import defaultdict

def validate_token(token, depth=0):
    if depth > 3:
        return False
    if token.startswith('<') and token.endswith('>'):
        return True
    elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', token):
        return len(token) % 2 == 0
    elif token.isdigit():
        return int(token) > 0 and (int(token) & (int(token) - 1)) == 0
    else:
        return validate_token(token[:-1], depth+1) if token else False

tokens = ['<START>', 'itemCount', '16', 'config_data', '256', '_tempVar', '0', '<END>']
categories = defaultdict(list)
validated_count = 0

for t in tokens:
    if validate_token(t):
        validated_count += 1
        if t.startswith('<'):
            categories['tags'].append(t)
        elif t.isidentifier():
            categories['identifiers'].append(t)
        elif t.isdigit() and int(t) > 0:
            categories['literals'].append(t)

# Apply logical filters using short-circuit evaluation
if categories['literals'] and all(int(x) > 10 for x in categories['literals']):
    validated_count += sum(1 for _ in filter(lambda x: len(x) > 5, categories['identifiers']))

# Final adjustment based on tag count
if len(categories['tags']) >= 2 and not (len(categories['identifiers']) == 0 or len(categories['literals']) == 0):
    validated_count *= 2

print(f"Result: {validated_count}")