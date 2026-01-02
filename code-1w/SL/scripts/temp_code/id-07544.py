import math

# Simulated sensor array data from a distributed monitoring system
def fetch_raw_readings():
    return [127, 255, 192, 64, 31, 88, 142]

# Irrelevant transformation: color space conversion (red herring)
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    else:
        h = (60 * ((r - g) / df) + 240) % 360
    s = 0 if mx == 0 else (df / mx)
    v = mx
    return h, s, v

# Unused function: dead code path (decoy)
def decrypt_key(fragment):
    return sum([ord(c) * (i + 1) for i, c in enumerate(fragment)]) % 256

# Signal processing pipeline
noise_floor = 32
calibration_offset = 17

raw_data = fetch_raw_readings()
filtered_data = [x for x in raw_data if x > noise_floor]  # Remove low-amplitude noise

# Apply calibration using lambda abstraction (meaningful use)
apply_calibration = lambda val: (val + calibration_offset) % 256
adjusted_data = list(map(apply_calibration, filtered_data))

# Bit manipulation stage: extract diagnostic bits (relevant)
bit_analysis = []
for val in adjusted_data:
    bit_pattern = ((val >> 3) & 1) ^ ((val >> 6) & 1)  # XOR of bit 3 and bit 6
    bit_analysis.append(bit_pattern)

count_of_ones = sum(bit_analysis)

# Set operations: track active signal bands (partially relevant)
band_a = {120, 140, 160, 180, 200}
band_b = {140, 160, 190, 210}
overlap = band_a & band_b  # {140, 160}
spurious_detection = len(overlap) > 2  # False

# Tuple unpacking with conditional logic (nested control flow)
signal_stats = (
    len(adjusted_data),
    sum(adjusted_data) // len(adjusted_data),
    max(adjusted_data)
)
size, avg, peak = signal_stats

# Early termination check (irrelevant condition)
if avg < 100:
    result_flag = "LOW_POWER"
    buffer_reset = [0] * 8
    final_diagnostic = -999
else:
    # Main computation branch
    entropy_component = 0
    for x in adjusted_data:
        if x > 0:
            entropy_component += x * math.log(x, 2)
    entropy_component = int(entropy_component / 10)

    # Secondary transformation: frequency masking (distractor)
    mask_sequence = [((i * 7) % 256) for i in range(8)]
    masked_avg = avg ^ mask_sequence[avg % 8]  # Bitwise distraction

    # Real computation: combine count_of_ones and entropy
    diagnostic_base = count_of_ones * 1000
    adjustment_factor = 0
    
    # Complex conditional with short-circuit evaluation
    if peak > 200 and (spurious_detection or (avg > 150 and size >= 5)):
        adjustment_factor = 25
    elif avg > 120 or size >= 6:
        adjustment_factor = 12
    else:
        adjustment_factor = 5

    # Final integration of components (critical path)
    final_diagnostic = diagnostic_base + adjustment_factor + entropy_component

# Function that is defined but not used (decoy)
def compress_signal(data):
    return [data[i] for i in range(0, len(data), 2)]

# Unused set operation (red herring)
potential_errors = {"E101", "E102", "W205"}
critical_errors = {"E101", "F300"}
ignored_diagnostics = potential_errors - critical_errors

# Key statement
final_diagnostic = analyze_readings(processed_signals)

# Wrapper to simulate modular structure (distracting abstraction)
def analyze_readings(signals):
    base_score = 0
    for s in signals:
        if s % 2 == 0:
            base_score += s // 4
        else:
            base_score += s // 5
    return base_score + 33

# Data preparation for analyze_readings (actual source of input)
processed_signals = [x + 5 for x in raw_data if x % 4 == 0]

# Reassign final_diagnostic using the real function
final_diagnostic = analyze_readings(processed_signals)

print(f"Result: {final_diagnostic}")