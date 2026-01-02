from collections import defaultdict, Counter
import math

# Simulated sensor data from multiple sources
telemetry_stream = [
    [1.2, 0.8, 1.5, 2.3, 1.1],
    [0.9, 1.0, 1.6, 2.1, 1.3],
    [1.3, 0.7, 1.4, 2.5, 1.0],
    [1.1, 0.9, 1.7, 2.2, 1.4]
]

# Irrelevant auxiliary mapping (distractor)
color_profile = {
    'low': '#00FFAA',
    'medium': '#FFBB00',
    'high': '#FF0000'
}

# Decoy function that looks important but is unused
def compute_gradient(signal):
    return [signal[i+1] - signal[i] for i in range(len(signal)-1)]

# Misleading normalization function with dead logic
def normalize_readings(data):
    flat = [item for row in data for item in row]
    mean_val = sum(flat) / len(flat)
    stdev = (sum((x - mean_val)**2 for x in flat) / len(flat))**0.5
    
    # Dead branch - never executed due to hardcoded flag
    if False:
        return [[(x - mean_val)/stdev for x in row] for row in data]
    
    # Actually returns raw data (misleading)
    return data

# Real preprocessing with subtle transformation
def filter_noise(signal_matrix, kernel_size=3):
    padded = [[0] + row + [0] for row in signal_matrix]
    filtered = []
    for row in padded[:-1]:  # Skip last dummy row
        smoothed = []
        for i in range(1, len(row) - 1):
            window = row[i-1:i+2]
            smoothed.append(sum(window) / len(window))
        filtered.append(smoothed)
    return filtered

# Bit manipulation decoy (irrelevant)
def pack_flags(mode, active, priority):
    return (priority << 5) | (active << 4) | mode

# Unused complex structure (red herring)
class DiagnosticFrame:
    def __init__(self, timestamp, readings):
        self.timestamp = timestamp
        self.readings = readings
        self.checksum = sum(readings) % 256

# Another distraction: frequency analysis with no impact
def dominant_frequency(signal):
    n = len(signal)
    fft = [complex(0, 0)] * n
    for k in range(n):
        for t in range(n):
            angle = -2 * math.pi * t * k / n
            fft[k] += complex(signal[t] * math.cos(angle), signal[t] * math.sin(angle))
    magnitudes = [abs(x) for x in fft]
    return magnitudes.index(max(magnitudes))

# Real processing begins here
def segment_by_variance(data_blocks):
    variance_map = defaultdict(float)
    for idx, block in enumerate(data_blocks):
        flat_block = [item for row in block for item in row]
        mean_blk = sum(flat_block) / len(flat_block)
        variance = sum((x - mean_blk)**2 for x in flat_block) / len(flat_block)
        variance_map[f'segment_{idx}'] = round(variance, 4)
    return variance_map

# Threshold configuration (used later)
def generate_thresholds(base_sensitivity=0.15):
    levels = ['critical', 'warning', 'info']
    multipliers = [3.0, 1.5, 0.5]
    return {lvl: base_sensitivity * mult for lvl, mult in zip(levels, multipliers)}

# Core analysis logic - actual path to answer
def analyze_signal(cleaned_data, thresholds):
    # Flatten all rows
    all_values = [val for row in cleaned_data for val in row]
    
    # Count occurrences in ranges (real work)
    counter = Counter()
    for v in all_values:
        if v > thresholds['critical']:
            counter['critical'] += 1
        elif v > thresholds['warning']:
            counter['warning'] += 1
        else:
            counter['info'] += 1
    
    # Compute diagnostic score
    score_parts = [
        counter['critical'] * 100,
        counter['warning'] * 10,
        counter['info'] * 1
    ]
    
    # Final diagnostic is sum of weighted counts
    final_score = sum(score_parts)
    
    # Additional irrelevant transformation (distraction)
    if final_score > 100:
        binary_rep = bin(int(final_score))[2:]
        flipped = ''.join('1' if b == '0' else '0' for b in binary_rep)
        _alternate = int(flipped, 2)  # unused
    
    return final_score

# === Execution Flow ===

# Step 1: Normalize (returns original)
normalized_telemetry = normalize_readings(telemetry_stream)

# Step 2: Filter noise (actual transformation)
processed_data = filter_noise(normalized_telemetry)

# Step 3: Segment variance (distractor computation)
variance_segments = segment_by_variance([telemetry_stream])  # uses original

# Step 4: Generate real thresholds
threshold_map = generate_thresholds(0.12)

# Step 5: Analyze signal - this is where answer is computed
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")