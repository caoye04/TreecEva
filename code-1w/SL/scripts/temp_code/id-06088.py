import math

# Simulated quantum sensor array diagnostics with noise filtering and state analysis

def generate_calibration_matrix(seed_offset):
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            base = (i + 1) * (j + 1) + seed_offset
            matrix[i][j] = int((base ** 2) % 17)
    return matrix


def apply_noise_filter(raw_data, threshold=0.85):
    # Irrelevant filtering function - not used in final computation but looks important
    filtered = []
    for x in raw_data:
        if abs(x) / (max(raw_data) + 1e-9) > threshold:
            filtered.append(x * 0.9)
        else:
            filtered.append(x * 0.1)
    return filtered


def compute_entropy(signal):
    # Distractor function: computes signal entropy but unused
    total = sum(abs(x) for x in signal)
    if total == 0:
        return 0.0
    probabilities = [abs(x) / total for x in signal]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)


def extract_phase_components(sequence):
    # Extract even-indexed elements as 'phase_a', odd as 'phase_b'
    phase_a = [sequence[i] for i in range(0, len(sequence), 2)]
    phase_b = [sequence[i] for i in range(1, len(sequence), 2)]
    return phase_a, phase_b


def transform_sequence(seq, factor):
    # Apply modular transformation with bit shifting
    transformed = []
    for val in seq:
        temp = (val * factor) % 13
        shifted = (temp << 1) ^ 5  # XOR for obfuscation
        transformed.append(shifted)
    return transformed


def validate_coherence(state_vector, ref_matrix):
    # Dummy validation that appears critical but returns constant
    coherence_score = 0
    for i in range(min(len(state_vector), len(ref_matrix))):
        for j in range(len(ref_matrix[i])):
            coherence_score += (state_vector[i] + j) % 5
    return coherence_score > 100  # Always True given inputs


def accumulate_diagnostic_weight(seq, matrix):
    weight = 0
    for i, val in enumerate(seq):
        row = matrix[i % 4]
        pivot = row[i % 4]
        # Complex-looking but deterministic accumulation
        weight += (val ^ pivot) * ((i + 1) % 7)
    return weight


def analyze_system_state(q_sequence, c_matrix):
    # Core analysis logic
    
    # Step 1: Unpack phases
    primary, secondary = extract_phase_components(q_sequence)
    
    # Step 2: Transform primary using derived factor
    factor = (c_matrix[0][0] + c_matrix[1][1]) // 3
    processed_primary = transform_sequence(primary, factor)
    
    # Step 3: Secondary undergoes slicing and reversal (distraction)
    sliced_secondary = secondary[1:3][::-1]  # Only uses middle two elements reversed
    enhanced_secondary = [x + 10 for x in sliced_secondary]  # Further distraction
    
    # Step 4: Accumulate diagnostic weight from processed primary
    raw_weight = accumulate_diagnostic_weight(processed_primary, c_matrix)
    
    # Step 5: Apply corrective offset based on matrix trace
    trace = sum(c_matrix[i][i] for i in range(4))
    corrected_weight = raw_weight - trace
    
    # Step 6: Conditional adjustment based on length parity (always even here)
    adjustment = 0
    if len(q_sequence) % 2 == 0:
        adjustment = (corrected_weight % 11)
    else:
        adjustment = -(corrected_weight % 13)
    
    # Step 7: Final diagnostic score
    final_score = corrected_weight + adjustment
    
    # Irrelevant entropy check (dead code path)
    if False:  # Simulates disabled debug mode
        entropy = compute_entropy(q_sequence)
        final_score = int(final_score * (1 + entropy / 10))
    
    return final_score

# --- Main Execution ---

# Sensor data initialization (simulated quantum readings)
sensor_readings = [3, 7, 2, 8, 5, 1, 9, 4]

# Generate calibration matrix with fixed offset
calibration_matrix = generate_calibration_matrix(seed_offset=6)

# Apply noise filter (result unused - red herring)
filtered_readings = apply_noise_filter(sensor_readings)

# Compute entropy for display (unused in logic)
signal_entropy = compute_entropy(sensor_readings)

# Validate system coherence (called but result ignored)
coherence_status = validate_coherence(sensor_readings, calibration_matrix)

# Transform full sequence (partially relevant - only factor matters)
transformed_full = transform_sequence(sensor_readings, factor=4)

# Extract quantum sequence segments
quantum_sequence = [
    sensor_readings[0] + 1,
    sensor_readings[2] * 2,
    sensor_readings[4] + 3,
    sensor_readings[6] - 1,
    sensor_readings[1] + 2,
    sensor_readings[3] * 3,
    sensor_readings[5] + 4,
    sensor_readings[7] - 2
]

# Update quantum_sequence with conditional overrides (only some apply)
for idx in range(len(quantum_sequence)):
    if quantum_sequence[idx] % 4 == 0:
        quantum_sequence[idx] = (quantum_sequence[idx] // 2) + 5
    elif quantum_sequence[idx] % 3 == 0:
        quantum_sequence[idx] = (quantum_sequence[idx] * 2) % 17

# Critical execution point
final_diagnostic = analyze_system_state(quantum_sequence, calibration_matrix)

# Output result
print(f"Result: {final_diagnostic}")