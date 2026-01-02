from collections import defaultdict
from itertools import combinations

def analyze_frequency(text):
    freq = defaultdict(int)
    for char in text.lower():
        if char.isalpha():
            freq[char] += 1
    return freq

def generate_pairs(elements):
    # Irrelevant helper function - dead code path
    return list(combinations(elements, 2))
def preprocess_metrics(raw):
    cleaned = []
    temp_buffer = []
    for val in raw:
        if val > 0:
            temp_buffer.append(val * 0.9)
        else:
            temp_buffer.append(0)
    smoothing_factor = 1.1
    for x in temp_buffer:
        cleaned.append(x * smoothing_factor)
    return cleaned

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * __import__('math').log(p)
    return round(entropy, 4)

def evaluate_performance(metrics):
    baseline = sum(metrics) / len(metrics) if metrics else 0
    adjusted_metrics = [m * 1.05 for m in metrics]
    
    # Tracking state across iterations (intermediate distractor)
    history_log = []
    cumulative_shift = 0
    for i, val in enumerate(adjusted_metrics):
        if i % 2 == 0:
            cumulative_shift += val * 0.01
        history_log.append(cumulative_shift)
    
    # Core logic embedded among distractions
    threshold = 85
    above_threshold = [m for m in adjusted_metrics if m >= threshold]
    penalty = len(history_log) * 0.02  # Minor adjustment
    
    # Key computation
    raw_sum = sum(above_threshold)
    count_bonus = len(above_threshold) * 5
    base_score = raw_sum + count_bonus
    
    # Distracting transformation
    temp_result = base_score * 0.99
    noise_offset = compute_entropy([len(metrics), len(above_threshold)])
    final_score = int(temp_result - noise_offset * 10 + penalty)
    
    # Unused variables - red herrings
    outlier_flags = [False] * len(metrics)
    validation_trace = set()
    for idx, m in enumerate(metrics):
        if m < 10:
            validation_trace.add(idx)

    return final_score

# Simulated input data
raw_input = [78, 92, 88, 96, 73, 85, 91, 80, 89]
cleaned_data = preprocess_metrics(raw_input)

# Character frequency analysis - irrelevant to main logic
text_sample = "Performance evaluation metrics"
frequency_map = analyze_frequency(text_sample)
letter_groups = generate_pairs(['a', 'b', 'c'])  # Dead computation

metric_data = [round(x) for x in cleaned_data]

# Key execution point
final_score = evaluate_performance(metric_data)

print(f"Target result: {final_score}")