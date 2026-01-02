from collections import defaultdict, Counter
import math

# Simulated sensor array diagnostics with red herrings
def analyze_redundancy_pattern(sequence):
    if len(sequence) < 3:
        return False
    redundant_count = 0
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            redundant_count += 1
    return redundant_count > 2

def compute_entropy(data):
    """Misleading function - not actually used in final calculation"""
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_phase_shift(signal):
    """Dead code path - never invoked"""
    shifted = []
    for i, val in enumerate(signal):
        shifted.append(val * math.sin(i * math.pi / 4))
    return shifted

def validate_checksum(buffer):
    # Distractor: looks important but unused
    checksum = 0
    for b in buffer:
        checksum ^= b
    return checksum == 0xFF

# Core logic disguised among irrelevant utilities
def extract_critical_path(traces):
    magnitude = 0
    for t in traces:
        if t > 0 and t % 2 == 0:
            magnitude += int(math.log2(t) + 1)
    return magnitude

def evaluate_stability_index(readings):
    index = 0
    temp_store = defaultdict(int)
    for i, val in enumerate(readings):
        temp_store[i % 4] += val
        if val > 50:
            index += 1
        elif val < 10:
            index -= 1
    # Real contribution to answer
    return sum(temp_store.values()) // len(readings)

def derive_invariant(signal):
    # This is a decoy invariant calculation
    xor_sum = 0
    for s in signal:
        xor_sum ^= int(s)
    return xor_sum % 17

def process_metrics(signature, baseline):
    # Key computation interwoven with noise
    stage_a = [x for x in signature if x > 25]
    stage_b = [y for y in stage_a if y < 75]
    
    # Irrelevant transformation
    phantom_map = {i: math.exp(i/10) for i in range(len(baseline)) if baseline[i] % 3 == 0}
    
    # Real processing begins
    accumulator = defaultdict(float)
    for i, val in enumerate(baseline):
        accumulator[i % 5] += (val * 1.5) if i % 2 else (val * 0.8)
    
    # Secondary filter chain
    filtered_sig = list(filter(lambda x: x % 7 != 0, stage_b))
    
    # Meaningful aggregation
    aggregate = sum(accumulator.values())
    signal_strength = sum(filtered_sig)
    
    # Final derivation using correct path
    raw_diagnostic = (aggregate * 0.7) + (signal_strength * 0.3)
    
    # Dead branch - looks like it affects outcome
    if raw_diagnostic > 1000:
        adjustment_factor = math.tanh(raw_diagnostic / 1000)
        raw_diagnostic *= adjustment_factor
    
    # This is the true final step
    final_diagnostic = int(round(raw_diagnostic / 10) * 2)
    
    # Unused debugging output
    debug_snapshot = {
        'size': len(phantom_map),
        'entropy': compute_entropy(baseline),
        'invariant': derive_invariant(signature)
    }
    
    return final_diagnostic

# Input data with plausible sensor readings
health_signature = [32, 45, 67, 28, 89, 56, 77, 41, 33, 50, 64, 29, 72, 58, 66, 31]
baseline_readings = [44, 23, 57, 12, 68, 35, 71, 19, 54, 28, 63, 47, 59, 38, 74]

# Trigger execution
temp_diagnostic = extract_critical_path(health_signature)
stability_score = evaluate_stability_index(baseline_readings)
final_diagnostic = process_metrics(health_signature, baseline_readings)

print(f"Result: {final_diagnostic}")