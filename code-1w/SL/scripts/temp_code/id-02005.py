import math

# Simulated sensor fusion system with diagnostic logic
def collect_sensor_data():
    raw_readings = [14, 7, 23, 5, 19, 31, 11]
    calibration_offset = 3
    adjusted = [r + calibration_offset for r in raw_readings]
    filtered = [x for x in adjusted if x > 10]
    return filtered

# Irrelevant auxiliary function - dead path
def deprecated_normalization(data):
    if not data:
        return []
    max_val = max(data)
    return [round(d / max_val, 3) for d in data]

# Unused transformation chain
transform_matrix = [[1, -1], [2, 0]]
def apply_transform(vec):
    return [vec[0]*transform_matrix[0][0] + vec[1]*transform_matrix[0][1],
            vec[0]*transform_matrix[1][0] + vec[1]*transform_matrix[1][1]]

# Decoy statistical analysis (never called)
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Signal classification heuristics
def classify_signal(val):
    if val < 15:
        return 'LOW'
    elif val < 25:
        return 'MEDIUM'
    else:
        return 'HIGH'

# Core pattern analyzer with distractors
system_flags = {'ACTIVE': True, 'DEBUG': False, 'VERBOSE': False}
temp_cache = set()

log_entries = []
def log_state(state):
    log_entries.append(state)

def analyze_pattern(signals, threshold):
    # Irrelevant pre-checks and red herrings
    if not signals:
        return -999
    
    # Distractor: complex but unused bitwise analysis
    bit_analysis = 0
    for s in signals[:3]:
        bit_analysis ^= (s << 2) & 0xFF
    
    # Real computation begins
    categorized = [classify_signal(s) for s in signals]
    category_set = set(categorized)
    
    # Conditional expression with side effect (distractor)
    _ = [temp_cache.add(cat) for cat in category_set] if system_flags['VERBOSE'] else None
    
    # Key filtering logic
    strong_signals = [s for s in signals if s >= threshold]
    
    # Distractor: unused nested structure
    summary_stats = {
        'count': len(signals),
        'unique_categories': len(category_set),
        'peak': max(signals),
        'energy': sum([s**2 for s in signals])
    }
    
    # Secondary filter based on position and value
    indexed_filtered = [(i, v) for i, v in enumerate(strong_signals) if i % 2 == 0]
    
    # Actual answer derivation through multiple steps
    base_score = sum(strong_signals)
    penalty = len([v for v in signals if v < 12]) * 2
    adjustment = len(category_set) * 3
    
    intermediate = base_score - penalty + adjustment
    
    # Final nonlinear transformation
    final_diagnostic = int((intermediate ** 0.5) * 10)
    
    # Dead code branch - never executed due to flag
    if system_flags['DEBUG']:
        log_state(f"Final: {final_diagnostic}")
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    collected_signals = collect_sensor_data()
    
    # Unused alternate processing path
    sorted_signals = sorted(collected_signals, reverse=True)
    reversed_original = collected_signals[::-1]
    
    # Primary control flow
    system_threshold = 18
    validation_check = any(x > 25 for x in collected_signals)
    
    # Critical statement
    final_diagnostic = analyze_pattern(collected_signals, system_threshold)
    
    # Output result
    print(f"Result: {final_diagnostic}")