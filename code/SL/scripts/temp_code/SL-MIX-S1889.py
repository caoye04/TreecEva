from collections import namedtuple
import re

def process_document_stages(content):
    # State machine using namedtuple for stage definitions
    Stage = namedtuple('Stage', ['name', 'transform_func', 'validate_func'])
    
    stages = [
        Stage('normalize', 
              lambda x: x.strip().lower(), 
              lambda x: len(x) > 0),
        Stage('clean_punct', 
              lambda x: re.sub(r'[^a-z0-9 ]', '', x), 
              lambda x: 'error' not in x),
        Stage('tokenize', 
              lambda x: x.split(), 
              lambda x: len(x) >= 3),
        Stage('filter_tokens', 
              lambda x: [t for t in x if len(t) > 2], 
              lambda x: len(x) > 0)
    ]
    
    doc_state = content
    validation_score = 0
    
    # Process through stages
    for i, stage in enumerate(stages):
        # Apply transformation
        doc_state = stage.transform_func(doc_state)
        
        # Short-circuit evaluation: only validate if previous stage passed (i>0) and current state passes validation
        if (i == 0 or validation_score > 0) and stage.validate_func(doc_state):
            validation_score += 10 * (i + 1)  # Weight later stages more heavily
        else:
            validation_score -= 5  # Penalty for failure
    
    # Dictionary comprehension to count token frequencies
    token_counts = {token: sum(1 for t in doc_state if t == token) for token in set(doc_state)} if isinstance(doc_state, list) else {}
    
    # Merge with base counts
    base_counts = {'total': len(doc_state) if isinstance(doc_state, list) else 0}
    merged_stats = {**base_counts, **token_counts}
    
    # Final score adjustment based on stats
    validation_score += sum(merged_stats.values())
    
    return validation_score

# Execute pipeline
initial_content = "  Error-check this DOCUMENT!! It's full of mistakes... "
document_result = process_document_stages(initial_content)
print(f"Result: {document_result}")