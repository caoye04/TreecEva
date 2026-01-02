def preprocess_signal(data_stream):
    filtered = [x for x in data_stream if x > 30]
    normalized = [x / max(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]


def validate_checksum(frame):
    return sum(frame) % 16 == 0

# Irrelevant helper that is never called
def decrypt_hamming_code(word):
    return word[::-1]

# Misleading diagnostic with decoy logic
class SystemMonitor:
    def __init__(self):
        self.log_entries = []
        self.threshold = 42

    def audit_cycle(self, readings):
        temp_flag = any(r < 10 for r in readings)
        high_activity = len([r for r in readings if r > 75])
        # This function does nothing useful
        return high_activity > 3

# Unused but plausible-looking transformation
transform_matrix = [[1, -1], [0, 1]]

# Core simulation state
quantum_registers = [52, 38, 44, 61, 29, 55, 47]

# Decoy variables to distract from main flow
baseline_offset = 12.8
reference_frame = {i: i**2 for i in range(10)}

# Simulated noise injection (irrelevant)
noise_pattern = set()
for i in range(len(quantum_registers)):
    if i % 3 == 0:
        noise_pattern.add(quantum_registers[i] ^ 7)

# Conditional expression using string method (required feature)
diagnostic_mode = 'deep_scan' if 'scan'.upper() in ['INIT', 'SCAN', 'FINAL'] else 'quick'

# Set operations and distractor logic
allowed_states = {40, 44, 47, 52, 55, 61}
active_states = set(quantum_registers)
overlap_count = len(allowed_states & active_states)  # Partially relevant

# Dead code path protected by always-False condition
if len(noise_pattern) > 100:
    quantum_registers.append(999)
    baseline_offset *= 2

# Primary analysis function — only this matters for final answer
def analyze_system_state(registers):
    # Step 1: Filter values above threshold
    critical_nodes = [r for r in registers if r > 45]
    
    # Step 2: Apply modular arithmetic weighting
    weighted_sum = 0
    for i, val in enumerate(critical_nodes):
        weighted_sum += (val * (i + 1)) % 19
    
    # Step 3: Conditional adjustment based on set membership
    if overlap_count >= 4:
        weighted_sum += 5
    
    # Step 4: String-based switch via conditional expression
    multiplier = 2 if diagnostic_mode == 'deep_scan' else 1
    intermediate = weighted_sum * multiplier
    
    # Step 5: Final adjustment using bit manipulation
    intermediate ^= 13  # XOR with prime
    intermediate += len(str(intermediate))  # Add digit count
    
    # Step 6: Loop-based correction factor
    correction = 0
    for _ in range(3):
        correction = (correction + intermediate) % 7
    
    # Step 7: Apply correction and normalize
    result = intermediate - correction
    
    # Step 8: Final clamp to prevent overflow (not triggered)
    if result > 1000:
        result %= 100
    
    return result

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_registers)
print(f"Target result: {final_diagnostic}")