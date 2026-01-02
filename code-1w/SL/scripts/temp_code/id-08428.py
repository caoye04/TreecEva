from itertools import combinations

def analyze_text_patterns(text_data):
    # Irrelevant helper: counts character frequencies (not used in final result)
    char_freq = {}
    for char in text_data:
        char_freq[char] = char_freq.get(char, 0) + 1
    unique_chars = len(char_freq)
    return unique_chars

def linear_search(arr, target):
    # Unused but plausible helper function
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def evaluate_performance(weights, results):
    weighted_sum = 0.0
    normalization_factor = sum(weights)
    
    # Distractor: creating unused pairs
    index_pairs = list(combinations(range(len(results)), 2))
    pair_count = len(index_pairs)  # Not used later
    
    temp_adjustment = 0.0
    for i, result in enumerate(results):
        if i % 2 == 0:
            temp_adjustment += 0.1 * (i + 1)
        else:
            temp_adjustment -= 0.05 * (i + 1)
    
    # Actual computation
    for i in range(len(weights)):
        contribution = weights[i] * results[i]
        weighted_sum += contribution
    
    # Final scoring with red herring adjustment that cancels out
    dummy_offset = temp_adjustment - temp_adjustment  # Useless but looks meaningful
    final_value = (weighted_sum / normalization_factor) + dummy_offset
    
    return final_value

# Main execution
raw_text = "algorithmic_complexity_assessment"
analyze_text_patterns(raw_text)  # Called but return value ignored

metric_weights = [0.3, 0.5, 0.7, 1.0, 0.4]
raw_results = [85, 90, 78, 92, 88]

# Key statement
final_score = evaluate_performance(metric_weights, raw_results)

print(f"Result: {final_score}")