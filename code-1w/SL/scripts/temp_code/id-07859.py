import math

# Simulated sensor data processing with noise filtering and pattern detection
def main():
    raw_readings = [2.1, 3.5, -1.2, 4.8, 6.3, -2.5, 0.7, 5.1, 8.9, 3.3, 7.6, -0.4, 1.8]
    calibration_offset = 1.1
    sensitivity_factor = 0.85
    noise_floor = 0.5
    threshold = 3.0

    # Irrelevant transformation (distractor)
    normalized = [math.log(abs(x) + 1) * sensitivity_factor for x in raw_readings]

    # Apply offset correction (red herring - not used later)
    corrected = [x + calibration_offset for x in raw_readings]

    # Real signal extraction path
    amplified = [x * 1.5 for x in raw_readings]  # Boost signal

    # Noise suppression
    cleaned = []
    for val in amplified:
        if abs(val) > noise_floor:
            cleaned.append(val)

    # Misleading intermediate calculation (dead path)
    avg_cleaned = sum(cleaned) / len(cleaned) if cleaned else 0
    adjusted_values = [x - avg_cleaned for x in cleaned]  # Not actually used

    # Critical slicing operation: focus on recent activity
    recent_activity = cleaned[-7:]  # Only last 7 values matter

    # Secondary filter based on dynamic threshold
    filtered_data = [x for x in recent_activity if x > threshold]

    # Decoy function call (never executed)
    def deprecated_analysis(data):
        return sum([x**2 for x in data]) if data else 0

    # Another red herring list
    shadow_buffer = [0] * len(filtered_data)
    for i in range(len(shadow_buffer)):
        shadow_buffer[i] = math.sin(i) * 10  # Completely irrelevant

    # Actual analysis function
    def analyze_pattern(data, limit):
        if not data:
            return -999
        
        # Complex logic chain
        squared_sum = sum([x ** 2 for x in data])
        mean_val = sum(data) / len(data)
        variance = sum([(x - mean_val) ** 2 for x in data]) / len(data)
        peak = max(data)
        
        # Composite metric with bitwise manipulation (for distraction)
        base_score = int(peak * 100) & int(variance * 10) | int(mean_val)
        
        # More distractions: unused transformations
        log_transform = [math.log(x) for x in data if x > 0]
        rollup = 0
        for x in log_transform:
            rollup ^= int(x * 100)  # Bitwise decoy

        # Real result computation (hidden among distractors)
        adjustment = math.sqrt(variance) if variance > 0 else 0
        final_metric = (squared_sum / len(data)) - adjustment
        
        # Final threshold-based decision
        if final_metric > limit * 2:
            return int(final_metric + 0.5)
        else:
            return int((mean_val + peak) / 2)

    # Unused recursive function (misdirection)
    def recursive_denoise(arr, depth=0):
        if depth >= 2 or len(arr) < 2:
            return arr
        mid = len(arr) // 2
        return recursive_denoise(arr[:mid], depth + 1) + recursive_denoise(arr[mid:], depth + 1)

    # Key execution point
    final_signal = analyze_pattern(filtered_data, threshold)

    # Print required output
    print(f"Result: {final_signal}")

    # Additional irrelevant post-processing
    residual = [x - final_signal for x in filtered_data if x > final_signal]
    entropy = -sum([p * math.log(p) for p in [0.1, 0.2, 0.7]]) if final_signal > 0 else 0

    return final_signal

if __name__ == "__main__":
    main()