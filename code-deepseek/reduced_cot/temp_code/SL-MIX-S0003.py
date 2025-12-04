import re

def sanitize_metadata(doc_meta):
    return re.sub(r'[^a-zA-Z0-9_\- ]', '', doc_meta).strip()

def evaluate_clearance(doc_meta):
    sanitized = sanitize_metadata(doc_meta)
    is_internal = 'INTERNAL' in sanitized
    is_confidential = 'CONFIDENTIAL' in sanitized
    is_public = 'PUBLIC' in sanitized
    
    # Short-circuit evaluation with logical operations
    if is_public and not (is_internal or is_confidential):
        return 1
    elif is_internal and not is_confidential:
        return 2
    elif is_confidential or (is_internal and 'RESTRICTED' in sanitized):
        return 3
    else:
        return 0

documents_metadata = [
    'PUBLIC DOCUMENT',
    'INTERNAL USE ONLY - CONFIDENTIAL',
    'CONFIDENTIAL - RESTRICTED ACCESS',
    'PUBLIC RELEASE - INTERNAL REVIEW',
    'RESTRICTED CONFIDENTIAL DOCUMENT'
]

# List comprehension with generator expression
processed_levels = [evaluate_clearance(meta) for meta in documents_metadata if len(meta) > 10]

# Pattern matching for final classification
access_level = 0
match sum(processed_levels):
    case n if n > 10:
        access_level = 5
    case n if n > 7:
        access_level = 4
    case n if n > 4:
        access_level = 3
    case n if n > 1:
        access_level = 2
    case _:
        access_level = 1

print(f'Result: {access_level}')