import math

def analyze_pattern(seq):
    # Distractor: unused function (dead code path)
    return sum(x ** 2 for x in seq if x > 0)

def validate_checksum(data):
    # Another red herring: computes something never used
    checksum = 0
    for i, val in enumerate(data):
        checksum += val * (i + 1)
    return checksum % 1024

def transform_element(x, mode):
    if mode == 'A':
        return int(math.sqrt(x)) if x > 0 else 0
    elif mode == 'B':
        return x ^ 15  # Bitwise XOR as distraction
    else:
        return x

def filter_noisy_data(raw):
    # Irrelevant filtering logic with misleading comments
    cleaned = [x for x in raw if isinstance(x, int) and x >= 0]
    stats = {
        'original_len': len(raw),
        'cleaned_len': len(cleaned),
        'noise_ratio': (len(raw) - len(cleaned)) / len(raw) if raw else 0
    }
    # Returns only data, stats are ignored later (distractor)
    return cleaned

def compute_moving_average(arr, window=3):
    # Unused helper — adds complexity but no impact
    if len(arr) < window:
        return []
    averages = []
    for i in range(len(arr) - window + 1):
        averages.append(sum(arr[i:i+window]) / window)
    return averages

def process_transformations(sequence, settings):
    temp_result = []
    mode_flag = settings['mode']
    threshold = settings['limit']
    scale_factor = settings.get('scale', 1.0)

    # Real logic starts here — buried among distractions
    for item in sequence:
        # Step 1: Apply transformation based on mode
        transformed = transform_element(item, mode_flag)

        # Step 2: Scale numerically (only relevant when mode is not B)
        if mode_flag != 'B':
            transformed = int(transformed * scale_factor)

        # Step 3: Filter by threshold
        if transformed < threshold:
            temp_result.append(transformed)
        else:
            continue  # Early break alternative

    # Step 4: Accumulate using arithmetic progression weight
    weighted_sum = 0
    for idx, val in enumerate(temp_result):
        weighted_sum += val * (idx + 1)  # Increasing weights

    # Step 5: Adjust with bit manipulation (key step)
    final_shift = weighted_sum >> 2  # Divide by 4 using right shift

    # Step 6: Add constant offset from encoded string (string method distractor)
    key_string = "offset_calibrate_x9"
    offset_str = ''.join([c for c in key_string if c.isdigit()])  # Extract digits: '9'
    offset = int(offset_str) if offset_str else 0

    # Final computation
    final_output = final_shift + offset

    # Irrelevant tuple unpacking (distractor)
    aux_data = (len(temp_result), sum(temp_result) if temp_result else 0, math.pi)
    count_ref, _, _ = aux_data

    # Return the real answer
    return final_output

# Main execution block
if __name__ == '__main__':
    # Input setup
    raw_data_stream = [16, 25, 9, 36, -4, 49, 64]  # Some negative and positive values
    config_params = {
        'mode': 'A',
        'limit': 10,
        'scale': 2
    }

    # Preprocessing: filter out invalid entries (negative numbers, non-ints)
    filtered_data = filter_noisy_data(raw_data_stream)

    # Introduce decoy computation on filtered_data
    decoy_avg = compute_moving_average(filtered_data, 2)
    _ = validate_checksum(filtered_data)  # Call with no use

    # Critical statement
    final_output = process_transformations(filtered_data, config_params)

    # Output result
    print(f"Result: {final_output}")