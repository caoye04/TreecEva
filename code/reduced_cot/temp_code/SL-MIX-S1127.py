import re
from functools import reduce

def calculate_linguistic_metrics():
    document_fragments = [
        "The Quick Brown Fox Jumps Over The Lazy Dog.",
        "Advanced analysis requires complex computations.",
        "Pattern recognition involves multiple verification steps."
    ]
    
    linguistic_patterns = [r'\b[A-Z]{2,}\b', r'\b[a-z]{8,}\b', r'\b\w*ly\b']
    
    fragment_scores = []
    
    for fragment in document_fragments:
        pattern_matches = []
        for pattern in linguistic_patterns:
            matches = re.findall(pattern, fragment)
            pattern_matches.append(len(matches))
        
        if any(count > 0 for count in pattern_matches):
            score = reduce(lambda x, y: x * (y + 1), pattern_matches, 1)
        else:
            score = 0
        
        fragment_scores.append(score)
    
    # Apply transformation using lambda and closure
    weight_function = lambda w: lambda x: x * w if x > 0 else x
    weighted_scores = list(map(weight_function(3), fragment_scores))
    
    # Calculate final linguistic score
    linguistic_score = sum(weighted_scores) + len([s for s in weighted_scores if s > 0])
    
    return linguistic_score

# Execute the analysis
linguistic_score = calculate_linguistic_metrics()
print(f"Result: {linguistic_score}")