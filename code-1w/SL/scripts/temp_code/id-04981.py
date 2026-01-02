from itertools import groupby, cycle
import math

# Simulated system telemetry data
telemetry_stream = [104, 95, 110, 90, 120, 80, 130, 70, 140, 60]

# Irrelevant signal processing chain (distractor)
def process_signal(data):
    filtered = [x for x in data if x > 85]
    smoothed = []
    for i in range(len(filtered)):
        window = filtered[max(0, i-2):i+1]
        smoothed.append(sum(window) / len(window))
    return [round(x, 1) for x in smoothed]

# Unused feature extraction (dead code path)
def extract_features(signal):
    peaks = [i for i in range(1, len(signal)-1) if signal[i] > signal[i-1] and signal[i] > signal[i+1]]
    troughs = [i for i in range(1, len(signal)-1) if signal[i] < signal[i-1] and signal[i] < signal[i+1]]
    return {'peaks': peaks, 'troughs': troughs, 'amplitude': len(peaks) - len(troughs)}

# Misleading diagnostic function (decoy)
def run_diagnostics(data):
    checksum = sum(data) * 0.95
    threshold = 100
    status_flags = []
    for val in data:
        if val > threshold:
            status_flags.append(1)
        else:
            status_flags.append(0)
    # This function looks important but is never used
    return {'checksum': checksum, 'alerts': sum(status_flags)}

# Core analysis logic (relevant)
def evaluate_stability(ratios):
    stable_count = 0
    for r in ratios:
        if 0.9 <= r <= 1.1:
            stable_count += 1
    return stable_count

# Primary transformation chain
raw_metrics = [telemetry_stream[i+1]/telemetry_stream[i] for i in range(len(telemetry_stream)-1)]

# Apply non-uniform scaling (red herring)
scaled_metrics = []
scaling_cycle = cycle([1.1, 0.9, 1.05])
for m in raw_metrics:
    scale = next(scaling_cycle)
    scaled_metrics.append(m * scale)

# Distractor: complex grouping with irrelevant statistics
grouped_data = []
sorted_metrics = sorted(scaled_metrics)
for key, group in groupby(sorted_metrics, key=lambda x: int(x)):
    items = list(group)
    if len(items) > 1:
        variance = sum((x - sum(items)/len(items))**2 for x in items) / len(items)
        grouped_data.append({'range': key, 'count': len(items), 'variance': round(variance, 3)})

# Another decoy function that's defined but not used
def calculate_robustness(measurements):
    trimmed = measurements[1:-1]  # Remove outliers
    geometric_mean = math.exp(sum(math.log(x) for x in trimmed) / len(trimmed))
    return geometric_mean * 0.87

# Real work happens here: filter and transform
filtered_ratios = [r for r in raw_metrics if r != 1.0]  # Use raw, not scaled
inverted_ratios = [1/r for r in filtered_ratios]
combined_ratios = [a * b for a, b in zip(filtered_ratios, inverted_ratios[:len(filtered_ratios)])]

# Baseline thresholds (key reference)
baseline = {
    'target_ratio': 1.0,
    'tolerance': 0.15,
    'penalty_factor': 0.7
}

# Central analysis function
def analyze_performance(ratios, config):
    # Step 1: Count deviations beyond tolerance
    deviations = [abs(r - config['target_ratio']) for r in ratios]
    significant_devs = [d for d in deviations if d > config['tolerance']]
    
    # Step 2: Calculate weighted instability score
    raw_score = len(significant_devs) * 10
    
    # Step 3: Apply penalty cascade
    if raw_score > 30:
        raw_score *= config['penalty_factor']
    elif raw_score > 20:
        raw_score *= 0.85
    
    # Step 4: Normalize by data length
    normalized = raw_score / len(ratios)
    
    # Step 5: Apply ceiling and floor
    normalized = max(5, min(normalized, 50))
    
    # Step 6: Add stability bonus (only if conditions met)
    stability_check = evaluate_stability(ratios)
    if stability_check > 3:
        normalized -= 3  # Bonus for stability
    
    # Step 7: Final adjustment using bit manipulation (obscure but deterministic)
    temp = int(normalized * 100)
    temp = temp ^ 0b1101  # XOR with arbitrary pattern
    temp = (temp >> 2) & 0b111111111  # Right shift and mask
    final_value = temp / 100.0
    
    # Step 8: Round to nearest 0.5 increment
    final_value = round(final_value * 2) / 2
    
    return final_value

# Execute main analysis
final_score = analyze_performance(raw_metrics, baseline)

# Print result as required
print(f"Result: {final_score}")