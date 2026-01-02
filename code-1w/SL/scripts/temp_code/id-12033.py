def analyze_pattern(seq):
    return sum(ord(c) for c in seq if c.isupper())

# Irrelevant helper function (dead code path)
def deprecated_normalization(x):
    return (x - min(x)) / (max(x) - min(x) + 1e-8)

# Unused complex structure
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size

    def reset(self):
        self.buffer = [0] * self.size

# Misleading transformation chain
def transform_signal(signal_str):
    temp = signal_str[::-1].lower()
    temp = temp.replace('a', '9').replace('e', '8').replace('i', '7')
    return ''.join(sorted(temp))

# Decoy statistical analysis
irrelevant_stats = {
    'baseline': 42,
    'tolerance': 0.05,
    'iterations': 1500,
    'convergence': False
}

# Unused bitwise diagnostic
flag_mask = 0b10101010
override_flag = (flag_mask << 3) & 0xFF

# Real computation begins here
health_data = {
    'vital_a': [65, 70, 72, 68, 71],
    'vital_b': [120, 118, 125, 119, 123],
    'vital_c': [80, 82, 78, 85, 81]
}

thresholds = {
    'vital_a': (60, 75),
    'vital_b': (115, 130),
    'vital_c': (75, 90)
}

# Complex distractor: nested dictionary traversal with filtering
diagnostics = {}
for key, readings in health_data.items():
    above_threshold = [r for r in readings if r > thresholds[key][1]]
    below_threshold = [r for r in readings if r < thresholds[key][0]]
    normal_range = [r for r in readings if thresholds[key][0] <= r <= thresholds[key][1]]
    
    # Store intermediate stats (some irrelevant)
    diagnostics[key] = {
        'count_above': len(above_threshold),
        'count_below': len(below_threshold),
        'stdev': sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings),
        'trend': 'stable',
        'anomalies': len(above_threshold) + len(below_threshold)
    }

# More red herrings
compression_factor = 3.14159
encoded_tag = "X9yZqP"
analysis_signature = analyze_pattern(encoded_tag)  # Returns 233

# Fake data fusion step
fused_metric = 0
for i, char in enumerate(transform_signal("HealthSync")):
    fused_metric += ord(char) * (i + 1)

# Actual core logic buried in distractions
def validate_readings(data_dict, bounds):
    score = 0
    penalty = 0
    for k, values in data_dict.items():
        low, high = bounds[k]
        for v in values:
            if v < low:
                penalty += (low - v) * 1.5
            elif v > high:
                penalty += (v - high) * 1.2
    return max(0, 100 - penalty)

# Secondary processing with string analysis
def extract_quality_code(text):
    count_upper = sum(1 for c in text if c.isupper())
    count_digit = sum(1 for c in text if c.isdigit())
    return count_upper * count_digit

quality_bonus = extract_quality_code("H3alT7hM0nit0r")  # 5 * 4 = 20

# Main processing function
def process_metrics(data, limits):
    base_score = validate_readings(data, limits)
    
    # Hidden adjustment using dictionary operation
    adjustments = {k: len(v) for k, v in data.items()}
    total_length = sum(adjustments.values())  # 15
    
    # Critical calculation step
    raw_final = base_score + quality_bonus
    
    # Apply subtle correction based on character count logic
    tag = "DIAGNOSTIC"
    char_count = len([c for c in tag if c in 'AEIOU'])  # 4 vowels
    corrected = raw_final - char_count
    
    # Final override (this is the true answer)
    final_value = int(corrected)  # 100 - 24 + 20 - 4 = 92?
    
    # But wait — one more hidden rule
    if total_length > 10 and analysis_signature > 200:
        final_value += 5
    
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")