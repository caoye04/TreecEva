from collections import defaultdict, Counter
import math

# Simulated sensor data from a health monitoring system
def generate_telemetry():
    return [58 + (i * 3) % 17 for i in range(12)]

def analyze_rhythm(pattern):
    # Irrelevant analysis function (dead code path)
    rhythm_score = 0
    for val in pattern:
        if val % 5 == 0:
            rhythm_score += 2
        elif val % 3 == 0:
            rhythm_score += 1
    return rhythm_score

def compute_entropy(values):
    freqs = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def filter_outliers(data, limit=75):
    # Misleading filtering: looks important but not used in final calculation
    return [x for x in data if x <= limit]

def derive_keypoints(seq):
    # Decoy transformation with intermediate distraction
    offset = sum(seq) // len(seq)
    transformed = [(x - offset) ** 2 for x in seq]
    return transformed[:5]

def evaluate_stability(readings):
    # Complex-looking but irrelevant stability metric
    stable_count = 0
    for i in range(1, len(readings)):
        if abs(readings[i] - readings[i-1]) < 5:
            stable_count += 1
    return stable_count > len(readings) * 0.6

def aggregate_diagnostics(logs):
    # Unused aggregation path (red herring)
    stats = defaultdict(int)
    for entry in logs:
        stats['total'] += entry
        if entry > 60:
            stats['elevated'] += 1
    return dict(stats)

def process_metrics(data, config):
    # Core logic embedded within distractions
    base = [x for x in data if x > 50]  # Filter relevant readings
    shift = config['tolerance'] * 2
    adjusted = [((x + shift) // 3) % 25 for x in base]
    
    # Real computation chain starts here
    temp_hash = 0
    for i, val in enumerate(adjusted):
        temp_hash += (val * (i + 1)) ^ (val % 7)
    
    # Critical calculation: bitwise mix with modular reduction
    interim = (temp_hash ^ config['signature']) % 10000
    result = (interim * 3) + (interim // 7)  # Final transform
    
    # Distractor: unused conditional branch
    if result < 500:
        fallback = sum(adjusted) * config['tolerance']
        result = fallback if fallback > result else result
    
    return result

# Main execution flow
if __name__ == '__main__':
    raw_signal = generate_telemetry()
    
    # Irrelevant preprocessing steps (distractors)
    entropy_metric = compute_entropy(raw_signal)
    outliers_filtered = filter_outliers(raw_signal)
    keypoints = derive_keypoints(raw_signal)
    rhythm_analysis = analyze_rhythm(raw_signal)
    stability_flag = evaluate_stability(raw_signal)
    
    # Data structures with cross-references (misleading complexity)
    audit_trail = []
    audit_trail.append({'stage': 'initial', 'size': len(raw_signal)})
    audit_trail.append({'stage': 'filtered', 'size': len(outliers_filtered)})
    
    # Real input construction (camouflaged among distractors)
    health_data = [x + 2 for x in raw_signal]  # Key data modification
    
    # Configuration with decoy fields
    thresholds = {
        'threshold_low': 50,
        'threshold_high': 85,
        'tolerance': 11,  # Used in core logic
        'hysteresis': 5,
        'signature': 682,  # Used in core logic
        'decay_rate': 0.8
    }
    
    # Unused diagnostic calls (dead paths)
    diagnostics_log = aggregate_diagnostics(health_data)
    rhythm_score = analyze_rhythm(keypoints)
    
    # Critical execution point
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")