from collections import Counter
def analyze_pattern(sequence):
    freq = Counter(sequence)
    modes = [k for k, v in freq.items() if v == max(freq.values())]
    return sorted(modes)[0] if len(modes) > 0 else 0

def normalize_values(data, factor=10):
    normalized = [round(x / factor, 2) for x in data]
    return [val for val in normalized if val > 0.5]

def calculate_performance(base, inputs):
    adjusted = [x * 1.5 for x in inputs if x >= base]
    processed = normalize_values(adjusted)
    if len(processed) == 0:
        return 0
    trend = sum(processed) / len(processed)
    raw_sequence = [int(x * 10) for x in processed]
    mode_value = analyze_pattern(raw_sequence)
    return round(trend * mode_value, 3)

# Simulate sensor data processing pipeline
baseline = 6
readings = [4, 7, 8, 6, 9, 7, 5]
dummy_var_x = "irrelevant string used briefly"
dummy_list = [1, 2, 3]
dummy_list.append(len(dummy_var_x))

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")