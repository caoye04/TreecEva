import math

# Simulated quantum register diagnostics with heavy interference

# Irrelevant constants (red herrings)
MAX_BUFFER_SIZE = 65536
CALIBRATION_OFFSET = -0.003456
REFERENCE_VOLTAGE = 3.3
TEMPORAL_DILATION_FACTOR = 1.000001
NOISE_FLOOR_DB = -97.4

# Core system state variables (some relevant, some not)
system_ticks = 128
quantum_registers = [0b1101, 0b1010, 0b1111, 0b0001]
entropy_pool = []
active_channels = 4
diagnostic_log = {"errors": [], "warnings": []}
baseline_checksum = 0

# Decoy function - looks important but unused
def compute_hamming_weight(value):
    weight = 0
    while value:
        weight += value & 1
        value >>= 1
    return weight

# Unused transformation table (distractor)
transform_lut = [compute_hamming_weight(i) for i in range(16)]

# Misleading intermediate calculations
shadow_register = sum([(r ^ 0b1010) & 0b0101 for r in quantum_registers])
temporal_coherence = math.sin(system_ticks * 0.1) * TEMPORAL_DILATION_FACTOR

# Fake data validation (dead path)
if len(quantum_registers) > 5:
    diagnostic_log["errors"].append("REGISTER_OVERFLOW")
elif any(r < 0 for r in quantum_registers):
    diagnostic_log["errors"].append("NEGATIVE_REGISTER")
else:
    diagnostic_log["warnings"].append("NORMAL_OPERATION")

# Real processing begins here — buried under noise
initial_entropy = 0
for reg in quantum_registers:
    bit_flips = 0
    temp_reg = reg
    # Count transitions between adjacent bits (cyclic)
    bits = [(reg >> i) & 1 for i in range(4)] + [(reg >> 0) & 1]  # cyclic wrap
    for i in range(4):
        if bits[i] != bits[i+1]:
            bit_flips += 1
    initial_entropy += bit_flips

entropy_pool.append(initial_entropy)

# Secondary transformation: map registers to phase weights
phase_weights = []
for idx, reg in enumerate(quantum_registers):
    # Weight based on popcount and position
    popcount = bin(reg).count('1')
    phase_factor = popcount * (idx + 1) * math.pi / 4
    phase_weights.append(math.cos(phase_factor))

# Accumulate weighted phase sum
weighted_phase_sum = sum(phase_weights)

# Auxiliary checksum from bit patterns
auxiliary_checksum = 0
for r in quantum_registers:
    reversed_r = int(bin(r)[2:].zfill(4)[::-1], 2)
    auxiliary_checksum += (r ^ reversed_r) & 0b1111

# Actual core logic disguised among distractions
# Apply non-linear transformation to entropy measure
nonlinear_entropy = math.log(entropy_pool[0] + 1) ** 2

# Combine with auxiliary checksum through bitwise blend
blended_metric = (int(nonlinear_entropy) << 4) | (auxiliary_checksum & 0b1111)

# Final analysis function — only called once, late in execution
def analyze_system_state(registers):
    # Local irrelevant copy
    local_copy = [r ^ 0b0011 for r in registers]
    
    # More fake diagnostics
    anomaly_score = 0
    for r in local_copy:
        if bin(r).count('1') == 3:
            anomaly_score += 10
    
    # Real computation hidden in middle
    total_set_bits = sum(bin(r).count('1') for r in registers)
    cyclic_shift_product = 1
    for i, r in enumerate(registers):
        shifted = ((r << i) | (r >> (4 - i))) & 0b1111
        cyclic_shift_product *= (shifted % 7) or 1  # avoid zero
    
    # Key calculation: combine product with bit count
    raw_diagnostic = total_set_bits * cyclic_shift_product
    
    # Red herring: normalize by fake metric
    if anomaly_score > 0:
        normalized = raw_diagnostic / anomaly_score
    else:
        normalized = raw_diagnostic + 5
    
    # Final adjustment using earlier blended metric (from outside)
    # This creates cross-scope dependency — critical for complexity
    final_adjustment = blended_metric % 13
    return int(normalized) + final_adjustment

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_registers)

# Output required format
print(f"Target result: {final_diagnostic}")