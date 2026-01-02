from collections import Counter

def analyze_pattern(sequence):
    count = Counter(sequence)
    most_common_val = count.most_common(1)[0][1]
    return most_common_val

def calculate_threshold(data, factor):
    length = len(data)
    offset = data.find('1')
    combined_key = length ^ offset
    if combined_key % 2 == 0:
        result = factor + (combined_key * 3)
    else:
        result = factor - (combined_key // 2)
    return result

# Simulate sensor pattern (irrelevant string for context)
sensor_log = 'SYS_OK:11011001:ACTIVE'
signal_data = '1011001'
base_factor = 17

# Key computation step
energy_threshold = calculate_threshold(signal_data, base_factor)

# Additional analysis (distractor but plausible)
pattern_score = analyze_pattern(signal_data)

# Final output
print(f"Result: {energy_threshold}")