import math

# Simulated quantum register diagnostics with decoy calculations
def initialize_registers(size):
    registers = [0] * size
    for i in range(size):
        registers[i] = (i ** 2 + 3 * i + 7) % 127
    entropy_offset = sum(registers) / len(registers)
    normalization_factor = math.log(entropy_offset + 1)  # unused red herring
    return registers

def apply_quantum_decay(registers):
    decayed = []
    for val in registers:
        if val % 2 == 0:
            decayed.append(int(val * 0.7))
        else:
            decayed.append(val + 5)
    # Dead path: reverse decay (never used)
    def reverse_decay(x):
        return x * 2 if x < 50 else x + 10
    return decayed

def compute_coherence_score(seq):
    score = 0
    for i in range(1, len(seq)):
        score += abs(seq[i] - seq[i-1])
    avg_diff = score / (len(seq) - 1) if len(seq) > 1 else 0
    return avg_diff * 1.7  # arbitrary scaling - distractor

def filter_anomalies(data):
    threshold = sum(data) / len(data) + 10
    filtered = [x for x in data if x < threshold]
    outliers = [x for x in data if x >= threshold]  # computed but unused
    return filtered

def generate_diagnostic_map(values):
    # Complex mapping with irrelevant transformations
    base_map = {i: round(math.sin(v / 10) * 100) for i, v in enumerate(values)}
    enhanced_map = {}
    for k, v in base_map.items():
        if k % 3 == 0:
            enhanced_map[k] = v + 5
        elif k % 5 == 0:
            enhanced_map[k] = v * 2
        else:
            enhanced_map[k] = v - 3
    # Additional decoy structure
    shadow_map = {k+100: -v for k, v in base_map.items()}  # never used
    return enhanced_map

def calculate_entropy(values):
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    probs = [f / len(values) for f in freq.values()]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return entropy * 10  # scaled for distraction

def temporal_phase_shift(data):
    shifted = [data[(i-1) % len(data)] ^ (i * 3) for i in range(len(data))]
    return shifted

def integrate_temporal_effects(registers):
    phase_1 = apply_quantum_decay(registers)
    phase_2 = temporal_phase_shift(phase_1)
    coherence = compute_coherence_score(phase_2)
    filtered = filter_anomalies(phase_2)
    entropy_metric = calculate_entropy(filtered)
    total_impact = int(coherence + entropy_metric)
    return total_impact

def analyze_system_state(registers):
    # Main analysis pipeline
    processed = apply_quantum_decay(registers)
    diagnostic_map = generate_diagnostic_map(processed)
    
    # Critical calculation path
    mapped_values = list(diagnostic_map.values())
    high_freq_count = sum(1 for v in mapped_values if v > 50)
    low_freq_count = sum(1 for v in mapped_values if v < 0)
    balance_factor = high_freq_count - low_freq_count
    
    # Decoy aggregation
    aggregate_sum = sum(mapped_values)  # looks important but not used
    weighted_avg = sum(v * (i+1) for i, v in enumerate(mapped_values)) / len(mapped_values)  # misleading
    
    # Key transformation
    lambda_transform = lambda x: x ** 2 if x > 0 else abs(x)
    transformed_balance = lambda_transform(balance_factor)
    
    # Final integration with prior system state
    temporal_effect = integrate_temporal_effects(registers)
    final_diagnostic = transformed_balance * 3 + temporal_effect // 2
    
    # Unused competing formula (distractor)
    alternative_diagnostic = (aggregate_sum // 10) + int(weighted_avg)
    
    return final_diagnostic

# Irrelevant global variables (distractors)
current_timestamp = 1712345678
system_version = "QX-9.3"
max_iterations = 1000
debug_mode = False

# Execution sequence
quantum_registers = initialize_registers(15)

# Simulate intermediate diagnostics (dead code path)
if debug_mode:
    raw_coherence = compute_coherence_score(quantum_registers)
    print(f"Debug coherence: {raw_coherence}")

# Critical execution point
final_diagnostic = analyze_system_state(quantum_registers)

print(f"Result: {final_diagnostic}")