def analyze_signal(pattern, threshold=0.5):
    """Irrelevant signal processing function (red herring)"""
    if len(pattern) < 5:
        return False
    peak = max(pattern)
    normalized = [p / peak for p in pattern]
    crossings = sum(1 for i in range(1, len(normalized)) if normalized[i-1] < threshold <= normalized[i])
    return crossings > 2


def calculate_entropy(sequence):
    """Distractor: computes entropy but not used in final result"""
    from math import log2
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = 0.0
    for count in freq.values():
        prob = count / total
        entropy -= prob * log2(prob)
    return entropy

# Irrelevant data structures (distractors)
raw_readings = [0.8, 0.92, 0.75, 0.68, 0.91, 0.43, 0.88]
signal_valid = analyze_signal(raw_readings, 0.6)

# Unused transformation chain (dead path)
data_buffer = [x ** 2 for x in raw_readings if x > 0.7]
filtered_stream = list(map(lambda v: v * 1.1, data_buffer))
buffer_entropy = calculate_entropy([int(x*10) for x in filtered_stream])

# Real computation begins here — deeply nested and obscured
base_threshold = 75

operation_log = [
    {'op': 'INIT', 'val': 100},
    {'op': 'DECAY', 'val': 12},
    {'op': 'BOOST', 'val': 8},
    {'op': 'DECAY', 'val': 5}
]

status_flags = {
    'active': True,
    'debug_mode': False,
    'locked': False
}

# Simulate system state transitions (mixed with irrelevant flags)
current_state = 90
for entry in operation_log:
    if entry['op'] == 'DECAY':
        current_state -= entry['val'] * 0.8
    elif entry['op'] == 'BOOST':
        current_state += entry['val'] * 1.5

# Introduce decoy variables that look important
system_health = current_state > 80
performance_index = (current_state + buffer_entropy * 10) if system_health else 0  # misleading!

# Core logic hidden in conditional expression with slicing distraction
recent_metrics = [85, 76, 92, 88, 73, 81, 90, 87, 79, 84]
metric_slice = recent_metrics[2:8:2]  # [92, 81, 87] -> indexes 2,4,6

adjusted_values = []
for val in metric_slice:
    if val >= base_threshold:
        adjusted_values.append(val * 0.95)
    else:
        adjusted_values.append(val * 1.05)

summed_adjusted = sum(adjusted_values)

# Another red herring: complex but unused calculation
historical_avg = sum(recent_metrics[-5:]) / 5
volatility = max(recent_metrics[-5:]) - min(recent_metrics[-5:])
penalty_factor = 0.9 if volatility > 8 else 1.0

# Destructuring that looks critical but only partially used
primary, secondary, tertiary = (summed_adjusted, historical_avg * 0.85, volatility * 2)

# Final evaluation uses only 'primary', others are distractions
def evaluate_performance(data_input, threshold):
    """Main scoring logic buried in function"""
    temp_state = primary  # captures summed_adjusted
    if temp_state >= threshold * 1.2:
        temp_state *= 1.1
    elif temp_state < threshold:
        temp_state *= 0.9
    else:
        temp_state += 5  # base case
    
    # Bit manipulation decoy
    binary_offset = (temp_state * 100) % 256
    masked = int(binary_offset) ^ 0b101010
    final_part = temp_state + (masked & 1)  # adds 0 or 1 depending on XOR
    
    return int(final_part)

# Key execution point
final_score = evaluate_performance(metric_slice, base_threshold)

# Print required output
print(f"Target result: {final_score}")