import math

# Simulated sensor array diagnostics with signal processing and noise filtering
def collect_sensor_readings(raw_data_stream, calibration_factor):
    readings = []
    temp_offset = 0.0
    for val in raw_data_stream:
        if val < 0:
            temp_offset += calibration_factor * 0.1
        elif val > 100:
            temp_offset -= calibration_factor * 0.05
        adjusted = val * (calibration_factor / 10) + temp_offset
        readings.append(round(adjusted, 3))
    return readings

# Legacy function - unused but looks relevant (dead code path)
def legacy_checksum(sequence):
    checksum = 0
    for i in range(len(sequence)):
        checksum ^= (sequence[i] * (i + 1)) % 256
    return checksum & 0xFF

# Signal pattern extraction using slicing and transformation
def extract_patterns(readings, window_size=6):
    patterns = []
    for i in range(0, len(readings) - window_size + 1, 3):  # Overlapping windows, step=3
        segment = readings[i:i + window_size]
        avg = sum(segment) / len(segment)
        peak = max(segment)
        energy = sum(x ** 2 for x in segment)
        normalized_energy = round(energy / (peak + 1e-5), 4)
        patterns.append((avg, peak, normalized_energy))
    return patterns

# Auxiliary function for bit-level analysis (used as distractor)
def bit_analysis(value):
    binary_rep = bin(int(abs(value) * 1000))[2:]
    ones = binary_rep.count('1')
    zeros = binary_rep.count('0')
    balance = abs(ones - zeros)
    return ones > 5 and balance < 10

# Main diagnostic analyzer combining multiple logic types
def analyze_signal(patterns, config_map):
    score_accumulator = 0.0
    penalty_factor = config_map.get('penalty', 0.95)
    critical_threshold = config_map.get('critical_level', 450.0)
    history_log = []

    for idx, entry in enumerate(patterns):
        avg_val, peak_val, norm_energy = entry

        # Irrelevant character counting distraction (simulating metadata)
        metadata_tag = f"SEG{idx:03}"
        char_sum = sum(ord(c) for c in metadata_tag)
        if char_sum % 7 == 0:
            score_accumulator += 0.01  # Red herring increment

        # Primary logic path
        if norm_energy > critical_threshold:
            if avg_val > 30.0:
                score_accumulator += peak_val * 0.3
            else:
                score_accumulator += peak_val * 0.15
        else:
            if peak_val > 85:
                intermediate_flag = (peak_val // 10) % 2 == 1
                if intermediate_flag and avg_val > 25:
                    score_accumulator += math.sqrt(norm_energy) * 0.1

        # Decoy conditional with bitwise distraction
        decoy_value = int(avg_val) ^ int(norm_energy % 100)
        if decoy_value & 0b101010:  # Always true for many values
            history_log.append(decoy_value % 50)

        # Logical operation chain with short-circuit evaluation
        if avg_val > 20 and (peak_val > 90 or norm_energy > 400) and not (idx > 10 and len(history_log) > 5):
            score_accumulator += 1.5

    # Final adjustment based on slicing of history (irrelevant but looks important)
    if len(history_log) >= 5:
        slice_contribution = sum(history_log[2:-1]) * 0.01
        score_accumulator += slice_contribution

    final_score = round(score_accumulator, 4)
    return int(final_score) if final_score > 100 else round(final_score, 2)

# Global constants (some irrelevant)
BASE_SENSITIVITY = 12.5
MAX_BUFFER_SIZE = 256
TEMPORAL_FACTOR = 0.87

# Simulated raw input data
raw_input = [89, 92, 76, 105, 88, 95, 67, 110, 94, 83, 98, 73, 102, 85, 90, 96, 70, 100]

# Calibration and preprocessing
processed_readings = collect_sensor_readings(raw_input, BASE_SENSITIVITY)

# Pattern extraction using slicing
pattern_buffer = extract_patterns(processed_readings)

# Configuration map with red herring entries
threshold_map = {
    'critical_level': 440.5,
    'penalty': 0.93,
    'debug_mode': True,
    'max_iterations': 500,
    'legacy_compat': 'disabled'
}

# Unused variable - misleading intermediate result
diagnostic_trace = [math.log(p[1] + 1) for p in pattern_buffer if p[1] > 30]

# Key execution point
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")