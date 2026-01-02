import math

# Simulated sensor data processing with noise filtering and pattern analysis
def main():
    raw_readings = [127, 255, 191, 63, 223, 31, 159, 95, 239, 47]
    base_offset = 10
    scaling_factor = 2
    noise_floor = 30
    critical_threshold = 200

    # Irrelevant transformation path (dead code branch)
    temp_buffer = [x ^ 0xFF for x in raw_readings if x < noise_floor]
    alternate_path = list(map(lambda x: (x + 5) ** 2 % 256, temp_buffer))

    # Actual signal extraction
    filtered_signal = []
    for val in raw_readings:
        adjusted = (val + base_offset) // scaling_factor
        if adjusted > noise_floor and adjusted % 2 == 1:
            filtered_signal.append(adjusted)

    # Decoy statistical analysis (unused)
    mean_val = sum(filtered_signal) / len(filtered_signal) if filtered_signal else 0
    variance = sum((x - mean_val) ** 2 for x in filtered_signal) / len(filtered_signal) if filtered_signal else 0
    entropy_proxy = -sum((x / sum(filtered_signal)) * math.log(x / sum(filtered_signal)) 
                         for x in filtered_signal if x > 0)

    # Core transformation chain
    shifted_data = [x ^ 0xAA for x in filtered_signal]  # Bit-flip pattern
    processed_data = [x for x in shifted_data if x > 50]
    doubled_stream = [x * 2 for x in processed_data][:8]  # Truncate to fixed size

    # Red herring: complex-looking but unused recursive function
    def _unused_recursive_sum(arr, idx=0):
        if idx >= len(arr):
            return 0
        return arr[idx] + _unused_recursive_sum(arr, idx + 1) if arr[idx] % 3 != 0 else _unused_recursive_sum(arr, idx + 1)

    recursive_trace = _unused_recursive_sum(raw_readings)  # Distractor computation

    # Primary data transformation
    transformed_data = []
    for i, x in enumerate(doubled_stream):
        if i % 3 == 0:
            transformed_data.append(x >> 1)
        elif i % 3 == 1:
            transformed_data.append(x & 0x7F)
        else:
            transformed_data.append(x ^ i)

    # Slicing operation with meaningful subset
    windowed_slice = transformed_data[1:-1]  # Exclude first and last

    # Set operations to eliminate duplicates (though none expected)
    unique_transformed = list(set(windowed_slice))
    unique_transformed.sort()

    # Conditional threshold function (used later)
    def threshold_func(x):
        return x > 65 and (x % 5 == 0 or x % 7 == 0)

    # Real analysis function (key logic path)
    def analyze_pattern(data, predicate):
        count = 0
        total = 0
        streak = 0
        max_streak = 0

        for val in data:
            if predicate(val):
                count += 1
                total += val
                streak += 1
            else:
                max_streak = max(max_streak, streak)
                streak = 0

        max_streak = max(max_streak, streak)
        bonus = 10 * (max_streak >= 2)  # Bonus for consecutive matches

        # Secondary combinatoric condition
        pairs = [(a, b) for i, a in enumerate(data) for b in data[i+1:]]
        valid_pairs = [(a, b) for a, b in pairs if (a + b) % 11 == 0]
        pair_score = len(valid_pairs) * 5

        return count * 100 + total + bonus + pair_score

    # Dummy higher-order function (distractor)
    processors = [
        lambda x: x + 1,
        lambda x: x * 2,
        lambda x: x - 5
    ]
    applied_ops = [op(10) for op in processors]  # Unused result

    # Key execution point
    filtration_score = analyze_pattern(transformed_data, threshold_func)

    # Additional red herring: bit manipulation chain not affecting result
    checksum = 0
    for x in raw_readings:
        checksum ^= x << 1
        checksum &= 0xFFFF
        checksum ^= checksum >> 8

    # Print target result
    print(f"Target result: {filtration_score}")

if __name__ == "__main__":
    main()