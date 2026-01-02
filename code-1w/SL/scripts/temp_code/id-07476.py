from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic logic
def collect_raw_data():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8]

def filter_outliers(data, threshold=2):
    avg = sum(data) / len(data)
    return [x for x in data if abs(x - avg) <= threshold]

def map_to_categories(values):
    category_map = defaultdict(int)
    for v in values:
        if v < 3:
            category_map['low'] += 1
        elif v < 7:
            category_map['medium'] += 1
        else:
            category_map['high'] += 1
    return category_map

def generate_frequency_profile(seq):
    # Irrelevant function - simulates signal harmonics but not used in final result
    profile = []
    for i in range(1, 6):
        harmonic = sum(math.sin(x * i) for x in seq[:10])
        profile.append(round(harmonic, 3))
    return profile

def extract_peaks(series, min_magnitude=7):
    # Dead code path - never called
    return [i for i, x in enumerate(series) if x >= min_magnitude]

def amplify_signal(x):
    # Unused transformation
    return x * 2 + (x % 3)

def compute_entropy(counts):
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def rolling_window_avg(data, window_size=3):
    # Misleading intermediate: looks important but unused
    averages = []
    for i in range(len(data) - window_size + 1):
        averages.append(sum(data[i:i+window_size]) / window_size)
    return [round(x, 2) for x in averages]

def validate_coherence(signal):
    # Distractor function: checks internal consistency but doesn't affect output
    sorted_signal = sorted(signal)
    inversions = 0
    for i in range(len(sorted_signal) - 1):
        if sorted_signal[i] == sorted_signal[i+1]:
            inversions += 1
    return inversions < 5

def normalize_readings(raw):
    min_val, max_val = min(raw), max(raw)
    if max_val == min_val:
        return raw
    return [(x - min_val) / (max_val - min_val) for x in raw]

def discretize(normalized):
    return [int(x * 9) + 1 for x in normalized]  # Scale to 1-10 range

def group_transitions(clean_seq):
    transitions = defaultdict(int)
    for a, b in zip(clean_seq, clean_seq[1:]):
        transitions[(a, b)] += 1
    return transitions

def detect_anomalies(counts):
    # Complex but irrelevant anomaly detector
    anomalies = []
    for (prev, curr), cnt in counts.items():
        if abs(curr - prev) > 6 and cnt == 1:
            anomalies.append((prev, curr))
    return anomalies

def calculate_risk_score(transitions):
    # Decoy metric
    score = 0
    for (a, b), count in transitions.items():
        if a >= 8 and b <= 2:
            score += count * 10
    return score

def aggregate_diagnostics(cat_counts, entropy_val):
    base = cat_counts['high'] * 100
    penalty = cat_counts['low'] * 10
    adjusted = base - penalty + int(entropy_val * 50)
    return max(adjusted, 0)

def analyze_readings(categories):
    entropy = compute_entropy(categories)
    risk_factor = 0
    
    # Simulate multi-path decision logic with red herring branches
    if categories['high'] > 4:
        if categories['low'] < 3:
            risk_factor = 2
        elif categories['medium'] % 2 == 0:
            risk_factor = 1
        else:
            risk_factor = 3
    else:
        if entropy > 1.0:
            risk_factor = 1
        else:
            risk_factor = 0
    
    # Core computation buried in distractions
    diagnostic_code = 800
    diagnostic_code += categories['high'] * 10
    diagnostic_code -= categories['low'] * 5
    diagnostic_code += risk_factor * 7
    
    # Final adjustment based on hidden pattern
    if categories['medium'] in [5, 6]:
        diagnostic_code += 1
    
    return diagnostic_code

# Main execution flow
raw_sensor_data = collect_raw_data()  # Initial dataset
filtered_data = filter_outliers(raw_sensor_data, threshold=2.5)
categorized = map_to_categories(filtered_data)

# Irrelevant transformations (distractors)
normalized_values = normalize_readings(raw_sensor_data)
discretized_signal = discretize(normalized_values)
window_averages = rolling_window_avg(discretized_signal, 4)
frequency_analysis = generate_frequency_profile(discretized_signal)
data_valid = validate_coherence(filtered_data)

# Transition analysis (misleading intermediate)
transitions = group_transitions(filtered_data)
anomalous_jumps = detect_anomalies(transitions)
risk_score = calculate_risk_score(transitions)

# Real signal processing chain
entropy_measure = compute_entropy(categorized)
final_diagnostic = analyze_readings(categorized)

# Output target result
print(f"Target result: {final_diagnostic}")