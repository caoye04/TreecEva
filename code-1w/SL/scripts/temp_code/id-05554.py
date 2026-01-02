from collections import defaultdict

# Simulate sensor data with noise and redundant channels
data_stream = [
    (1, 'A', 12), (2, 'B', 15), (3, 'A', -8), (4, 'C', 23),
    (5, 'B', 0), (6, 'A', 11), (7, 'D', -5), (8, 'C', 19),
    (9, 'B', 7), (10, 'A', 14), (11, 'E', -12), (12, 'C', 21)
]

# Irrelevant mapping - distractor
device_weights = {'A': 0.5, 'B': 0.3, 'C': 0.7, 'D': 0.2, 'E': 0.9}
weight_sum = sum(device_weights.values())
adjusted_weights = {k: v / weight_sum for k, v in device_weights.items()}

# Track counts per device (semi-relevant)
device_count = defaultdict(int)
for _, device, _ in data_stream:
    device_count[device] += 1

# Filter only positive readings above threshold (core logic start)
threshold = 10
filtered_data = [value for _, _, value in data_stream if value > threshold]

# Misleading transformation - not used later but looks important
normalized_values = [round(v / max(filtered_data), 3) for v in filtered_data] if filtered_data else [0]
mean_value = sum(normalized_values) / len(normalized_values) if normalized_values else 0

# Auxiliary function that appears critical but has red herring parameters
def analyze_trend(values, method='moving_avg', lookback=3):
    if len(values) < lookback:
        return 0
    recent = values[-lookback:]
    avg_recent = sum(recent) / len(recent)
    return avg_recent - sum(values[:lookback]) / len(values[:lookback]) if len(values) >= lookback else 0

# Another distraction: trend analysis on normalized scale
trend_score = analyze_trend([int(x * 100) for x in normalized_values])

# Core processing function with conditional logic
def process_signals(signal_list, limit):
    base = 0
    penalty = 0
    
    # Bitwise interaction between elements (advanced operation)
    for i, val in enumerate(signal_list):
        if i % 2 == 0:
            base ^= val  # XOR accumulation on even indices
        else:
            base += val & 7  # Bitwise AND then add
    
    # Conditional adjustment based on length (hidden rule)
    if len(signal_list) > 4:
        adjustment = 13
    else:
        adjustment = 5
    
    # Secondary check using min/max deviation
    if max(signal_list) - min(signal_list) > 15:
        penalty = 3
    
    # Final computation chain
    temp_result = (base + adjustment) // (penalty + 1)
    final_shift = temp_result >> 1  # Right shift by 1 (divide by 2)
    
    # Apply case-specific correction using conditional expression
    final_shift = final_shift if final_shift > 0 else -final_shift
    
    return final_shift

# Execute main logic
intermediate_sum = sum(filtered_data)  # Distractor: computed but unused
size_flag = 'large' if len(filtered_data) >= 6 else 'small'

# Key statement
final_output = process_signals(filtered_data, threshold)

print(f"Result: {final_output}")