import itertools

# Simulated sensor data processing with red herrings and complex transformations
def collect_readings():
    raw_readings = [i * 0.7 + (i % 3) for i in range(15)]
    offset_calib = sum([r % 2.3 for r in raw_readings[::2]])  # Irrelevant calibration offset
    filtered = [r for r in raw_readings if r > 2.0]
    return filtered

# Unrelated diagnostic function (decoy)
def system_health_check(data):
    checksum = sum(d ** 2 for d in data[-5:])
    anomaly_score = len([x for x in data if x < 0])
    return 999 if checksum > 100 else anomaly_score  # Dead-end computation

# Data transformation with distractor logic
def transform_signal(seq, factor=1.5):
    amplified = [s * factor for s in seq]
    noise_floor = 0.25
    applied_noise = [a + noise_floor if i % 4 == 0 else a for i, a in enumerate(amplified)]
    
    # Distractor: unused but plausible signal smoothing
    smoothed = []
    for j in range(len(applied_noise)):
        window = applied_noise[max(0, j-2):j+3]
        smoothed.append(sum(window) / len(window))
    
    # Actual relevant transformation path
    modulated = [abs(x) ** 0.5 * 2 for x in applied_noise]  # Key transformation
    return modulated

# Pattern analyzer - core logic buried among red herrings
def analyze_pattern(data, limit):
    # Irrelevant pre-check
    if len(data) < 5:
        baseline = sum(data) / len(data)
        adjusted = [d - baseline for d in data]
    else:
        adjusted = data[:]  # No real adjustment

    # Complex but irrelevant clustering attempt
    clusters = {}
    for idx, val in enumerate(adjusted):
        key = int(val // 1.5)
        if key not in clusters:
            clusters[key] = []
        clusters[key].append(val)
    
    # Real logic starts here: find first peak above threshold
    peak_found = None
    for i in range(1, len(adjusted) - 1):
        if adjusted[i] > limit and adjusted[i] > adjusted[i-1] and adjusted[i] > adjusted[i+1]:
            peak_found = adjusted[i]
            break
    
    # Distractor: elaborate fallback logic never triggered
    secondary_eval = 0
    if not peak_found:
        pairs = list(itertools.combinations(adjusted, 2))
        diffs = [abs(a - b) for a, b in pairs]
        if diffs:
            avg_diff = sum(diffs) / len(diffs)
            secondary_eval = avg_diff * 1.5
    else:
        # This is the actual result path
        secondary_eval = peak_found * 0.8  # Final meaningful calculation
    
    # Misleading post-processing (never used)
    normalized = [val / (secondary_eval + 1e-8) for val in adjusted]
    entropy = 0
    for n in normalized:
        if n > 0:
            entropy -= n * (n).log()  # Would fail due to missing math import — dead end
    
    return secondary_eval

# Unused helper functions (red herrings)
def compress_sequence(seq):
    return [seq[i] for i in range(0, len(seq), 3)]

def validate_checksum(arr):
    total = 0
    for i, v in enumerate(arr):
        total += v * (i + 1)
    return total % 7 == 0

# Main execution flow
def main():
    readings = collect_readings()                    # Step 1: collect data
    transformed_data = transform_signal(readings)     # Step 2: transform signal
    
    # Irrelevant intermediate checks
    health_status = system_health_check(readings)      # Red herring call
    compressed = compress_sequence(transformed_data)   # Unused result
    valid = validate_checksum(compressed)              # Distractor logic
    
    threshold = 3.8
    final_diagnostic = analyze_pattern(transformed_data, threshold)  # Critical statement
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()