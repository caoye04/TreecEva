import math

# Simulated sensor data processing for a diagnostic system
def collect_readings():
    raw_signals = [127, 255, 193, 64, 89, 211]
    filtered = [x for x in raw_signals if x > 50]
    normalized = [round(x / 255.0, 3) for x in filtered]
    return normalized

# Irrelevant auxiliary function - dead code path
def legacy_calibrate(x):
    return (x * 0.97) + 3.2

# Another red herring: unused transformation chain
def transform_sequence(seq):
    shifted = [x << 1 for x in seq]
    inverted = [~x & 0xFF for x in shifted]
    return [inverted[i] ^ 0xAA for i in range(len(inverted))]

# Misleading intermediate diagnostics
aux_diags = {
    'noise_floor': 0.042,
    'gain_stabilized': False,
    'phantom_peak': 0.881
}

# Core logic disguised among distractions
def analyze_pattern(values):
    magnitude = sum([v ** 2 for v in values])
    coherence = len(values) / (1 + math.sqrt(magnitude))
    return round(coherence, 4)

# Unused but plausible-looking aggregation
snapshot_log = []
for i in range(3):
    temp_entry = {'cycle': i, 'reading': collect_readings()[i], 'status': 'valid'}
    snapshot_log.append(temp_entry)

# Decoy statistical analysis
mean_proxy = sum(collect_readings()) / len(collect_readings())
variance_proxy = sum([(x - mean_proxy)**2 for x in collect_readings()])
sham_index = variance_proxy * 0.73 if mean_proxy > 0.5 else variance_proxy * 1.4

# Real threshold logic buried in set operations and conditionals
def evaluate_stability(readings, config_level=2):
    critical_set = {0.5, 0.75, 1.0}
    reading_set = set(round(v, 2) for v in readings)
    overlap = critical_set & reading_set  # set operation
    
    baseline = 0.6
    adjustment = 0.15 if len(overlap) > 0 else 0.05
    tolerance = baseline - adjustment
    
    return sum(1 for r in readings if r >= tolerance)

# Distractor: complex-looking but unused bit manipulation
flag_state = 0
for val in [7, 15, 31]:
    flag_state ^= (val << 2) | 0x03
    flag_state &= ~(0x01 << 3)

# Actual signal path begins here
health_indicators = collect_readings()

# Phantom correlation matrix (unused)
corr_matrix = [[round(a * b, 3) for a in health_indicators] for b in health_indicators]

# Conditional expression with real impact (buried)
thresholds = {
    'alpha': 0.45 if len(health_indicators) > 4 else 0.65,
    'beta': 0.7
}

def process_metrics(data, config):
    # Key logic step 1: early filtering
    relevant = [d for d in data if d >= config['alpha']]
    
    # Key logic step 2: conditional branching based on size
    if len(relevant) < 3:
        score = len(relevant) * 17
        return score
    
    # Key logic step 3: real computation path
    avg_val = sum(relevant) / len(relevant)
    
    # Key logic step 4: boolean logic with short-circuit
    bonus = 10 if avg_val > config['beta'] and any(x > 0.8 for x in data) else 0
    
    # Key logic step 5: final calculation
    base_score = int(avg_val * 100)
    
    # Key logic step 6: arithmetic combination
    penalty = 0
    for d in data:
        if d < 0.3:
            penalty += 5
            break  # early termination
    
    # Key logic step 7: final composition
    result = base_score + bonus - penalty
    
    # Key logic step 8: definitive assignment
    final_diagnostic = result * 2
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(health_indicators, thresholds)
print(f"Target result: {final_diagnostic}")