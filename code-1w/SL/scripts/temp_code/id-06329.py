import itertools

# Simulated sensor data processing with red herrings and distractions
def analyze_readings(raw):    # Irrelevant transformation (never used)    smoothed = [round((r + r*0.05) / 1.05, 3) for r in raw]    filtered = [x for x in raw if x > 0]    return sum(filtered[:len(filtered)//2])

def compute_checksum(data):    # Distractor function - looks important but unused    chk = 0    for i, d in enumerate(data):        chk ^= (d + i) % 256    return chk

def transform_sequence(seq):    # Unused recursive red herring    if len(seq) <= 1:        return seq    mid = len(seq) // 2    return transform_sequence(seq[mid:]) + transform_sequence(seq[:mid])

def extract_features(values):    # Another decoy operation with slicing and conditionals    a = values[::2]                # even indices    b = values[1::2]               # odd indices    c = [x for x in values if x % 3 == 0]    d = [x for x in values if x > sum(values)/len(values)]    return {'low': a, 'high': b, 'div3': c, 'above_avg': d}

def evaluate_performance(metrics, config):    # Core logic embedded in noise    base = 0    adjustment = 0    temp_results = []    
    # Real computation begins - heavily masked by irrelevant blocks
    for k, v in metrics.items():        if k.startswith('err'):            base -= v * config.get(k, 1.0)
        elif k.endswith('_rate') and v > 0:
            adjustment += v ** 0.5 * config.get(k, 0.5)
    
    # Critical calculation buried in middle
    raw_scores = [metrics['throughput'], metrics['accuracy'], metrics['stability']]
    normalized = [s / 100.0 for s in raw_scores]  # scale to [0,1]
    
    # Actual answer derivation
    product = 1.0
    for ns in normalized:
        product *= ns
    composite = (sum(normalized) / len(normalized)) * (product ** (1/3))
    
    # Distraction: complex-looking but unused bitwise mix
    magic = 0
    for i in range(3):
        magic |= int(normalized[i] * 100) << (i * 8)
    checksum_fake = (magic >> 16) ^ (magic & 0xFFFF)

    # More irrelevant code
    pairs = list(itertools.combinations_with_replacement(normalized, 2))
    avg_pair = sum(a * b for a, b in pairs) / len(pairs) if pairs else 0

    # Real final logic
    threshold_met = sum(1 for val in normalized if val >= config['min_threshold'])
    bonus = 10 if threshold_met == 3 else 5 if threshold_met == 2 else 0
    
    # Final score computation - this is what matters
    final_score = int((composite * 100) + adjustment - abs(base) + bonus)
    
    # Dead code path - never executed but looks plausible
    if final_score < 0:        final_score = 0    elif final_score > 200:        final_score = 200

    return final_score

# Main execution with multiple distractions
if __name__ == '__main__':
    # Sensor input (distraction)
    readings = [127, -50, 203, 188, -400, 97, 150]
    analysis_out = analyze_readings(readings)

    # Checksum of nothing useful
    fake_chk = compute_checksum([1, 2, 3, 4])

    # Meaningless feature extraction
    features = extract_features([6, 9, 12, 15, 18])

    # Transform unused sequence
    scrambled = transform_sequence([1, 1, 2, 3, 5, 8])

    # ACTUAL INPUT DATA FOR EVALUATION
    metric_data = {
        'throughput': 85,
        'accuracy': 92,
        'stability': 78,
        'error_count': 15,
        'recovery_rate': 0.64,
        'failover_rate': 0.33
    }

    thresholds = {
        'err_weight': 1.2,
        'recovery_rate': 0.8,
        'failover_rate': 0.4,
        'min_threshold': 0.80  # 80% normalized
    }

    # Key statement
    final_score = evaluate_performance(metric_data, thresholds)
    
    # Output result as required
    print(f"Target result: {final_score}")