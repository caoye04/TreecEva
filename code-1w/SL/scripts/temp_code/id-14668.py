from collections import defaultdict

# Simulate multi-sensor signal processing with noise filtering and pattern detection
def main():
    raw_data = [12, 15, 10, 8, 13, 15, 9, 11, 14, 10, 12, 13, 15, 8, 9]
    baseline_threshold = 11
    signal_buffer = []
    noise_counter = 0
    filtered_signals = []
    trend_moments = []

    # Step 1: Filter out low-amplitude noise and capture significant fluctuations
    for i, reading in enumerate(raw_data):
        if reading > baseline_threshold:
            adjusted_value = reading - baseline_threshold
            signal_buffer.append(adjusted_value)
            if i % 3 == 0:
                noise_counter += 1  # Distraction: counts every third high signal
        else:
            if reading < baseline_threshold - 2:
                noise_counter -= 1  # Misleading adjustment

    # Step 2: Amplify signals above dynamic threshold
    amplified_pool = []
    dynamic_factor = len(signal_buffer) // 3 + 1
    for val in signal_buffer:
        amplified = val * dynamic_factor
        amplified_pool.append(amplified)
        if amplified > 10:
            trend_moments.append(amplified // 2)

    # Step 3: Group by magnitude class (mod 3) using defaultdict
    magnitude_groups = defaultdict(list)
    for x in amplified_pool:
        magnitude_groups[x % 3].append(x)

    processed_signals = []
    secondary_sum = 0
    for key in sorted(magnitude_groups.keys()):
        group = magnitude_groups[key]
        if len(group) > 1:
            processed_signals.extend(group)
        else:
            secondary_sum += sum(group)  # Dead-end computation

    # Step 4: Detect equilibrium based on symmetry in processed signals
    def detect_equilibrium(signals):
        if not signals:
            return 0
        sorted_signals = sorted(signals)
        n = len(sorted_signals)
        mid = n // 2
        left_half = sorted_signals[:mid]
        right_half = sorted_signals[-mid:]
        
        # Compute symmetry score
        symmetry_score = 0
        for a, b in zip(left_half, reversed(right_half)):
            symmetry_score += abs(a - b)
        
        # Introduce distractor loop (no impact)
        temp_cache = {}
        for idx, val in enumerate(right_half):
            temp_cache[idx] = val ** 0.5  # Unused cache
            
        return len(left_half) * 2 - symmetry_score  # Core logic

    # Key assignment point
    equilibrium_score = detect_equilibrium(processed_signals)
    
    # Additional red herring computations
    outlier_flags = 0
    for s in processed_signals:
        if s % 7 == 0:
            outlier_flags += 1
    final_diagnostic = noise_counter + secondary_sum + outlier_flags

    print(f"Result: {equilibrium_score}")

if __name__ == "__main__":
    main()