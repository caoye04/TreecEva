def analyze_sensor_data(raw_readings, threshold=100):
    # Irrelevant preprocessing: normalize data (not actually used in final result)
    normalized = [x / max(raw_readings) * 100 for x in raw_readings]
    filtered = [x for x in raw_readings if x > 10]

    # Distractor: complex-looking but unused transformation
    transformed = []
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            transformed.append(val ** 0.5 * (i + 1))
        else:
            transformed.append(val / (i + 1) + 5)

    # Real computation begins: extract critical indices
    critical_indices = [i for i, x in enumerate(raw_readings) if x > threshold]

    # Compute diagnostic windows using slicing
    windows = []
    for idx in critical_indices:
        start = max(0, idx - 2)
        end = min(len(raw_readings), idx + 3)
        window_slice = raw_readings[start:end]
        windows.append(sum(window_slice) / len(window_slice))

    # Unused decoy function call (misleading)
    def calculate_entropy(data):
        from math import log
        freq = {}
        for x in data:
            freq[x] = freq.get(x, 0) + 1
        entropy = 0
        for count in freq.values():
            p = count / len(data)
            entropy -= p * log(p)
        return entropy

    entropy_diagnostic = calculate_entropy(raw_readings[:5])  # Dead code path

    # Actual relevant logic: compute trend reversals using bitwise and logical ops
    reversals = 0
    for i in range(1, len(windows) - 1):
        prev, curr, next_val = windows[i-1], windows[i], windows[i+1]
        if (curr > prev and curr > next_val) or (curr < prev and curr < next_val):
            reversals += 1

    # Construct aggregate metrics with zip and slicing
    trend_data = list(zip(windows[::2], windows[1::2]))
    aggregate_metrics = [abs(a - b) for a, b in trend_data]

    # Correction factor based on reversal parity and bit manipulation
    shift_amount = reversals & 3  # Bitwise AND to get modulo 4
    base_correction = 7
    correction_factor = base_correction << shift_amount  # Left shift distraction

    # Safety margin computed via conditional expression
    safety_margin = 1.5 if len(critical_indices) >= 2 else 0.8

    # Key statement
    final_diagnostic = aggregate_metrics[-1] + correction_factor * safety_margin

    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Unused variables (distractors)
    peak_magnitude = max(raw_readings) - min(raw_readings)
    stability_ratio = len(critical_indices) / len(raw_readings)
    dummy_flag = False or True and not False

    return final_diagnostic

# Execute with fixed input
data_stream = [85, 92, 103, 47, 115, 64, 120, 58, 99, 134]
analyze_sensor_data(data_stream)