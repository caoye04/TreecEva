import math

# Simulated sensor data processing with red herrings and complex flow
def fetch_raw_readings():
    return [2.1, 3.5, 4.8, 5.0, 6.3, 7.7, 8.2, 9.0, 10.1]

def normalize(values):
    max_val = max(values)
    return [v / max_val for v in values]

def apply_filter(data, mode='lowpass'):
    # Irrelevant filtering modes (only 'lowpass' used)
    if mode == 'lowpass':
        return [x for x in data if x > 0.3]
    elif mode == 'highpass':
        return [x for x in data if x < 0.7]
    else:
        return data

def encrypt_key(sequence):  # Distractor function – looks important but unused
    key = 0
    for i, val in enumerate(sequence):
        key ^= int(val * 100) + i
    return key

def scramble_text(text):  # Heavy distraction using string methods
    reversed_parts = [part[::-1].upper() for part in text.split(',')]
    joined = '-'.join(reversed_parts)
    return joined.replace('A', 'X').replace('E', 'Y')

def generate_checksum(arr):  # Seemingly relevant but not used in final result
    checksum = 0
    for i, x in enumerate(arr):
        checksum += int(x * 100) * (i + 1)
    return checksum % 1000

def transform_signal(readings):
    log_scaled = [math.log(x + 1) for x in readings]  # Non-linear transformation
    centered = [y - 0.5 for y in log_scaled]  # Shift
    abs_vals = [abs(z) for z in centered]  # Make positive
    return abs_vals

def decode_metadata(meta_str):  # Complex string manipulation as distraction
    segments = meta_str.lower().split('|')
    cleaned = [s.strip().replace('_', '') for s in segments]
    case_swapped = [item.casefold() if len(item) % 2 else item.swapcase() for item in cleaned]
    return ''.join(case_swapped)

def analyze_pattern(seq, limit):
    # Core logic hidden among noise
    total = 0.0
    count = 0
    for val in seq:
        if val < limit:
            total += val ** 2
            count += 1
        else:
            break  # Early exit based on order
    if count == 0:
        return 0.0
    avg_sq = total / count
    return round(avg_sq * 1000, 4)  # Scale up to integer-like decimal

def main():
    # Step 1: Fetch raw data
    raw_data = fetch_raw_readings()

    # Step 2: Normalize (red herring: normalization occurs but later steps use transformed version)
    normalized_data = normalize(raw_data)

    # Step 3: Apply irrelevant filter
    filtered_data = apply_filter(normalized_data, mode='lowpass')

    # Step 4: Generate useless checksum
    dummy_checksum = generate_checksum(filtered_data)

    # Step 5: Transform signal — this is actually critical
    transformed_data = transform_signal(raw_data)

    # Step 6: Use string method distractions
    metadata = "sensor_01|loc_a|q3_2024"
    decoded_info = decode_metadata(metadata)
    scrambled_diag = scramble_text("error,warning,info")

    # Step 7: Encrypt key — looks security-critical but unused
    secret_key = encrypt_key(transformed_data)

    # Step 8: Set threshold based on a misleading constant
    base_threshold = 1.8
    adjustment_factor = 0.3
    threshold = base_threshold - adjustment_factor  # evaluates to 1.5

    # Step 9: Critical analysis on correct data path
    final_diagnostic = analyze_pattern(transformed_data, threshold)

    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Dead code paths below (distractors)
    if dummy_checksum > 500:
        fallback = math.sin(secret_key)
    else:
        fallback = math.cos(len(scrambled_diag))

    return final_diagnostic

if __name__ == '__main__':
    main()