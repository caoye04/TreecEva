import math

# System health monitoring simulation with red herrings and complex data flow
def analyze_component_load(readings):
    if not readings:
        return 0
    filtered = [x for x in readings if x > 0.1]
    if len(filtered) < 3:
        return 0.5
    weighted = sum(x * (i + 1) for i, x in enumerate(filtered[:5]))
    return weighted / len(filtered)


def compute_entropy(data):
    # Irrelevant function: simulates signal entropy but unused in final path
    total = sum(data)
    if total == 0:
        return 0
    probabilities = [d / total for d in data]
    return -sum(p * math.log(p) for p in probabilities if p > 0)


def evaluate_stability_index(temporal_data):
    # Complex but ultimately irrelevant stability metric
    base_score = 0
    for i in range(1, len(temporal_data)):
        if temporal_data[i] > temporal_data[i-1]:
            base_score += 0.3
        else:
            base_score -= 0.2
    return round(base_score, 2)


def generate_diagnostic_report(configs):
    # Dead code path — never called
    return {"status": "idle", "code": 777}

# Decoy variables with plausible names
temp_cache = [0.4, 0.6, 0.8, 0.9]
signal_buffer = [1, 0, 1, 1, 0]
baseline_offset = 0.05
reference_frame = {'a': 10, 'b': 20}

# Core processing chain — relevant data
processing_chain = [
    [2, 4, 6],
    [3, 9, 12],
    [1, 5, 7, 11]
]

# Thresholds used in aggregation
thresholds = {
    'min_activation': 4,
    'penalty_factor': 0.8,
    'boost_enabled': True
}

# Distractor: unused intermediate calculations
snapshot_moment = 12345.67
phase_vector = [math.sin(i * 0.5) for i in range(10)]
consistency_check = any(len(seq) > 4 for seq in processing_chain)

# Real computation begins here — multiple steps with interference
intermediate_scores = []
for sequence in processing_chain:
    # Apply transformation: sum only even numbers above threshold
    activated = [x for x in sequence if x % 2 == 0 and x >= thresholds['min_activation']]
    score = sum(activated)
    if thresholds['boost_enabled'] and len(activated) >= 2:
        score = int(score * 1.25)
    intermediate_scores.append(score)

# Additional irrelevant logic block
if len(intermediate_scores) > 5:
    adjustment = sum(math.sqrt(s) for s in intermediate_scores if s > 0)
else:
    adjustment = -999  # Misleading value, unused

# Aggregate using min, max, and average — key step
min_score = min(intermediate_scores)
max_score = max(intermediate_scores)
avg_score = sum(intermediate_scores) / len(intermediate_scores)

# Final diagnostic depends on composite formula
final_diagnostic = (min_score + max_score * 2 + avg_score) // 1  # Ensures integer

# Another decoy function that looks important
def validate_calibration():
    return False

# Unused flag that seems critical
system_armed = True

# Output the target result
print(f"Result: {final_diagnostic}")