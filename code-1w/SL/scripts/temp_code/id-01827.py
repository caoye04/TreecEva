def analyze_signal(samples, threshold=0.75):
    filtered = [s for s in samples if abs(s) > threshold]
    return len(filtered) > 0 and sum(filtered) / len(filtered) > 0.9


def validate_checksum(data):
    checksum = 0
    for d in data:
        checksum ^= d % 256
    return checksum == 0xAA


def generate_sequence(base, length):
    seq = [base]
    for i in range(1, length):
        seq.append((seq[-1] * 7 + 31) % 100)
    return seq[:length]

# Irrelevant helper - dead code path
def deprecated_normalize(vec):
    mag = sum(x**2 for x in vec) ** 0.5
    return [x / mag for x in vec] if mag else vec

# Unused transformation
def frequency_shift(signal, factor=1.5):
    return [s * factor for s in signal if s > 0.5]

# Main processing chain
primary_samples = [0.1, 0.8, 0.92, 0.65, 0.88]
calibration_sequence = generate_sequence(13, 10)

# Distraction: multiple unrelated checks
signal_ok = analyze_signal(primary_samples)
checksum_valid = validate_checksum(calibration_sequence)

aux_data = [x * 2 + 1 for x in calibration_sequence if x % 3 == 0]
aggregated = sum(aux_data) % 1000

# Another red herring: complex but unused calculation
transformed = [x for x in calibration_sequence if x & 1] \
            + [y // 2 for y in calibration_sequence if not y & 1]
disorder_index = sum(1 for i in range(len(transformed)-1) if transformed[i] > transformed[i+1])

# Real logic begins here — conditional expression with nested logic
status_flags = [
    (x >> 2) & 1 for x in calibration_sequence
]

active_count = sum(status_flags)
shift_correction = 5 if active_count > 4 else 3

adjusted_sequence = [
    ((x << 1) + shift_correction) % 256 for x in calibration_sequence
]

# Diagnostics based on bit patterns
diagnostics = 0
for val in adjusted_sequence:
    if val & (1 << 3):  # Check if bit 3 is set
        diagnostics += 1
    if val & 1 and val & 2:  # If both bit 0 and 1 are set
        diagnostics += 2

# Key computation hidden among distractors
final_diagnostic = process_metrics(calibration_sequence, diagnostics)

# This function looks generic but is actually central
def process_metrics(seq, base_diag):
    total = base_diag * 10
    for i, v in enumerate(seq):
        if i % 2 == 0:
            total += (v % 7) * (i + 1)
        else:
            total -= (v % 5) * ((i + 1) // 2)
    return total + (sum(seq) % 100)

# Final print statement required
Result: {final_diagnostic}