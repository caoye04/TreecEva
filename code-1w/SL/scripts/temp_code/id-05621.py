import itertools

# Simulated sensor and system diagnostic framework with heavy interference

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing path (dead code)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    return [x * 2 for x in filtered]  # Unused result

def evaluate_stability(profile):
    # Misleading stability metric (not used in final calculation)
    baseline = sum(profile) / len(profile)
    variance = sum((x - baseline) ** 2 for x in profile) / len(profile)
    return variance < 0.5

def extract_signature(sequence):
    # Real but obfuscated utility: computes product of prime-indexed elements
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    product = 1
    for idx, val in enumerate(sequence):
        if is_prime(idx):  # 2,3,5,7...
            product *= val
    return product

def compute_entropy(data):
    # Distractor function: calculates Shannon entropy (unused)
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return entropy

def generate_triplets(arr):
    # Creates overlapping triplets – used in red herring branch
    return list(itertools.combinations(arr, 3))

def detect_resonance(pattern):
    # Fake resonance check (never called)
    return sum(pattern[i] * pattern[-i-1] for i in range(len(pattern)//2)) > 100

def aggregate_anomalies(fragments, flags):
    # Core logic buried in noise
    temp_cache = []
    for fragment in fragments:
        # Extract every third element as signal candidate
        signal_candidates = fragment[::3]
        
        # Decoy branching based on unused flag
        if len(signal_candidates) > 5:
            smoothed = [sum(signal_candidates[i:i+3])/3 for i in range(len(signal_candidates)-2)]
        else:
            smoothed = [x + 1 for x in signal_candidates]  # Dead path
        
        # Actual relevant transformation
        shifted = [(x * 2) + 1 for x in signal_candidates]
        
        # Key operation: sum of squares of odd-positioned elements in shifted
        contribution = sum(shifted[i] ** 2 for i in range(1, len(shifted), 2))
        temp_cache.append(contribution)
    
    # Combine using bitwise interaction with system flags (only one matters)
    flag_influence = 0
    for f in flags:
        if f % 4 == 0 and f != 0:  # Only multiples of 4 (non-zero) contribute
            flag_influence ^= f  # XOR into influence
    
    # Final computation
    base_score = sum(temp_cache)
    adjustment = extract_signature([flag_influence, 12, 18, 24, 30, 36])  # Uses index 2,3,5 -> values: 18,24,36
    final_diagnostic = base_score - adjustment
    
    # Debugging decoys
    debug_info = {"raw": fragments, "flags_raw": flags, "temp": temp_cache}
    log_entry = f"Diag={final_diagnostic}"  # Unused
    
    return final_diagnostic

# Simulated input data
sensor_readings = [
    [1, 8, 3, 4, 9, 6, 7],
    [2, 5, 1, 8, 3, 4, 5],
    [3, 2, 7, 1, 8, 2, 9]
]

system_diagnostics = [10, 12, 15, 16, 20, 25, 27]  # Only 12,16,20 are multiples of 4

# Dead initialization - irrelevant variables
baseline_mesh = [[i*j for j in range(5)] for i in range(5)]
spectral_weights = list(itertools.accumulate([1, 2, 1, 3, 2]))
overlap_groups = generate_triplets([1, 2, 3, 4])

# Preprocessing call (result unused)
_ = preprocess_signal([1, 2, 3, 4, 5])

# Flag evaluation (partial use)
eval_flags = [f for f in system_diagnostics if f % 5 == 0]  # 10,15,20,25

# Main execution buried in middle of noise
final_diagnostic = aggregate_anomalies(sensor_readings, system_diagnostics)

# Output requirement
print(f"Result: {final_diagnostic}")