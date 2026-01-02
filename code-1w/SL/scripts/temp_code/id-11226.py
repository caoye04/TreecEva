import itertools

# Simulated sensor fusion system for predictive maintenance

def analyze_phase_shift(signal_a, signal_b):
    shift = 0
    for i in range(min(len(signal_a), len(signal_b))):
        if signal_a[i] & 1 != signal_b[i] & 1:
            shift += (signal_a[i] ^ signal_b[i]) % 7
    return shift

# Irrelevant helper - dead code path
def deprecated_normalizer(x):
    return (x + 32768) % 65536

# Misleading intermediate diagnostic (decoy)
current_telemetry = [184, 215, 193, 204, 177, 226, 168, 201]
baseline_reference = [180, 220, 190, 210, 170, 230, 160, 200]

# Unused transformation chain
temp_offset = 0
for a, b in zip(current_telemetry, baseline_reference):
    temp_offset += abs(a - b) // 4

# Core processing functions
def generate_entropy_vector(data_stream):
    entropy = 0
    counts = {}
    for val in data_stream:
        counts[val] = counts.get(val, 0) + 1
    for count in counts.values():
        if count > 1:
            entropy += count ** 2
    return entropy

def evaluate_coherence(sequence):
    coherence = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1] or sequence[i-1] > sequence[i] < sequence[i+1]:
            coherence += 1
    return coherence * (len(sequence) % 13)

def compute_harmonic_balance(seq):
    even_sum = sum(x for x in seq if x % 2 == 0)
    odd_sum = sum(x for x in seq if x % 2 == 1)
    return (even_sum - odd_sum) * len(seq)

# Primary analysis engine
def process_metrics(signature, thresholds):
    # Key computational steps
    base_score = 0
    
    # Step 1: Analyze bit-pattern stability
    stable_bits = 0
    for val in signature:
        stable_bits += bin(val).count('1')
    
    # Step 2: Apply threshold-based filtering using set logic
    critical_values = set(signature) & set(thresholds['critical'])
    warning_values = set(signature) - set(thresholds['ignore'])
    
    # Step 3: Conditional weighting
    weight = len(critical_values) if critical_values else len(warning_values) // 2 or 1
    
    # Step 4: Modular arithmetic chain
    accumulator = stable_bits % 97
    for _ in range(3):
        accumulator = (accumulator * 17 + 29) % 97
    
    # Step 5: Bitwise integration
    fused_state = 0
    for val in signature[:4]:
        fused_state ^= (val << 2) & 0xFF
        fused_state = (fused_state | (val >> 6)) & 0xFF
    
    # Step 6: Coherence evaluation (recursive pattern)
    def recursive_dampener(x, depth):
        if depth <= 0 or x < 10:
            return x
        return recursive_dampener((x // 3) + (x & 15), depth - 1)
    
    dampened = recursive_dampener(accumulator + len(critical_values), 4)
    
    # Step 7: Final composition
    raw_metric = (dampened * weight) + fused_state
    
    # Step 8: Final adjustment using harmonic balance (red herring: not actually used)
    unused_harmonic = compute_harmonic_balance(signature)
    
    # ACTUAL final result
    final_adjustment = (raw_metric ^ 42) % 10000
    return final_adjustment

# System initialization
sensor_readings = [213, 187, 194, 203, 176, 221, 169, 208, 188, 199]

# Configuration map with misleading entries
threshold_map = {
    'critical': [213, 176, 999, 888],  # 999,888 are decoys
    'ignore': [100, 200, 300, 188],    # 188 is actually in data but should be ignored
    'legacy_mode': False
}

# Secondary irrelevant calculation chain
aggregate_checksum = 0
for chunk in itertools.batched(sensor_readings, 3):  # Python 3.12 syntax
    aggregate_checksum += sum(chunk) * len(chunk)

# Phase analysis with unused result
phase_diagnostic = analyze_phase_shift(sensor_readings[::2], sensor_readings[1::2])

# Entropy computation (distraction)
entropy_level = generate_entropy_vector(sensor_readings)
coherence_index = evaluate_coherence(sensor_readings)

# Signal health assessment
health_signature = []
for val in sensor_readings:
    processed = val
    processed = ((processed ^ 48) + 13) % 256  # Nonlinear transform
    processed = (processed * 2) % 256 if val > 190 else (processed + 50) % 256
    health_signature.append(processed)

# Final integration step
final_diagnostic = process_metrics(health_signature, threshold_map)

print(f"Result: {final_diagnostic}")