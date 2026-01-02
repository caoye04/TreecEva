import math

# Irrelevant constants (distractors)
BASELINE_OFFSET = 237
REFERENCE_SCALE = 1.85
MAX_ITERATIONS = 1500

# Misleading intermediate variables
temporal_factor = 42
alignment_score = 987
activation_mask = [0] * 10

# Core system parameters (some are decoys)
def generate_phase_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def calculate_entropy(flow):
    total = 0
    for x in flow:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 6)

# Unused function - red herring
def deprecated_calibration(x):
    return (x ** 2 + 3 * x + 1) % 107

# Lambda for dynamic weighting - actually used
weight_adjuster = lambda w: w * 0.9 if w > 5 else w * 1.2

# Simulated sensor array with irrelevant processing
def simulate_sensor_readings(count=8):
    readings = []
    for i in range(count):
        val = (i * i + 3 * i + 7) % 13
        readings.append(val)
    # Dead code path
    if len(readings) > 20:
        readings = readings[:10]
    return readings

# Sensor data not directly related to main calculation
sensor_data = simulate_sensor_readings()
filtered_data = [x for x in sensor_data if x % 2 == 1]

# Main logic setup
logic_threshold = 7
phase_vectors = generate_phase_sequence(7)

# Decoy transformation chain
echo_buffer = list(map(lambda x: (x + 4) * 2, phase_vectors))
shadow_copy = echo_buffer.copy()
echo_buffer.extend([0, 0, 0])

# Auxiliary function with partial relevance
def assess_coherence(elements):
    if not elements:
        return 0
    raw_sum = sum(abs(e) for e in elements)
    norm_factor = len(elements) ** 0.5
    return raw_sum / norm_factor

# Secondary distraction: unused coherence analysis
coherence_index = assess_coherence(sensor_data)
consistency_flag = coherence_index > 5

# Core evaluation function that matters
def evaluate_system_response(limit, phases):
    # Level 1: Filter based on threshold
    filtered = [p for p in phases if p <= limit]
    
    # Level 2: Apply weight adjustment via lambda
    adjusted = [weight_adjuster(f) for f in filtered]
    
    # Level 3: Transform using arithmetic and exponentiation
    transformed = []
    for a in adjusted:
        if a != 0:
            result = (a ** 2) / math.log(a + 2)
            transformed.append(result)
        else:
            transformed.append(0)
    
    # Level 4: Compute weighted sum with offset distraction
    base_total = sum(transformed)
    
    # Level 5: Apply conditional scaling (control flow)
    scaling_factor = 1.5 if len(filtered) > 4 else 2.0
    scaled = base_total * scaling_factor
    
    # Level 6: Add constant derived from phase vector property
    magic_offset = phases[2] * phases[4]  # 2 * 5 = 10
    
    # Level 7: Final adjustment with distractor constant
    final_value = scaled + magic_offset - BASELINE_OFFSET * 0  # Neutralized distractor
    
    return int(round(final_value))

# Execution point of interest
thermal_capacity = evaluate_system_response(logic_threshold, phase_vectors)

# Print result as required
print(f"Target result: {thermal_capacity}")