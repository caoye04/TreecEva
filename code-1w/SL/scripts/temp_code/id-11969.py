import math

# Simulated sensor array data (irrelevant structure for distraction)
sensor_specs = {
    'sensitivity': 0.87,
    'calibration_offset': -0.03,
    'noise_floor': 0.005
}

# Irrelevant helper function (dead code path)
def validate_calibration(data):
    if len(data) < 10:
        return False
    return sum(data) / len(data) > 0.1

# Unused signal generation (distractor)
baseline_signals = [math.sin(x * 0.1) + 0.5 * math.cos(x * 0.3) for x in range(20)]

# Core problem: Analyze binary-encoded diagnostics from mixed sensor inputs
def encode_status(code, shift):
    return (code << 2) ^ shift

def decode_threshold(val):
    return (val >> 1) & 0x7FF

# Simulated raw input (12-bit encoded readings)
raw_readings = [0x3A7, 0x2C1, 0x4E6, 0x1D3, 0x5F9]

# Irrelevant transformation chain (misleading intermediate values)
filtered_readings = []
for r in raw_readings:
    temp_val = r * 1.05 - 4.2
    if temp_val > 100:
        filtered_readings.append(int(temp_val))

# Actual relevant processing begins here
adjusted_offsets = [encode_status(r, 7) for r in raw_readings]  # Bit manipulation

# Conditional logic with red herring control flow
critical_flags = []
for a in adjusted_offsets:
    threshold = decode_threshold(a)
    is_critical = False
    if threshold > 512:
        is_critical = True
    elif threshold == 512:
        is_critical = (a % 3) == 0
    else:
        pass  # Explicit no-op for confusion
    critical_flags.append(is_critical)

# Distractor: unused aggregation
average_offset = sum(adjusted_offsets) / len(adjusted_offsets)
median_threshold = sorted([decode_threshold(a) for a in adjusted_offsets])[2]

# Relevant computation: count how many readings have even decoded thresholds
validity_checks = [decode_threshold(a) for a in adjusted_offsets]
even_diagnostic_count = sum(1 for v in validity_checks if v % 2 == 0)

# Secondary diagnostic based on bit parity
parity_matches = 0
for a in adjusted_offsets:
    bits = bin(a).count('1')
    if bits % 2 == 0:
        parity_matches += 1

# Tertiary factor: logical combination of flags
flag_combinations = 0
for i in range(len(critical_flags)):
    if critical_flags[i] and (validity_checks[i] % 4 == 0):
        flag_combinations += 1

# Final processing pipeline
processed_signals = []
for idx, val in enumerate(raw_readings):
    # Multi-step transformation with conditional expression
    transformed = (val * 3 + 1) if idx % 2 == 0 else (val * 2 - 5)
    processed_signals.append(transformed ^ 0x200)  # XOR mask

# Decoy analysis function (never called)
def legacy_analysis(data):
    return [d | 0x1FF for d in data if d < 0x400]

# Key function: computes final diagnostic score
def analyze_readings(signals):
    base_score = 0
    for s in signals:
        # Extract bits 4-7 (inclusive) using bit operations
        segment = (s >> 4) & 0xF
        if segment % 3 == 0:
            base_score += segment
        elif segment % 2 == 0:
            base_score += segment // 2
        else:
            base_score -= 1
    
    # Combine with earlier independent counts (cross-reference)
    global even_diagnostic_count, parity_matches
    bonus = even_diagnostic_count * 2 + parity_matches
    penalty = flag_combinations * 3
    
    # Final formula
    return base_score + bonus - penalty

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Output result as required
print(f"Target result: {final_diagnostic}")