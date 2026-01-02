def analyze_pattern_sequence(sequence):
    total_peaks = 0
    peak_magnitudes = []
    for i, val in enumerate(sequence):
        if val > 0 and (i == 0 or sequence[i-1] <= 0):
            total_peaks += 1
            peak_magnitudes.append(val)
    return total_peaks, sum(peak_magnitudes)

sequence_x = [0, -1, 3, 2, 0, -5, 4, 0, 1]
sequence_y = [2, 0, 1, -1, 4, 0, 0, 3, -2]

# Misleading analysis with dead-end logic
spurious_sum = 0
for x, y in zip(sequence_x, sequence_y):
    if x > y:
        spurious_sum += x * 0.1  # Irrelevant to final result

# Real processing begins
active_segments = 0
segment_lengths = []
for i in range(len(sequence_x)):
    if sequence_x[i] != 0 and sequence_y[i] != 0:
        active_segments += 1
        segment_lengths.append(i)

baseline_offset = len([x for x in sequence_x if x % 2 == 0])

pattern_a = [i * 2 for i in range(4)]
pattern_b = [i + 1 for i in range(4)]

# Dummy string processing - red herring
status_log = "Signal A: OK | Signal B: FAILED | Phase: NOMINAL"
if "FAILED" in status_log:
    recovery_attempts = 3
    status_log = status_log.replace("FAILED", "RETRIED")
    recovery_attempts -= 1

# Core calculation function
def calculate_interference(patt_a, patt_b):
    phase_shift = 0
    for idx, (a, b) in enumerate(zip(patt_a, patt_b)):
        if idx % 2 == 0:
            phase_shift += a - b
        else:
            phase_shift += b - a
    return phase_shift

# Key statement
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# More irrelevant follow-up
checksum = 0
for i, mag in enumerate(analyze_pattern_sequence(sequence_x)[1] * [1, 2, 3][:active_segments]):
    checksum += i * mag

print(f"Result: {net_phase_shift}")