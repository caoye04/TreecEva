from functools import reduce
from collections import namedtuple

def calculate_semantic_weights(token_sequence):
    weights = {'alpha': 3, 'beta': 7, 'gamma': 11, 'delta': 13, 'epsilon': 17}
    return [weights.get(token, 1) for token in token_sequence]

def apply_modification_rules(weight_list):
    modified = []
    for i, w in enumerate(weight_list):
        if i % 3 == 0:
            modified.append(w << 1)
        elif i % 3 == 1:
            modified.append(w ^ 5)
        else:
            modified.append(w | 9)
    return modified

def compute_aggregate(modified_weights):
    SemanticScore = namedtuple('SemanticScore', ['primary', 'secondary'])
    primary_sum = sum(filter(lambda x: x & 1, modified_weights))
    secondary_sum = sum(map(lambda x: x >> 1 if x > 10 else x, modified_weights))
    return SemanticScore(primary_sum, secondary_sum)

# Main processing pipeline
token_stream = ['alpha', 'gamma', 'beta', 'epsilon', 'delta', 'alpha', 'gamma']
weight_sequence = calculate_semantic_weights(token_stream)
transformed_weights = apply_modification_rules(weight_sequence)
aggregated_scores = compute_aggregate(transformed_weights)

# Final scoring calculation
is_complex_text = len(token_stream) > 5 and 'epsilon' in token_stream
complexity_bonus = 42 if is_complex_text else 0
base_computation = (aggregated_scores.primary * 3) - (aggregated_scores.secondary << 1)
final_score = base_computation + complexity_bonus if is_complex_text else base_computation - 15

print(f'Result: {final_score}')