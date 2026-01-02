def transform_sequence(data, key_offset):
    shifted = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            shifted.append(val * 2 + key_offset)
        else:
            shifted.append(val - key_offset)
    return shifted


def evaluate_coherence(sequence):
    score = 0
    for a, b in zip(sequence, sequence[1:]):
        if b > a:
            score += 1
        else:
            score -= 0.5
    return score


def filter_anomalies(raw_logs):
    cleaned = []
    thresholds = {'low': -10, 'high': 100}
    for log in raw_logs:
        if thresholds['low'] < log < thresholds['high']:
            cleaned.append(log * 0.95)
    return cleaned  # Distractor: used nowhere critical


def compute_harmonic(weights):
    if not weights:
        return 0
    inv_sum = sum(1 / w for w in weights if w != 0)
    return len(weights) / inv_sum if inv_sum != 0 else 0


def aggregate_metrics(chains, reference):
    temp_result = 0
    for idx, chain in enumerate(chains):
        if idx % 3 == 0:
            temp_result += sum(chain) * 1.1
        elif idx % 3 == 1:
            temp_result -= max(chain) * 0.5
        else:
            temp_result += min(chain) * 2
    
    adjustment = 0
    for r in reference:
        adjustment += r ** 0.5
    
    final_correction = 0
    for c in chains[2]:
        if c > 15:
            final_correction += c // 4
    
    return int(temp_result - adjustment + final_correction)

# Irrelevant setup - red herring variables
system_flags = [True, False, True]
diagnostic_mode = "VERBOSE"
boot_sequence = [0x1A, 0x2B, 0x3C]

# Real data initialization
data_segment = [4, 7, 13, 21]
key_offset = 3

# Step 1: Transform data
transformed = transform_sequence(data_segment, key_offset)
# transformed = [11, 4, 29, 18]

# Step 2: Create processing chain (multiple stages)
processing_chain = [
    [10, transformed[0], 12],              # [10, 11, 12]
    [5, 25, transformed[2]],               # [5, 25, 29]
    [transformed[1], 16, transformed[3]],  # [4, 16, 18]
    [8, 9, 10]
]

# Step 3: Baseline reference generation (distraction logic mixed in)
baseline_reference = []
for i in range(4):
    baseline_reference.append((i+1)**2)
# baseline_reference = [1, 4, 9, 16]

# Irrelevant diagnostics
log_entries = [101, 205, -5, 999, 45]
analyzed_logs = filter_anomalies(log_entries)
coherence_score = evaluate_coherence(transformed)  # Used nowhere

# Unused function call - dead path
def unused_helper(x): return x * x

# Critical statement
final_diagnostic = aggregate_metrics(processing_chain, baseline_reference)

print(f"Result: {final_diagnostic}")