import math

# Simulated sensor fusion system for environmental monitoring
def collect_data():
    raw_values = [i * 0.73 for i in range(15)]
    offset = 12.8
    calibrated = [v + offset for v in raw_values]
    return calibrated

# Irrelevant preprocessing: signal smoothing with unused method
def smooth_signal(data):
    smoothed = []
    for i in range(len(data)):
        if i == 0:
            smoothed.append(data[i])
        else:
            weighted = (data[i] * 0.6) + (data[i-1] * 0.4)
            smoothed.append(weighted)
    return smoothed  # Never used in main logic

# Distractor function: frequency analysis (not part of critical path)
def compute_frequencies(signal):
    freqs = {}
    for s in signal:
        bin_key = int(s // 5)
        freqs[bin_key] = freqs.get(bin_key, 0) + 1
    entropy = 0.0
    total = len(signal)
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log(p) if p > 0 else 0
    return entropy  # Computed but not used

# Core transformation: applies non-linear correction and filtering
def preprocess(readings):
    corrected = []
    threshold = 13.5
    scale_factor = 1.8
    for val in readings:
        if val < threshold:
            corrected.append(val ** 1.1)
        else:
            corrected.append(val * scale_factor)
    # Additional irrelevant adjustment
    normalized = [c / max(corrected) * 100 for c in corrected]  # Unused
    return corrected  # Only this matters

# Signal classification based on dynamic thresholds
def classify_signal(value, base_ref):
    ref = base_ref * 1.2 if value > base_ref else base_ref * 0.9
    deviation = abs(value - ref)
    if deviation < 2.0:
        return 'stable'
    elif deviation < 5.0:
        return 'fluctuating'
    else:
        return 'unstable'

# Data enrichment with red herring fields
def enrich_with_metadata(analyzed):
    records = []
    for idx, item in enumerate(analyzed):
        # Real data needed downstream
        status = classify_signal(item['value'], item['baseline'])
        
        # Excessive metadata (only 'status' and 'adjusted' are relevant)
        record = {
            'id': f"SR-{idx:03}",
            'timestamp': f"2023-07-15T12:{idx:02}:00",
            'value': item['value'],
            'baseline': item['baseline'],
            'adjusted': item['value'] - item['baseline'],
            'status': status,
            'source': 'sensor_array_A',
            'version': 'v2.1',
            'checksum': (idx + len(str(item['value'])) * 3) % 7  # Dead field
        }
        records.append(record)
    return records

# Main processing pipeline
raw_input = collect_data()

# Dead branch: alternative processing (never executed due to flag)
use_alternative = False
if use_alternative:
    processed_input = [x * 2 for x in raw_input]  # Unused
else:
    temp_processed = preprocess(raw_input)

# Transform into structured format for analysis
structured_data = [{'value': temp_processed[i], 'baseline': 14.0 + (i % 3)} for i in range(len(temp_processed))]

# Enrichment step (some fields used, others ignored)
enriched_data = enrich_with_metadata(structured_data)

# Filtering out entries — only 'fluctuating' and 'unstable' kept
filtered_statuses = ['fluctuating', 'unstable']
filtered_entries = [e for e in enriched_data if e['status'] in filtered_statuses]

# Secondary filtering: remove low-adjusted values (irrelevant filter, not applied later)
high_adjustment = [f for f in filtered_entries if abs(f['adjusted']) > 1.5]  # Computed but unused

# Extract relevant values for diagnostic scoring
relevant_values = [entry['adjusted'] for entry in filtered_entries]

# Diagnostic engine with conditional expression and combinatorics
def analyze_readings(values):
    n = len(values)
    if n == 0:
        return 0.0
    
    # Calculate weighted impact: alternating signs based on index parity
    weighted_sum = sum(v * (-1)**i for i, v in enumerate(values))
    
    # Apply decay factor only if more than 5 readings (true here)
    decay_factor = 0.95 ** n if n > 5 else 1.0
    
    # Conditional transformation using Python idiom
    base_score = weighted_sum * decay_factor
    
    # Final nonlinear calibration
    final_score = base_score ** 2 / (1 + abs(base_score) * 0.1)
    
    # Red herring computation: combinatorial penalty (unused)
    penalty = 0
    for i in range(n):
        for j in range(i+1, n):
            if values[i] * values[j] < 0:  # opposite signs
                penalty += 1
    effective_penalty = penalty / (n * (n-1) / 2) if n > 1 else 0  # Not applied
    
    return final_score

# Critical execution point
final_diagnostic = analyze_readings(relevant_values)

# Print result as required
print(f"Target result: {final_diagnostic}")