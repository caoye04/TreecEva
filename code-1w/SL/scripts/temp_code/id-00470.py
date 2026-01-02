def analyze_data(samples):
    # Irrelevant preprocessing
    cleaned = [x for x in samples if x > 0]
    stats = {"mean": sum(cleaned) / len(cleaned), "count": len(cleaned)}
    
    # Distractor: unused transformation
    transformed = [(i, val ** 0.5) for i, val in enumerate(samples) if val % 2 == 0]
    meta_log = {"version": "2.1", "status": "processed"}

    # Real logic starts: extract indices of large values
    large_indices = {i for i, x in enumerate(samples) if x > 50}

    # Misleading intermediate: looks important but unused later
    outlier_report = set()
    for i, x in enumerate(samples):
        if x > 90:
            outlier_report.add(f'crit_{i}')

    # Key data structure used later
    threshold_mask = {i for i in range(len(samples)) if i % 3 == 0}

    # Combine relevant sets
    core_set = large_indices & threshold_mask  # Only indices >50 and at multiples of 3

    # Dead code path - never called
    def debug_trace(s):
        return {k: v for k, v in enumerate(s) if v < 0}

    # Another red herring: complex but unused calculation
    peak_moments = []
    for i in range(1, len(samples)-1):
        if samples[i] > samples[i-1] and samples[i] > samples[i+1]:
            peak_moments.append((i, samples[i]))

    # Simulated metric collection (some fields irrelevant)
    metrics = {
        'amplitude': sum(samples),
        'rhythm': len([x for x in samples if x in {25, 50, 75}]),
        'coverage': len(core_set),
        'stability': samples[0] // 10 if samples else 0,
        'diversity': len(set(samples))
    }

    return metrics


def aggregate_metrics(logs):
    # Unused aggregation method
    totals = {}
    for log in logs:
        for k, v in log.items():
            totals[k] = totals.get(k, 0) + v
    return totals

def filter_noisy_readings(data, cutoff=10):
    # This function is defined but not used
    return [x for x in data if x > cutoff]

# Simulate sensor readings over time
sensor_readings = [
    5, 67, 12, 88, 34, 91, 23, 55, 7, 44,
    6, 73, 19, 82, 31, 95, 28, 61, 14, 50
]

# Extract key features (this call matters)
extracted_metrics = analyze_data(sensor_readings)

# Distractor variables
baseline_shift = sum(x for x in sensor_readings if x < 20)
calibration_factor = baseline_shift * 0.1

# Simulated reference set (partially overlaps with real logic)
reference_zones = {0, 3, 6, 9, 12, 15, 18}

# Build metric set using actual result
metric_set = extracted_metrics

# Add misleading field to metric_set
metric_set['ghost_metric'] = sum(1 for x in sensor_readings if x == 999)  # always 0

# Critical statement: this determines final answer
final_score = evaluate_performance(metric_set)

# Function definition comes *after* usage (tests parsing/ordering reasoning)
def evaluate_performance(metrics):
    # Simulated performance model
    score = 0
    
    # Relevant scoring components
    if 'coverage' in metrics:
        score += metrics['coverage'] * 10  # core contribution
    
    if 'rhythm' in metrics:
        score += metrics['rhythm'] * 5
    
    # Distractor: checks existence but adds nothing
    if 'ghost_metric' in metrics:
        # Looks important, but contributes zero
        pass
    
    # Bonus for diversity beyond threshold
    if 'diversity' in metrics and metrics['diversity'] > 15:
        score += 25
    
    # Decoy logic branch: appears significant but unused
    compliance_check = []
    for k in ['amplitude', 'stability']:
        if k in metrics:
            compliance_check.append(f'{k}_ok')
    
    # Final adjustment based on hidden rule
    hidden_modifier = 7 if metrics['coverage'] % 2 == 1 else -3
    score += hidden_modifier
    
    return score

# Print result as required
print(f"Target result: {final_score}")