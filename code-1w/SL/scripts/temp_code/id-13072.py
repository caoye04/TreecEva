import itertools

# Sensor network diagnostic simulation with noise filtering and calibration
raw_readings = [145, 128, 256, 99, 1024, 77, 512, 88, 2048, 66, 33, 4096]
noise_floor = 50
calibration_factor = 0.87
baseline_offset = 12
max_threshold = 4000

# Irrelevant temperature conversion (distraction)
temp_celsius = [22.5, 23.1, 21.8, 24.0]
temp_fahrenheit = [(c * 9/5) + 32 for c in temp_celsius]
ambient_avg = sum(temp_fahrenheit) / len(temp_fahrenheit)

def apply_hampel_filter(data, window_size=3):
    # Real but overkill filter (only some data needs cleaning)
    cleaned = []
    half_win = window_size // 2
    for i in range(len(data)):
        window = data[max(0, i-half_win):min(len(data), i+half_win+1)]
        median = sorted(window)[len(window)//2]
        mad = sorted([abs(x - median) for x in window])[len(window)//2]
        if abs(data[i] - median) <= 3 * mad:
            cleaned.append(data[i])
        else:
            cleaned.append(median)
    return cleaned

# Decoy function - never used (dead path)
def analyze_trend_pattern(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    trend_score = 0
    for d in diffs:
        if d > 0:
            trend_score += 1
        elif d < 0:
            trend_score -= 1
    return abs(trend_score)

# Simulate packet loss by dropping every 5th reading (irrelevant to final result)
distorted_readings = [v for i, v in enumerate(raw_readings) if (i + 1) % 5 != 0]

# Real preprocessing: filter out noise floor
filtered_data = [x for x in raw_readings if x > noise_floor]

# Bit manipulation red herring: simulate checksum calculation
checksum = 0
for val in filtered_data:
    checksum ^= (val << 2) | (val >> 8)
    checksum &= 0xFFFF  # Clamp to 16 bits

# Fake normalization chain (unused)
normalized = [(x - noise_floor) / (max_threshold - noise_floor) for x in filtered_data]
scaled_normalized = [round(n * 1000) for n in normalized]

# Real processing function — only this contributes to answer
def process_readings(data, factor):
    adjusted = [int(x * factor) for x in data]
    
    # Use itertools to group powers of two (decoy grouping)
    grouped = {k: list(g) for k, g in itertools.groupby(adjusted, key=lambda x: bin(x).count('1'))}
    
    # Extract only values that are multiples of 4 after adjustment (actual logic)
    valid_outputs = [v for v in adjusted if v % 4 == 0]
    
    # Apply rounding based on average magnitude (critical step)
    avg_val = sum(valid_outputs) / len(valid_outputs) if valid_outputs else 0
    
    # Final transformation uses tuple unpacking and integer division
    summary_stats = (min(valid_outputs), max(valid_outputs), int(avg_val // 1.5))
    min_val, max_val, dampened_avg = summary_stats
    
    # Compute diagnostic score using multiple concepts
    diagnostic_score = (max_val - min_val) // 2
    diagnostic_score += dampened_avg
    
    # String method distraction: encode part of the result as padded hex (unused)
    hex_component = format(diagnostic_score & 0xFF, '04x').replace('0', 'X')
    
    return diagnostic_score

# Unused alternative processing path (distractor)
avg_filtered = sum(filtered_data) // len(filtered_data)
adjusted_avg = avg_filtered * 0.92

# Key execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output the target result
print(f"Result: {final_diagnostic}")