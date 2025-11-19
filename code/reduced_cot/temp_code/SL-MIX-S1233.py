import base64
import re
from functools import reduce

def process_document_workflow():
    # Document metadata tags
    tags = ['CONFIDENTIAL', 'INTERNAL', 'PUBLIC', 'RESTRICTED']
    encoded_metadata = base64.b64encode(':'.join(tags).encode()).decode()
    
    # State machine for document classification
    state_transitions = {
        'INIT': {'CONFIDENTIAL': 'HIGH', 'RESTRICTED': 'HIGH'},
        'HIGH': {'INTERNAL': 'MEDIUM', 'PUBLIC': 'LOW'},
        'MEDIUM': {'PUBLIC': 'LOW'},
        'LOW': {}
    }
    
    # Decode metadata and initialize state
    decoded_tags = base64.b64decode(encoded_metadata).decode().split(':')
    current_state = 'INIT'
    security_score = 0
    
    # Process each tag through state machine
    for tag in decoded_tags:
        if tag in state_transitions[current_state]:
            current_state = state_transitions[current_state][tag]
        
        # Assign score based on state
        if current_state == 'HIGH':
            security_score += 10
        elif current_state == 'MEDIUM':
            security_score += 5
        elif current_state == 'LOW':
            security_score += 1
    
    # Apply pattern matching to adjust score
    pattern_matches = sum(1 for tag in decoded_tags if re.match(r'^[A-Z]+$', tag))
    adjusted_score = security_score * pattern_matches
    
    # Final calculation using functional programming
    weights = [1, 2, 3, 4]
    weighted_values = list(map(lambda x, y: x * y, [adjusted_score, len(decoded_tags), pattern_matches, security_score], weights))
    final_security_score = reduce(lambda a, b: a + b, weighted_values)
    
    return final_security_score

final_security_score = process_document_workflow()
print(f"Result: {final_security_score}")