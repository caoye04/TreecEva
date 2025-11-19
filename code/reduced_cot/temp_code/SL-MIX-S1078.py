from functools import reduce
from itertools import combinations

def process_signal_batch(signal_values, threshold):
    # Step 1: Apply modular transformation
    transformed = [(val * 3 + 7) % 13 for val in signal_values]
    
    # Step 2: Filter using boolean logic with ternary operator
    filtered = [x if x > threshold else 0 for x in transformed]
    
    # Step 3: Generate pairwise combinations and apply bitwise operations
    combo_scores = []
    for a, b in combinations(filtered, 2):
        combo_score = (a & b) | (a ^ b)
        combo_scores.append(combo_score)
    
    return combo_scores

def calculate_network_score(batch_results, weights):
    # Step 4: Weighted aggregation using functional programming
    weighted = list(map(lambda x, w: x * w, batch_results, weights))
    
    # Step 5: Conditional aggregation based on parity
    positive_sum = sum(filter(lambda x: x > 0, weighted))
    negative_count = len(list(filter(lambda x: x < 0, weighted)))
    
    # Step 6: Final score calculation with modular arithmetic
    raw_score = positive_sum - (negative_count * 5)
    final_score = raw_score % 17 if raw_score > 0 else (raw_score % 17) + 17
    
    return final_score

# Signal processing pipeline
network_signals = [4, 9, 2, 11, 7, 15, 3]
signal_threshold = 5

processed_signals = process_signal_batch(network_signals, signal_threshold)
weight_vector = [1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1]

finalScore = calculate_network_score(processed_signals, weight_vector)
print(f"Result: {finalScore}")