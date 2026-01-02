from itertools import combinations

# Simulate a data processing pipeline for sensor readings
def analyze_readings(readings):
    window_size = 4
    threshold = 75
    temp_log = []
    outlier_count = 0

    # Preprocess: normalize readings using modular arithmetic
    normalized = [(val % 100) + 10 for val in readings]

    # Misleading transformation: this is logged but not used later
    transformed = [x * 1.5 if x > threshold else x * 0.8 for x in normalized]
    temp_log.extend(transformed)

    # Actual relevant processing: sliding window sum
    window_sums = [sum(normalized[i:i+window_size]) for i in range(len(normalized) - window_size + 1)]

    # Detect outliers based on window variance (distraction logic)
    for ws in window_sums:
        if ws > threshold * 2:
            outlier_count += 1

    # Irrelevant recursive helper (dead-end function)
    def recursive_sum(n):
        return n if n <= 1 else n + recursive_sum(n - 2)

    # Core logic: apply lambda-based filtering to valid windows
    valid_windows = list(filter(lambda x: x % 2 == 1, window_sums))

    # Compute character count from debug tag (semi-relevant)
    debug_tag = "analysis_v1"
    char_offset = len(debug_tag)  # Used later

    # Destructuring assignment with slice
    first_half, second_half = valid_windows[:len(valid_windows)//2], valid_windows[len(valid_windows)//2:]

    # Checksum calculation depends only on first half and offset
    checksum = 0
    for val in first_half:
        checksum += (val ^ char_offset)  # XOR with length of tag

    # Red herring: unused product calculation
    total_product = 1
    for val in second_half:
        total_product *= max(1, val // 10)

    # This print is required to output the result
    return checksum


def process_segment(data, size):
    # Additional slicing and case conversion distraction
    ascii_vals = [ord(c.lower()) for c in 'DebugMode']
    shift = sum(ascii_vals) % size
    shifted_data = [d + shift for d in data]
    return analyze_readings(shifted_data)

# Input data
sensor_data = [120, 85, 60, 95, 110, 40, 70, 50]
window_size = 4
checksum = process_segment(sensor_data, window_size)
print(f"Result: {checksum}")