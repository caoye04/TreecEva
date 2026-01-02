import math

# System calibration and diagnostic evaluation
# Simulates a sensor array self-test with data validation and error correction

def generate_noise_profile(length, seed=42):
    # Irrelevant function: generates dummy noise (not used in final result)
    return [(i * seed) % 7 for i in range(length)]


def validate_checksum(data):
    # Unused validation utility (red herring)
    return sum(data) % 16 == 0


def shift_window(buffer, offset):
    # Misleading transformation not used in critical path
    return [buffer[i % len(buffer)] for i in range(offset, offset + len(buffer))]


def compute_entropy(values):
    # Distractor function: computes Shannon entropy but unused
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

# Raw sensor inputs (simulated)
sensor_readings = [18, 24, 36, 42, 54, 60, 72]

# Irrelevant transformations (dead code paths)
decoy_transform = [x // 3 * 2 for x in sensor_readings if x > 30]
offset_data = shift_window(sensor_readings, 3)
noise_pattern = generate_noise_profile(7)

# Critical data pipeline
baseline_correction = [x // 6 for x in sensor_readings]  # Integer division step
filtered_signals = [x for x in baseline_correction if x % 2 == 0]  # List comprehension: keep even
scaled_outputs = [x * 9 for x in filtered_signals]  # Scale for calibration

# System flags representing hardware states
system_flags = {
    'overload': False,
    'calibrated': True,
    'legacy_mode': False,
    'debug_enabled': True
}

# Secondary derived metrics (some irrelevant)
cpu_temperature = 72.3
memory_cycles = 144
sync_counter = sum(scaled_outputs) // 12  # Distraction calculation

# Checksum verification (unused but looks important)
data_integrity = validate_checksum(scaled_outputs)

# Main calibration sequence
 calibration_sequence = []
for val in scaled_outputs:
    if val > 30:
        calibration_sequence.append(val + 4)
    elif val == 30:
        calibration_sequence.append(val + 1)
    else:
        calibration_sequence.append(val)

# Additional decoy logic with nested conditions (never executed)
temporary_state = 0
if system_flags['legacy_mode']:
    for i in range(len(calibration_sequence)):
        if calibration_sequence[i] > 50:
            temporary_state += 2
        else:
            temporary_state -= 1

# Real-time clock adjustment (irrelevant side computation)
rtc_offset = 0
for _ in range(3):
    rtc_offset += 11
rtc_offset = rtc_offset % 29

# Core diagnostic processor
def process_metrics(metrics, flags):
    if not flags['calibrated']:
        return -999
    
    # Key logic steps:
    # Step 1: Apply safety threshold filter
    safe_range = [m for m in metrics if 35 <= m <= 60]
    
    # Step 2: Find mid-range stability point
    if len(safe_range) >= 2:
        midpoint = (safe_range[0] + safe_range[-1]) // 2
    else:
        midpoint = 0
    
    # Step 3: Adjust based on debug status
    adjustment = 5 if flags['debug_enabled'] else -5
    
    # Step 4: Add entropy from system constants (fixed)
    base_entropy = cpu_temperature // 6  # Always 12 (72.3 // 6 = 12.0 → 12)
    
    # Step 5: Combine all factors
    raw_diagnostic = midpoint + adjustment + int(base_entropy)
    
    # Step 6: Final scaling (irrelevant bit manipulation)
    final_value = (raw_diagnostic << 2) >> 2  # No-op bit shift (keeps same value)
    
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(calibration_sequence, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")