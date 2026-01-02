import itertools

# Simulated sensor data processing with diagnostic analysis
raw_readings = [14, -5, 23, 18, -7, 42, 31, -22, 19, 8]

def apply_noise_filter(data):
    # Real preprocessing step: remove negative values (noise)
    filtered = [x for x in data if x > 0]
    return filtered

def compute_trend_score(seq):
    # Meaningful metric: sum of pairwise differences
    score = 0
    for i in range(1, len(seq)):
        score += seq[i] - seq[i-1]
    return score

def generate_combinations(arr):
    # Distractor function: generates unused combinations
    combos = []
    for r in range(2, 4):
        combos.extend(list(itertools.combinations(arr, r)))
    # This result is never used
    dummy_usage = len(combos) > 10
    return combos  # Dead end

def calculate_entropy(values):
    # Distractor: looks sophisticated but unused
    import math
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def extract_peaks(series):
    # Unused feature extraction
    peaks = []
    for i in range(1, len(series)-1):
        if series[i-1] < series[i] > series[i+1]:
            peaks.append(series[i])
    return peaks  # Computed but not used

def rolling_average(window_data, size=3):
    # Another distractor transformation
    avgs = []
    for i in range(len(window_data) - size + 1):
        avgs.append(sum(window_data[i:i+size]) / size)
    return avgs  # Calculated later but irrelevant

def normalize_dataset(entries):
    # Red herring normalization
    min_val, max_val = min(entries), max(entries)
    if min_val == max_val:
        return [0.5] * len(entries)
    return [(x - min_val) / (max_val - min_val) for x in entries]

def analyze_signal(clean_data):
    # Core logic begins
    baseline = sum(clean_data) // len(clean_data)
    
    # Transform using cumulative effects
    cum_effects = []
    accumulator = 0
    for val in clean_data:
        accumulator += val - baseline
        cum_effects.append(abs(accumulator))
    
    # Key summation over effect magnitudes
    total_deviation = sum(cum_effects)
    
    # Apply conditional amplification based on pattern
    trigger_count = 0
    for i in range(1, len(clean_data)):
        if clean_data[i] > clean_data[i-1] and clean_data[i] % 2 == 0:
            trigger_count += 1
    
    # Final diagnostic depends on both deviation and triggers
    if trigger_count >= 3:
        final_score = total_deviation * 2 + trigger_count
    else:
        final_score = total_deviation + trigger_count * 5
    
    return final_score

# Main execution flow
filtered_samples = apply_noise_filter(raw_readings)

# Distracting computations - appear important but don't affect outcome
all_combinations = generate_combinations(filtered_samples)
signal_entropy = calculate_entropy(filtered_samples)
peak_values = extract_peaks(filtered_samples)
moving_averages = rolling_average(filtered_samples, 3)
normalized_set = normalize_dataset(filtered_samples)

# Additional red herring: complex itertools usage
pairwise_diffs = [abs(a - b) for a, b in itertools.pairwise(filtered_samples)]
accumulated_pairs = list(itertools.accumulate(pairwise_diffs, lambda x, y: x + y//2))
threshold_flags = [1 if x > 10 else 0 for x in accumulated_pairs]
flag_summation = sum(threshold_flags)  # Looks useful, isn't

# Actual critical path
processed_samples = [x * 2 for x in filtered_samples if x > 15]  # Further processing

# Introduce another decoy variable
weighted_total = 0
weights = itertools.cycle([0.8, 1.2, 1.0])
for val in processed_samples:
    weight = next(weights)
    weighted_total += val * weight
# Not used beyond this point

# Key statement
final_diagnostic = analyze_signal(processed_samples)

print(f"Result: {final_diagnostic}")