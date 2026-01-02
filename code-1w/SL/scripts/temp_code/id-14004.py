import math

# Simulate sensor data processing with noise filtering and phase analysis
def generate_raw_phases(n):
    return [((i * 1.618) % 3.14159) for i in range(n)]

# Irrelevant helper: computes magnitude (not used in final path)
def compute_magnitude(x, y):
    return math.sqrt(x**2 + y**2)

# Decoy function: looks important but unused
def legacy_calibrate(data):
    adjusted = []
    for d in data:
        adjusted.append(d * 0.98 + 0.01)
    return adjusted

# Real signal filter based on amplitude and harmonic properties
def is_significant(harmonic_power, base_freq):
    return harmonic_power > (base_freq * 0.5)

# Main filter logic: selects phases where sin^2(value) exceeds threshold
def apply_filter(phases, threshold):
    result = []
    temp_store = []  # Distractor: accumulates values but not used
    for p in phases:
        intensity = math.sin(p) ** 2
        temp_store.append(intensity * 100)  # Red herring storage
        if intensity > threshold:
            result.append(p)
    # Dead code branch: never reached due to prior logic
    if len(result) == 0 and False:
        fallback = sum(temp_store) / len(temp_store)
        result.append(fallback)
    return result

# Unused recursive summation (misleading)
def recursive_sum(lst, idx=0):
    if idx >= len(lst):
        return 0
    return lst[idx] + recursive_sum(lst, idx + 1)

# Bit manipulation decoy: simulates checksum but irrelevant
def calculate_checksum(data):
    chk = 0
    for val in data:
        shifted = int(val * 100) & 0xFF
        chk ^= shifted
        chk = (chk << 1) | (chk >> 7)
        chk &= 0xFF
    return chk

# Generate sequence with known pattern
raw_phases = generate_raw_phases(15)

# Intermediate transformation: create pairs (unused later)
pairwise = list(zip(raw_phases, raw_phases[1:]))
indexed_shifts = [p * (i + 1) for i, p in enumerate(raw_phases)]  # Computed but irrelevant

# Apply actual filter
filtered_phase = apply_filter(raw_phases, threshold=0.7)

# Further distraction: slice operations on filtered result (no effect)
trimmed = filtered_phase[1:-1] if len(filtered_phase) > 2 else filtered_phase
extended_info = [math.cos(f) for f in trimmed]

# Final output - only this matters
Target result: {filtered_phase}