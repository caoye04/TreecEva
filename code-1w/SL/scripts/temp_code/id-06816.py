import math

# Irrelevant helper function (decoy)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Unused transformation matrix
tf_matrix = [[1, -1], [0.5, 0.5]]

# Simulated sensor readings (distraction data)
sensor_a = 42.7
sensor_b = 18.3
sensor_c = 91.2

# Noise threshold constants (mostly unused)
NOISE_FLOOR = 0.05
SATURATION_LIMIT = 95.0
BASELINE_DRIFT = 0.003

# Core parameters for actual computation
raw_flux = 144
base_threshold = 12

# Dead code path — looks important but never called
def calibrate_system(mode='passive'):
    if mode == 'aggressive':
        return sum([i * 0.1 for i in range(10)])
    return 0

# Auxiliary irrelevant list comprehension
offsets = [i * BASELINE_DRIFT for i in range(1, 8) if i % 2 == 0]

# Fake diagnostic log (never used)
diagnostic_log = [f'ErrCode-{i}' for i in [3, 7, 11, 14] if sensor_a > i * 3]

# Red herring: complex-looking but unused bitwise cascade
bit_cascade = ((sensor_a ^ 100) & 0xFF) >> 2

# Unused conditional expression
status_flag = 'active' if SATURATION_LIMIT > sensor_c else 'idle'

# Dummy data structure with cross-references
system_state = {
    'flux_history': [raw_flux - 10, raw_flux, raw_flux + 5],
    'threshold_snapshot': [base_threshold - 1, base_threshold],
    'checksum': (raw_flux ^ base_threshold) % 17
}

# Another decoy function that appears related but isn't used
def evaluate_stability(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings)
    return variance < 10

# Real logic begins here — deeply nested and obscured by context

def analyze_phase_stability(flux_value):
    if flux_value <= 0:
        return 0
    phase_score = 0
    for i in range(2, int(math.sqrt(flux_value)) + 1):
        if flux_value % i == 0:
            phase_score += i
            if i != flux_value // i:
                phase_score += flux_value // i
    return phase_score

# Secondary computation with distraction
harmonic_set = {i for i in range(1, 25) if 144 % i == 0}  # set operation

# Misleading efficiency approximation (unused)
rough_efficiency = round((raw_flux / SATURATION_LIMIT) * 100, 2)

# Actual key function buried among distractions
def compute_efficiency(value, threshold):
    # Step 1: Apply logarithmic scaling
    scaled = math.log(value, 2) if value > 1 else 0
    
    # Step 2: Add contribution from divisor analysis
    divisors_total = analyze_phase_stability(value)
    
    # Step 3: Conditional adjustment based on threshold parity
    adjustment = threshold * 2 if threshold % 2 == 0 else threshold
    
    # Step 4: Use list comprehension to filter harmonic relevance
    relevant_harmonics = [h for h in harmonic_set if h <= scaled * 2]
    
    # Step 5: Aggregate harmonic influence
    harmonic_influence = sum(relevant_harmonics) // len(relevant_harmonics) if relevant_harmonics else 0
    
    # Step 6: Combine scaled log, divisor sum, and harmonic input
    intermediate = int(scaled + harmonic_influence)
    
    # Step 7: Apply adjustment only if intermediate passes condition
    if intermediate > threshold:
        intermediate += adjustment
    
    # Step 8: Final transformation using bit manipulation
    final_result = (intermediate ^ divisors_total) & 0xFFFF  # Mask to 16 bits
    
    return final_result

# --- Execution Point of Interest ---
filtration_yield = compute_efficiency(raw_flux, base_threshold)

# Unrelated post-processing (dead path)
if filtration_yield > 100:
    filtration_yield = filtration_yield % 89

# Output the target result
print(f"Target result: {filtration_yield}")