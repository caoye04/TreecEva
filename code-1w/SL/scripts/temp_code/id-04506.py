from collections import defaultdict, Counter
import math

def collect_sensor_data():
    # Simulated sensor matrix (irrelevant structure)
    raw_readings = [
        [14, 17, 23, 31, 19],
        [11, 16, 25, 33, 21],
        [13, 18, 22, 30, 20],
        [12, 15, 24, 32, 18]
    ]
    return raw_readings

def filter_outliers(data_block):
    # Irrelevant filtering logic with misleading statistics
    flat = [item for row in data_block for item in row]
    mean_val = sum(flat) / len(flat)
    std_dev = (sum((x - mean_val) ** 2 for x in flat) / len(flat)) ** 0.5
    threshold = mean_val + 1.5 * std_dev
    filtered = [x for x in flat if x <= threshold]  # Most pass anyway
    return filtered

def generate_checksum(sequence):
    # Decoy function - never actually used in critical path
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= (val + i) * 3
    return chk % 1000

def decrypt_sequence(encrypted):
    # Obfuscation layer - appears important but output unused
    decrypted = []
    key = 247
    for val in encrypted:
        shifted = (val ^ key) % 100
        decrypted.append(shifted)
    return decrypted

def parse_metadata(header_str):
    # String processing red herring
    parts = header_str.split('|')
    metadata_map = {}
    for part in parts:
        if '=' in part:
            k, v = part.split('=', 1)
            metadata_map[k.strip()] = v.strip()
    timestamp = metadata_map.get('ts', '0')
    node_id = sum(ord(c) for c in metadata_map.get('node', ''))
    return int(timestamp), node_id

def transform_readings(readings):
    # Core transformation - only this matters
    transformed = []
    for row in readings:
        new_row = []
        for val in row:
            temp = val * 2 - 1
            if temp % 3 == 0:
                temp = int(temp / 3)
            else:
                temp = temp + 5
            new_row.append(temp)
        transformed.append(new_row)
    return transformed

def aggregate_levels(matrix):
    # Secondary relevant operation
    level_count = defaultdict(int)
    total = 0
    for row in matrix:
        for val in row:
            category = 'low' if val < 25 else 'high'
            level_count[category] += 1
            total += val
    return dict(level_count), total

def analyze_readings(data):
    # Final analysis - depends on prior transforms
    counts, grand_total = aggregate_levels(data)
    adjustment = 0
    if 'high' in counts and counts['high'] > 6:
        adjustment = int(math.log(grand_total, 2))
    elif 'low' in counts:
        adjustment = -sum(counts.values())
    diagnostic_code = grand_total - adjustment
    return diagnostic_code

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    sensor_grid = collect_sensor_data()

    # Step 2: Parse fake metadata (distraction)
    header = "format=AX7|ts=19485|node=ZETA7|version=3.1"
    timestamp, node_score = parse_metadata(header)

    # Step 3: Transform readings (critical path starts)
    processed_data = transform_readings(sensor_grid)

    # Step 4: Filter outliers (result ignored - red herring)
    cleaned_readings = filter_outliers(sensor_grid)

    # Step 5: Attempt decryption (unused result)
    disguised_data = decrypt_sequence(cleaned_readings)

    # Step 6: Generate checksum for logging (decoy use)
    log_checksum = generate_checksum(disguised_data)

    # Step 7: Analyze the *processed* data (key step)
    final_diagnostic = analyze_readings(processed_data)

    # Step 8: Print result
    print(f"Result: {final_diagnostic}")