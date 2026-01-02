def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant preprocessing: reverse and pad with zeros
    padded_readings = [0] * 5 + raw_readings[::-1] + [0] * 3
    normalized = [x * calibration_factor for x in raw_readings]

    # Distractor: complex-looking but unused transformation
    transformed = []
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(val ** 0.5)

    # Real filtering based on dynamic thresholds
    dynamic_threshold = sum(normalized) / len(normalized) * 1.2
    filtered_data = [x for x in normalized if x > dynamic_threshold]

    # Decoy function call that does nothing
    def adjust_phase(signal):
        return [abs(x * 1j) for x in signal]  # Unused result

    # Bit manipulation red herring
    bit_analysis = 0
    for x in filtered_data:
        shifted = int(x) << 2
        xor_val = shifted ^ 255
        bit_analysis += bin(xor_val).count('1')

    # Create threshold map using string-based keys (misleading complexity)
    categories = ['low', 'med', 'high']
    thresholds = [dynamic_threshold * 0.8, dynamic_threshold, dynamic_threshold * 1.4]
    threshold_map = {k: v for k, v in zip(categories, thresholds)}

    # Unused sorting operation to distract
    sorted_pairs = sorted(enumerate(transformed), key=lambda x: x[1], reverse=True)

    # Actual processing function
    def process_readings(data, config):
        base = config['med']
        count_above = sum(1 for x in data if x > base)
        avg_enhanced = sum(x * 1.1 for x in data) / len(data) if data else 0
        # Key computation step
        score = int(avg_enhanced) * count_above

        # String slicing distraction
        tag = 'diagnostics_report_v2'
        prefix = tag[:10]
        suffix = tag[-3:]
        version_code = int(suffix) if suffix.isdigit() else 2

        # Final diagnostic combines numeric and irrelevant string-derived value
        return score + version_code * 10

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Print required output
    print(f"Result: {final_diagnostic}")

# Seeded input to ensure determinism
import math
raw_input_data = [math.sin(x * 0.5) * 100 for x in range(15)]
calib_factor = 1.05
analyze_sensor_array(raw_input_data, calib_factor)