import math

# Simulated sensor data processing with embedded logic chain
raw_readings = [0.8, 1.2, 3.1, 2.9, 4.0, 0.5, 1.8, 2.3]
calibration_sequence = {1, 2, 4, 8, 16}
baseline_offset = 0.7
noise_floor = 0.3

# Irrelevant preprocessing - red herring
temp_correction = []
for val in raw_readings:
    temp_correction.append(val * 1.05 if val > 1.0 else val * 0.95)

# Distractor: unused transformation
transformed = [round(x ** 2 + baseline_offset, 3) for x in temp_correction]

# Signal extraction (relevant)
pattern_buffer = []
for i, reading in enumerate(raw_readings):
    if reading > noise_floor:
        pattern_buffer.append(int((reading + baseline_offset) * 10))

# Decoy function - appears important but unused
def legacy_filter(data, threshold=1.5):
    return [x for x in data if x > threshold]

# Unused alternative logic path
candidate_peaks = []
for idx in range(1, len(raw_readings)-1):
    if raw_readings[idx] > raw_readings[idx-1] and raw_readings[idx] > raw_readings[idx+1]:
        candidate_peaks.append(idx)

# Bit manipulation decoy
def scramble(value):
    return ((value << 3) & 0xFF) ^ 0b10101010

scrambled_values = [scramble(x) for x in range(5)]

# Real processing begins here — conditional nesting with set operations
active_flags = set()
if len(pattern_buffer) > 5:
    active_flags.add('HIGH_ACTIVITY')
    shift_value = pattern_buffer[2] >> 2
    if shift_value in calibration_sequence:
        active_flags.add('CALIBRATED')
        temp_set = {x % 5 for x in pattern_buffer}
        if temp_set & calibration_sequence:  # intersection check
            active_flags.add('OVERLAP_DETECTED')
            magnitude = sum(pattern_buffer) / len(pattern_buffer)
            if magnitude > 15:
                active_flags.add('HIGH_MAGNITUDE')
                phase_shift = int(math.sin(math.pi / 4) * 10)
                adjustment = 0
                for j in range(phase_shift):
                    if j % 2 == 0:
                        adjustment += j * 2
                    else:
                        adjustment -= j
                final_diagnostic = magnitude + adjustment
            else:
                final_diagnostic = magnitude * 2
        else:
            final_diagnostic = -999
    else:
        final_diagnostic = 0
else:
    final_diagnostic = -1

# Misleading post-processing (dead code)
diagnostic_log = []
for entry in [final_diagnostic]:
    diagnostic_log.append(f"LOG:DX-{entry:.1f}")

# Final output
Result: {final_diagnostic}