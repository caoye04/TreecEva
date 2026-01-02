from collections import Counter, defaultdict
import math

def analyze_frequency(text):
    # Irrelevant function: analyzes character frequency but not used in final result
    char_count = Counter(text.lower())
    total_chars = sum(char_count.values())
    freq_ratio = {char: count / total_chars for char, count in char_count.items()}
    return freq_ratio

def validate_sequence(seq):
    # Semi-relevant function: checks sequence properties but only one result is used
    is_monotonic = all(seq[i] <= seq[i+1] for i in range(len(seq)-1))
    max_value = max(seq)
    min_value = min(seq)
    avg_value = sum(seq) / len(seq)
    variance = sum((x - avg_value) ** 2 for x in seq) / len(seq)
    return is_monotonic, max_value, min_value, avg_value, variance

def calculate_performance(data_log):
    # Core logic with distractions
    raw_values = [x['value'] for x in data_log if x['active']]
    
    # Distractor variables
    temp_buffer = []
    for val in raw_values:
        temp_buffer.append(math.sqrt(val) * 0.1)  # Not used later
    
    # Real processing begins
    adjusted_scores = []
    multiplier = 1.5
    for v in raw_values:
        if v < 10:
            adjusted_scores.append(v * multiplier)
        elif v < 25:
            adjusted_scores.append(v * 1.2)
        else:
            adjusted_scores.append(v * 0.8)
    
    # State tracking with some irrelevant counters
    state_tracker = defaultdict(int)
    above_threshold = 0
    cumulative_shift = 0.0
    
    for score in adjusted_scores:
        if score > 20:
            state_tracker['high'] += 1
            above_threshold += 1
            cumulative_shift += 0.5
        elif score > 10:
            state_tracker['medium'] += 1
            cumulative_shift += 0.2
        else:
            state_tracker['low'] += 1

    # Red herring computation
    normalized_shift = cumulative_shift / (len(adjusted_scores) + 1e-5)
    decay_factor = math.exp(-abs(normalized_shift))

    # Final calculation - depends only on 'above_threshold' from earlier
    base_metric = sum(adjusted_scores)
    bonus = 10 if above_threshold >= 3 else 5
    penalty = 7 if state_tracker['low'] > 1 else 0
    
    final_score = int(base_metric + bonus - penalty)  # This will be printed
    
    return final_score

# Simulated benchmark data
benchmark_data = [
    {'value': 5,  'active': True},
    {'value': 12, 'active': True},
    {'value': 8,  'active': True},
    {'value': 30, 'active': True},
    {'value': 22, 'active': True},
    {'value': 3,  'active': False},  # Inactive, should be skipped
    {'value': 18, 'active': True}
]

# Call the function
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")