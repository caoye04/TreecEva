import itertools

# Simulated sensor data processing for a medical diagnostic system
def analyze_rhythm(sequence):
    if len(sequence) < 5:
        return False
    oscillations = 0
    for i in range(1, len(sequence)-1):
        if sequence[i-1] < sequence[i] > sequence[i+1] or sequence[i-1] > sequence[i] < sequence[i+1]:
            oscillations += 1
    return oscillations > 3

def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    normalized = [(x - mean_val) * 1.75 for x in signal]
    return [round(x, 3) for x in normalized]

def detect_spikes(data, threshold=2.5):
    spikes = []
    for i, val in enumerate(data):
        if abs(val) > threshold:
            spikes.append(i)
    return spikes if len(spikes) > 2 else []

def evaluate_stability(risk_profile, history):
    baseline = {'neural': 0.8, 'cardiac': 0.6, 'respiratory': 0.9}
    score = 0
    for key in baseline:
        if key in risk_profile:
            score += risk_profile[key] * baseline[key]
    # Irrelevant transformation
    temp_map = {i: history.count(i) for i in set(history)}
    adjustment = len(temp_map) * 0.1
    return score + adjustment

def compute_coherence(sequence):
    coherence_score = 0
    for a, b in itertools.pairwise(sequence):
        coherence_score += abs(a - b)
    inverse = 1 / (coherence_score + 1)
    # Dead computation - never used
    decoy_transform = [x ** 0.5 for x in sequence if x > 0]
    return round(coherence_score * inverse, 4)

def filter_artifacts(raw_readings):
    clean = []
    for val in raw_readings:
        if -5 <= val <= 5:
            clean.append(val)
    return clean

def generate_synthetic_controls(count):
    # Unused function - red herring
    return [0.1 * i % 1 for i in range(count)]

def integrate_subsystems(logs):
    # Complex but irrelevant aggregation
    stats = {}
    for entry in logs:
        for k, v in entry.items():
            if k not in stats:
                stats[k] = []
            stats[k].append(v)
    aggregates = {k: sum(v)/len(v) for k, v in stats.items()}
    return aggregates

def process_metrics(data, limits):
    # Core logic begins
    filtered = filter_artifacts(data['readings'])
    normed = normalize_signal(filtered[:12])  # Slice operation
    
    # Distractor block: unused analysis
    spike_indices = detect_spikes(normed, 3.0)
    rhythm_ok = analyze_rhythm(normed)
    
    # Relevant path
    coherence = compute_coherence(normed)
    stability = evaluate_stability(data['risk_factors'], spike_indices)
    
    # Set operations as per requirement
    unique_normed = set(round(x, 2) for x in normed)
    threshold_set = set(round(x, 2) for x in limits['values'])
    overlap = unique_normed & threshold_set  # Intersection
    penalty = len(threshold_set - unique_normed) * 0.05
    
    # Conditional expression with logical operations
    base_score = coherence if stability > 0.5 else coherence * 0.7
    adjusted_score = base_score - penalty if overlap else base_score + 0.1
    
    # Final computation
    if adjusted_score < 0:
        final_diagnostic = -int(abs(adjusted_score) * 1000)
    else:
        final_diagnostic = int(adjusted_score * 1000)
    
    # Critical print statement
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution data
health_data = {
    'readings': [0.3, -1.2, 4.5, 2.1, -3.3, 0.9, 1.8, -0.4, 2.7, 5.1, -2.2, 1.1, 0.8],
    'risk_factors': {
        'neural': 0.7,
        'cardiac': 0.85
    }
}

thresholds = {
    'values': [0.3, 1.1, 2.1, 2.7, 3.0, 4.5],
    'mode': 'strict'
}

# Dead code path - misleading initialization
logs = [
    {'cpu': 0.4, 'io': 120},
    {'cpu': 0.5, 'io': 140}
]
system_stats = integrate_subsystems(logs)  # Unused result

# Generate unused synthetic controls
synth_controls = generate_synthetic_controls(10)  # Red herring

# Key execution point
final_diagnostic = process_metrics(health_data, thresholds)