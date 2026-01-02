import math

# Simulated sensor array diagnostics with signal processing
# Focus: embedded systems signal validation

# Raw sensor inputs (simulated)
sensor_ids = [101, 102, 103, 104]
raw_readings = [127, 255, 96, 180]

def collect_diagnostics(readings):
    # Irrelevant health check (distractor)
    system_health = sum(1 for r in readings if r > 100)
    threshold_met = [r for r in readings if r >= 128]
    return len(threshold_met)

# Unused transformation map (dead code path)
transform_map = {
    'linear': lambda x: x * 1.05,
    'boost': lambda x: x * 1.3 if x < 128 else x * 0.9,
    'attenuate': lambda x: x * 0.7
}

# Signal conditioner with masking logic
def apply_mask(signal, mask_type='default'):
    if mask_type == 'inverted':
        return signal & 0xFF
    else:
        return signal | 0x0F

# Legacy calibration function (never called)
def calibrate_legacy(signal_list):
    adjusted = []
    for s in signal_list:
        adj = s * 0.98 + 5
        if adj > 255:
            adj = 255
        adjusted.append(int(adj))
    return adjusted

# Core signal processor
processed_signals = []
for sid, reading in zip(sensor_ids, raw_readings):
    # Apply bitwise conditioning
    masked = apply_mask(reading, 'default')
    
    # Normalize to 8-bit range (redundant but plausible)
    normalized = min(255, max(0, masked))
    
    # Frequency emulation transform (only some used)
    freq_shift = (normalized ^ 0xAA) >> 2
    amplitude_comp = int(math.sqrt(freq_shift) * 4)
    
    # Add to processed set
    processed_signals.append(amplitude_comp)

# Diagnostic engine
baseline_ref = [50, 60, 55, 65]
offset_tracker = 0

for i, val in enumerate(processed_signals):
    if val > baseline_ref[i]:
        offset_tracker += 1
    elif val < baseline_ref[i]:
        offset_tracker -= 1

# Secondary validation chain (distractor)
consistency_check = all(p > 40 for p in processed_signals)
validity_score = sum(processed_signals) / len(processed_signals) if consistency_check else 0

# Red herring: unused combinatorics block
combinatoric_weight = 0
for i in range(1, len(processed_signals)):
    combinatoric_weight += math.factorial(i) % 100

# Real analysis function
analyze_readings = lambda signals: sum(
    sig * (idx + 1) for idx, sig in enumerate(signals)
) // len(signals)

# Final diagnostic computation (key statement)
final_diagnostic = analyze_readings(processed_signals)

# Output result
print(f"Result: {final_diagnostic}")