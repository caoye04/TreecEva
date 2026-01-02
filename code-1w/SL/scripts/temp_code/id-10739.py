import itertools

# Simulated health monitoring system with diagnostic logic
def analyze_biomarkers(data_stream):
    filtered = [x for x in data_stream if 30 < x < 200]
    baseline = sum(filtered[:5]) / len(filtered[:5])
    deviation = sum(abs(baseline - x) for x in filtered)
    return deviation > 150, baseline

def compute_rolling_stat(values, window=3):
    if len(values) < window:
        return [0]
    rolling = [(values[i] + values[i+1] + values[i+2]) // window for i in range(len(values)-window+1)]
    noise_floor = max(rolling) * 0.1
    # Distractor: irrelevant transformation
    adjusted = [val - int(noise_floor) for val in rolling if val > noise_floor]
    return adjusted

def generate_phase_vector(sequence):
    # Complex but ultimately unused function (dead code path)
    paired = list(itertools.combinations(sequence, 2))
    products = [a * b for a, b in paired if (a + b) % 2 == 0]
    return [p % 17 for p in products]

def validate_coherence(signal):
    # Misleading intermediate calculation
    total_energy = sum(s**2 for s in signal)
    normalized = [s / (total_energy ** 0.5) for s in signal]
    coherence_score = sum(normalized[i] * normalized[i+1] for i in range(len(normalized)-1))
    return abs(coherence_score) > 0.8

def extract_signatures(raw_data):
    # Real processing branch
    segments = [raw_data[i:i+4] for i in range(0, len(raw_data), 4)]
    signatures = []
    for seg in segments:
        if len(seg) == 4:
            # Core logic: product of differences
            sig = (seg[0] - seg[1]) * (seg[2] - seg[3])
            signatures.append(abs(sig))
    # Decoy aggregation
    avg_sig = sum(signatures) / len(signatures) if signatures else 0
    return signatures, avg_sig

def process_metrics(indicators, config):
    # Main control flow
    anomalies = 0
    cumulative_weight = 0.0
    
    for idx, val in enumerate(indicators):
        if idx % 5 == 0:
            # Red herring: complex condition that never triggers due to data range
            if val > 999:
                anomalies += 1
                cumulative_weight += 0.3
        elif val < config['lower']:
            anomalies += 1
            cumulative_weight += 0.1
        elif val > config['upper']:
            anomalies += 1
            cumulative_weight += 0.2
    
    # Critical logic hidden among distractors
    temp_state = [x * 0.95 for x in indicators if x % 2 == 1]
    reduced = sum(temp_state) // 2  # Integer division and accumulation
    
    # Key computation
    final_risk = (anomalies * 100) + int(cumulative_weight * 10)
    adjustment = len([x for x in indicators if x > config['baseline']])
    final_diagnostic = final_risk - adjustment
    
    # Unused but plausible-looking debug trace
    debug_snapshot = {"risk": final_risk, "adjust": adjustment, "count": anomalies}
    return final_diagnostic

# Irrelevant auxiliary data
system_log = [101, 105, 103, 110, 102]
diagnostic_codes = ['ERR_207', 'WRN_405', 'INF_101']

# Primary data input
vital_readings = [88, 92, 95, 101, 103, 105, 108, 112, 115, 118, 120, 125, 130, 135, 140]

# Signal preprocessing (partially used)
processed_signal = compute_rolling_stat(vital_readings)
analyze_biomarkers(vital_readings)  # Called but result ignored

# Extract relevant features
signatures_list, mean_signature = extract_signatures(vital_readings)

# Configuration parameters
thresholds = {
    'lower': 90,
    'upper': 130,
    'baseline': 100
}

# Generate phase vector (unused but computed)
phase_pattern = generate_phase_vector([3, 6, 9, 12])

# Validate coherence (called with side effect)
validate_coherence(vital_readings)

# Final integration step — target execution point
health_indicators = vital_readings + signatures_list
final_diagnostic = process_metrics(health_indicators, thresholds)

# Output result
print(f"Result: {final_diagnostic}")