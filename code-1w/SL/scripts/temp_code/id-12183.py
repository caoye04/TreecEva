import itertools

def analyze_signal(samples, threshold=0.75):
    filtered = [s for s in samples if abs(s) > threshold]
    return len(filtered) > 0 and sum(1 for _ in enumerate(filtered)) % 2 == 1

def compute_entropy(data):
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
    probabilities = [count / len(data) for count in counts.values()]
    entropy = -sum(p * __import__('math').log2(p) for p in probabilities)
    return round(entropy, 4)

def validate_checksum(sequence):
    # Irrelevant checksum logic (dead path)
    total = 0
    for i, val in enumerate(sequence):
        total += val * (i + 1)
    return total % 17

def transform_readings(readings):
    # Distractor transformation with no impact on final result
    temp_log = []
    for idx, val in enumerate(readings):
        if idx % 3 == 0:
            temp_log.append(val ** 2)
        elif idx % 3 == 1:
            temp_log.append(val // 2)
        else:
            temp_log.append(abs(val - 10))
    return temp_log

def generate_pairs(values):
    # Use of itertools - relevant but indirect
    return list(itertools.combinations(values[:4], 2))

def evaluate_stability(metrics):
    baseline = metrics.get('baseline', 0)
    fluctuation = metrics.get('noise', 0)
    tolerance = metrics.get('tolerance_level', 5)
    
    if baseline < 0 or fluctuation > tolerance:
        return False
    
    score = baseline - fluctuation
    return score >= 2.5

def process_diagnostics(raw):
    # Complex nested logic with red herrings
    status_map = {0: 'idle', 1: 'active', 2: 'standby', 3: 'error'}
    codes = [raw[i] for i in range(0, len(raw), 2)]
    labels = [status_map.get(c % 4, 'unknown') for c in codes]
    
    counter = {label: 0 for label in status_map.values()}
    for label in labels:
        if label != 'unknown':
            counter[label] += 1
    
    # Decoy aggregation
    dummy_agg = sum(counter[k] * (i+1) for i, k in enumerate(counter))
    
    # Real signal: count of 'active'
    return counter['active']

def process_metrics(diagnostics, readings):
    # Key function with mixed concerns and distractions
    
    # Irrelevant preprocessing block
    normalized = []
    mean_val = sum(readings) / len(readings)
    for r in readings:
        norm = (r - mean_val) / (max(readings) - min(readings) + 1e-8)
        normalized.append(round(norm, 3))
    
    # Bit manipulation decoy
    magic_flag = 0
    for r in readings[:5]:
        magic_flag ^= (r << 1) & 0xF
        magic_flag |= (r >> 2) & 0x3
    
    # Dummy structure creation
    history = []
    for i, (a, b) in enumerate(zip(readings, readings[1:])):
        entry = {
            'index': i,
            'delta': b - a,
            'flagged': (a + b) % 7 == 0,
            'meta': {'level': i % 4}
        }
        history.append(entry)
    
    # Real computation begins here — deeply buried
    active_count = process_diagnostics(diagnostics)
    
    # Conditional branching based on unrelated analysis
    if analyze_signal(normalized, threshold=0.65):
        entropy = compute_entropy([int(x * 10) for x in normalized])
        if entropy > 1.0:
            active_count *= 2
    
    # Another misleading branch
    pairs = generate_pairs(readings)
    pair_sum = sum(a + b for a, b in pairs)
    if pair_sum > 100:
        active_count += 5  # red herring: never triggers due to data
    
    # Critical calculation
    adjustment_factor = 0
    for i, val in enumerate(readings):
        if i % 4 == 3 and val % 2 == 1:
            adjustment_factor += 1
    
    final_adjusted = active_count * 17 + adjustment_factor
    
    # Final irrelevant set operation
    unique_bases = set(r % 5 for r in readings)
    overflow_flag = any(b in [0, 4] for b in unique_bases)
    
    # This is the actual answer variable
    final_diagnostic = final_adjusted - 8
    
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# Main execution with realistic data
if __name__ == "__main__":
    diagnostics = [1, 8, 1, 6, 2, 9, 1, 5]
    readings = [12, 7, 3, 9, 4, 6, 8, 3, 11, 2]
    final_diagnostic = process_metrics(diagnostics, readings)