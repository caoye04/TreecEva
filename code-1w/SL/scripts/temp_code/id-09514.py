import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_readings = [127, 255, 192, 64, 32, 15, 8, 3]
    scale_factor = 0.75
    adjusted = [r * scale_factor for r in raw_readings]
    return adjusted

# Irrelevant transformation: color mapping (distractor)
def map_to_color(value):
    if value > 200:
        return 'red'
    elif value > 100:
        return 'yellow'
    else:
        return 'green'

# Unused function: dead code path (red herring)
def legacy_calibrate(data):
    return [int(x * 1.1) % 256 for x in data]

# Signal mask using bitwise manipulation (relevant)
def apply_mask(signal, key=0b1101):
    masked = []
    for val in signal:
        # Convert float to int for bitwise op, use fractional part as modifier
        intval = int(val)
        fractional = val - intval
        masked_val = (intval ^ key) + fractional  # XOR with key
        masked.append(masked_val)
    return masked

# Data smoothing via moving average (distractor, not used in final path)
def smooth_data(seq, window=3):
    smoothed = []
    for i in range(len(seq)):
        start = max(0, i - window // 2)
        end = min(len(seq), i + window // 2 + 1)
        avg = sum(seq[start:end]) / (end - start)
        smoothed.append(avg)
    return smoothed

# Core analysis: frequency pattern detection (relevant)
def detect_frequency_peaks(signal):
    peaks = 0
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks += 1
    return peaks

# String-based status encoding (required python string method)
def encode_status(code, version='v2'):
    binary_str = bin(code)[2:]  # Convert to binary string
    padded = binary_str.zfill(8)  # Pad to 8 bits
    flipped = ''.join('1' if b == '0' else '0' for b in padded)
    return flipped.replace('1', 'X').replace('0', 'O')  # String substitution

# Secondary transformation chain (partially relevant)
def transform_sequence(data):
    shifted = [int(x) >> 2 for x in data]  # Right shift by 2
    modded = [s % 7 for s in shifted]
    return sorted(modded, reverse=True)  # Sorting distractor

# Main processing pipeline
readings = collect_readings()

# Dead assignment: intermediate result not used later (distractor)
temperatures = [math.log(r + 1) for r in readings if r > 50]

# Apply critical mask
masked_signal = apply_mask(readings, key=13)

# Extract diagnostic features
peak_count = detect_frequency_peaks(masked_signal)

# Generate unused hash-like digest (red herring)
digest = ''.join([encode_status(int(x), 'v2')[:4] for x in masked_signal[:4]])

decoy_stats = {
    'avg': sum(masked_signal) / len(masked_signal),
    'max': max(masked_signal),
    'min': min(masked_signal)
}

# Transform but only use one element (misleading complexity)
transformed_ranks = transform_sequence(masked_signal)
rank_anchor = transformed_ranks[0]  # Only this is used

# Auxiliary calculation with string logic (minimal relevance)
def compute_string_weight(s):
    return s.count('X') * 1.5 + s.count('O') * 0.5

weight_score = compute_string_weight(digest)

# Final integration of multiple sources (key step)
base_diagnostic = peak_count * 1000
offset = rank_anchor * 50
adjusted_diagnostic = base_diagnostic + offset - int(weight_score)

# Final computation depends on conditional history (short-circuit logic)
reference_check = len(digest) > 0 and digest.find('X') != -1

if reference_check and math.isclose(decoy_stats['avg'], decoy_stats['avg'], abs_tol=1e-9):
    correction = int(math.sin(math.pi / 4) * 100)
else:
    correction = -1

final_diagnostic = adjusted_diagnostic + correction

# Output required result
print(f"Result: {final_diagnostic}")