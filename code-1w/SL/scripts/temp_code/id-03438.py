import math

# Simulated sensor fusion system for environmental monitoring
def acquire_data():
    raw_entries = [127, 255, 192, 64, 224, 32, 160, 96]
    scaling_factor = 0.75
    adjusted = [x * scaling_factor for x in raw_entries]
    return adjusted

# Irrelevant preprocessing - distractor
def normalize_dataset(data):
    mean_val = sum(data) / len(data)
    normalized = [x - mean_val for x in data]
    squared_devs = [(x - mean_val)**2 for x in data]
    variance = sum(squared_devs) / len(squared_devs)
    stdev = math.sqrt(variance)
    return [x / stdev for x in normalized] if stdev != 0 else normalized

# Bit manipulation for noise filtering (RELEVANT)
def filter_noise(value):
    masked = value & 255
    rotated = ((masked << 3) | (masked >> 5)) & 255
    return rotated ^ 85  # XOR scramble for error detection

# Signal classification heuristic (distractor)
class SignalClassifier:
    def __init__(self):
        self.thresholds = {'low': 50, 'high': 200}

    def classify(self, x):
        if x < self.thresholds['low']:
            return 'L'
        elif x > self.thresholds['high']:
            return 'H'
        else:
            return 'M'

# Real signal processor (RELEVANT)
def process_signal(x):
    if x <= 0:
        return 0
    log_component = math.log(x) if x > 1 else 0
    trig_component = math.sin(x / 10) * 10
    combined = log_component + trig_component
    if combined > 15:
        return 15
    return round(combined, 4)

# Higher-order function with lambda - required feature
apply_correction = lambda f, val: f(val) + 0.1 if val > 10 else f(val)

# Main processing chain
def process_signals(raw_list):
    temp_results = []
    classifier = SignalClassifier()  # Unused object - red herring

    for reading in raw_list:
        # Distractor branch
        category = classifier.classify(reading)
        if category == 'H':
            adjusted = reading * 0.9
        elif category == 'M':
            adjusted = reading * 1.05
        else:
            adjusted = reading

        # Relevant path
        filtered = filter_noise(int(reading))
        processed = process_signal(filtered)
        corrected = apply_correction(lambda x: x * 0.8, processed)  # Uses lambda
        temp_results.append(corrected)

    return temp_results

# Aggregation logic
summarize_diagnostics = lambda data: {
    'count': len(data),
    'total': sum(data),
    'max': max(data),
    'min': min(data)
}

# Irrelevant statistical analysis - dead code path
def compute_entropy(data):
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

# Core analysis function (RELEVANT)
def analyze_readings(signal_list):
    cumulative_score = 0
    weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.05, 0.08, 0.07]
    
    for i, val in enumerate(signal_list):
        weighted_contribution = val * weights[i % len(weights)]
        cumulative_score += weighted_contribution
        
        # Early termination red herring
        if cumulative_score > 100:
            break
        
        # Additional transformation
        if i % 3 == 0:
            cumulative_score = math.ceil(cumulative_score)

    # Final adjustment using modular arithmetic
    final_mod = int((cumulative_score * 1000) % 97)
    return final_mod * 2

# Unused data structure - distraction
diagnostic_log = {
    'timestamps': [],
    'errors': set(),
    'history': []
}

# Execution flow
data_acquired = acquire_data()
signals_normalized = normalize_dataset(data_acquired)  # Computed but not used
processed_signals = process_signals(data_acquired)
diagnostic_summary = summarize_diagnostics(processed_signals)  # Stored but irrelevant
entropy_value = compute_entropy(processed_signals)  # Dead computation

# Key execution point
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")