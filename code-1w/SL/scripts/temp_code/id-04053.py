from collections import defaultdict, Counter

# Simulated sensor data stream with noise and calibration flags
def process_sensor_readings(raw_data_stream):
    temporal_marks = [i for i in range(len(raw_data_stream)) if i % 3 == 0]
    filtered_readings = []
    outlier_count = 0
    calibration_shift = 0.987
    base_offset = -12.45

    # Irrelevant frequency analysis (distractor)
    frequency_map = defaultdict(int)
    for val in raw_data_stream:
        frequency_map[val] += 1

    # Actual filtering logic mixed with decoy operations
    temp_buffer = []
    for idx, reading in enumerate(raw_data_stream):
        adjusted = reading * calibration_shift + base_offset
        
        if abs(adjusted) > 100:  # Likely corrupted
            outlier_count += 1
            continue
        
        if idx % 4 == 0:
            temp_buffer.append(adjusted * 0.85)  # Dampen every 4th reading (red herring)

        if reading < -50 or reading > 50:
            pass  # Placeholder for future handling (dead code path)
        else:
            filtered_readings.append(adjusted)

    # Compute moving average over valid window (partially relevant)
    window_size = 3
    smoothed_values = []
    for i in range(len(filtered_readings) - window_size + 1):
        window_avg = sum(filtered_readings[i:i+window_size]) / window_size
        smoothed_values.append(window_avg)

    # Decoy statistical summary (irrelevant)
    stats_summary = {
        'peak': max(smoothed_values),
        'trough': min(smoothed_values),
        'median_guess': sorted(smoothed_values)[len(smoothed_values)//2],
        'stdev_approx': (max(smoothed_values) - min(smoothed_values)) / 2
    }

    # Real computation chain begins here
    magnitude_list = [abs(x) for x in smoothed_values]
    top_quartile = sorted(magnitude_list, reverse=True)[:len(magnitude_list)//4]
    aggregate_score = sum(top_quartile) / len(top_quartile) if top_quartile else 0

    # Secondary adjustment path with misleading intermediate
    trend_analysis = []
    for i in range(1, len(smoothed_values)):
        trend_analysis.append(smoothed_values[i] - smoothed_values[i-1])
    
    volatility_index = sum(abs(x) for x in trend_analysis) / len(trend_analysis) if trend_analysis else 0
    volatility_flag = volatility_index > 15

    # Unused diagnostic flag (distractor)
    system_stable = len([x for x in trend_analysis if x > 0]) / len(trend_analysis) > 0.6 if trend_analysis else False

    # Core calculation hidden among distractions
    correction_factor = 0.88 if not volatility_flag else 0.72
    offset_value = 17.3

    # Key statement
    final_diagnostic = aggregate_score * correction_factor + offset_value

    # Multiple print statements (mimic debugging noise)
    debug_mode = False
    if debug_mode:
        print(f'Outliers removed: {outlier_count}')
        print(f'Volatility: {volatility_index:.2f}, Flag: {volatility_flag}')
        print(f'Stats: {stats_summary}')

    return final_diagnostic

# Auxiliary function (decoy - never called)
def compute_fourier_components(signal):
    result = []
    for k in range(8):
        comp = sum(signal[n] * complex(0, -2 * 3.14159 * k * n / len(signal)).exp() for n in range(len(signal)))
        result.append(abs(comp))
    return result

# Another red herring: string-based checksum (unrelated)
data_tag = "SENS-V4R2"
checksum = sum(ord(c) * (i+1) for i, c in enumerate(data_tag)) % 1024

# Main execution
raw_input = [120, -65, 34, 89, -10, 44, 73, -88, 15, 52, 67, -30, 22, 38, 77, -55]

# Enumerate used idiomatically but partially irrelevant
indexed_weights = {i: w for i, w in enumerate([1.1, 0.9, 1.0, 1.2])}
weight_sum = sum(indexed_weights.values())  # Dead computation

# Zip usage in a non-critical context
timestamps = list(range(10, 10 + len(raw_input)))
dataset_pairs = list(zip(timestamps, raw_input))

result = process_sensor_readings(raw_input)
print(f"Result: {result}")