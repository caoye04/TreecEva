import itertools
import re

def validate_token(token):
    components = token.split('-')
    if len(components) != 3:
        return False
    
    part_a, part_b, part_c = components
    
    # Check 1: Part A must be alphanumeric and start with a letter
    if not (part_a.isalnum() and part_a[0].isalpha()):
        return False
    
    # Check 2: Part B must be numeric and its modulo 7 equals 3
    if not (part_b.isdigit() and int(part_b) % 7 == 3):
        return False
    
    # Check 3: Part C must match pattern of two lowercase letters followed by two digits
    if not re.match(r'^[a-z]{2}\d{2}$', part_c):
        return False
    
    return True

token_pool = ['abc12-34567-xy99', 'def89-12348-ab12', 'ghi77-98765-cd34']
valid_tokens = [t for t in token_pool if validate_token(t)]

# Authentication level computation
auth_level = 0
for token in valid_tokens:
    parts = token.split('-')
    numeric_part = int(parts[1])
    char_sum = sum(ord(c) for c in parts[0])
    
    # Short-circuit evaluation with logical operations
    if numeric_part > 50000 and char_sum % 5 == 0 or not (char_sum & 1):
        auth_level += (numeric_part // 1000) % 13
    else:
        auth_level -= (len(parts[2]) * 3) % 7

print(f'Result: {auth_level}')