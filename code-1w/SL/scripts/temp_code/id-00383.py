import itertools

# Simulated sensor data processing with noise filtering and state tracking
def main():
    raw_signals = [15, 23, 9, 44, 67, 12, 4, 38, 77, 29]
    calibration_offset = 7
    noise_floor = 10
    max_amplitude = 100
    temp_buffer = [x + calibration_offset for x in raw_signals]  # Irrelevant adjusted copy

    # Distractor: complex but unused signal transformation
    transformed = []
    for x in temp_buffer:
        if x > 20:
            transformed.append((x ** 2) % 53)

    # Actual filtering based on dynamic thresholds
    filtered_data = []
    for val in raw_signals:
        if val > noise_floor:
            filtered_data.append(val)

    # Bitwise flag tracking (mixed paradigm)
    flag_register = 0
    for i in range(len(filtered_data)):
        if filtered_data[i] % 2 == 0:
            flag_register |= (1 << i)
        else:
            flag_register &= ~(1 << i)

    # Create misleading summary stats
    avg_val = sum(raw_signals) / len(raw_signals)
    peak_magnitude = max(raw_signals)
    entropy_approx = 0.0
    for x in raw_signals:
        if x > 0:
            entropy_approx += x * math.log(x, 2)  # Unused complex calc

    # Set up threshold map using dictionary and set operations
    critical_levels = {40, 60, 80}
    baseline = {'low': 15, 'med': 30, 'high': 50}
    threshold_map = {**baseline}
    for k in threshold_map.keys():
        if k in ['med', 'high']:
            threshold_map[k] *= 2  # Modify thresholds

    # Use itertools to generate redundant combinations (distractor)
    combos = list(itertools.combinations(filtered_data, 2))
    valid_pairs = []
    for a, b in combos:
        if (a + b) > threshold_map['med']:
            valid_pairs.append((a, b))

    # Real processing function buried among distractions
    def analyze_magnitude(x):
        if x > threshold_map['high']:
            return 3
        elif x > threshold_map['med']:
            return 2
        elif x > threshold_map['low']:
            return 1
        return 0

    def process_signals(data, thresholds):
        counts = [0, 0, 0, 0]
        for item in data:
            level = analyze_magnitude(item)
            counts[level] += 1
        # Final logic: weighted sum based on levels
        aggregate = 0
        for i in range(len(counts)):
            aggregate += i * counts[i]
        # Secondary adjustment based on bit register parity
        bin_str = bin(flag_register).count('1')
        if bin_str % 2 == 0:
            aggregate -= counts[0]
        else:
            aggregate += counts[3]
        return aggregate

    # Dead code path - never executed but looks important
    def debug_dump():
        print("Signal dump:", raw_signals)
        return False  # Never called

    # Key execution point
    final_output = process_signals(filtered_data, threshold_map)

    # Print result as required
    print(f"Result: {final_output}")

if __name__ == '__main__':
    import math
    main()