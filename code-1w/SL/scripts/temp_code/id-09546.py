from collections import defaultdict
import math

def preprocess_input(data_str):
    # Split and clean input string
    tokens = data_str.strip().split(',')
    cleaned = [t.strip().lower() for t in tokens]
    return cleaned

def calculate_metrics(values):
    # Some intermediate calculations with distractions
    base_total = sum(v * 1.5 for v in values)
    adjustment = len(values) ** 0.5
    dummy_offset = sum([i * 0.1 for i in range(len(values))])  # Irrelevant
    meaningful_adjustment = base_total / (adjustment + 1)
    return base_total, meaningful_adjustment

def build_frequency_map(items):
    freq = defaultdict(int)
    for item in items:
        freq[item] += 1
    return freq

def extract_numerical_patterns(token_list):
    counts = []
    lengths = []  
    for token in token_list:
        digit_count = sum(1 for c in token if c.isdigit())
        counts.append(digit_count)
        lengths.append(len(token))
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    total_digits = sum(counts)
    return total_digits, avg_length

def process_results(raw_data, weights):
    # Main processing function
    processed_tokens = preprocess_input(raw_data)
    
    # Extract patterns (some useful, some not)
    digit_count, mean_len = extract_numerical_patterns(processed_tokens)
    
    # Build frequency map - relevant later
    freq_map = build_frequency_map(processed_tokens)
    
    # Generate numeric vector from frequencies
    numeric_vector = [freq_map[t] * 10 for t in set(processed_tokens)]
    
    # Perform core metric calculation
    raw_sum, adjusted_sum = calculate_metrics(numeric_vector)
    
    # Dummy transformations (distraction)
    temp_cache = {f'key_{i}': raw_sum * 0.01 for i in range(3)}
    cached_value = temp_cache['key_1']  # Not used later
    
    # Weighted combination using external weights
    weighted_component = sum(val * weights[i % len(weights)] for i, val in enumerate(numeric_vector))
    
    # Final nonlinear transformation
    stability_factor = math.log(adjusted_sum + 2) if adjusted_sum > 0 else 0
    score_breakdown = [
        weighted_component * 0.4,
        stability_factor * digit_count * 1.2,
        mean_len * 5
    ]
    
    final_score = int(sum(score_breakdown))  # Deterministic integer result
    
    # Dead code path - never executed but looks plausible
    if False:
        fallback = sum(numeric_vector) // 2
        final_score = max(final_score, fallback)
    
    return final_score

# Input data and parameters
raw_data = "Apple, banana, apple, cherry, banana, apple, date"
weights = [0.7, 1.3, 0.9, 1.1]

# Execute main logic
final_score = process_results(raw_data, weights)
print(f"Result: {final_score}")