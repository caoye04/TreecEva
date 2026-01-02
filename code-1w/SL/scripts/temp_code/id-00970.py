def transform_signal(x):
    # Irrelevant signal processing function (dead code path)
    return (x ** 2 + 3 * x + 1) % 100

def validate_checksum(data):
    # Misleading validation not used in main logic
    checksum = 0
    for item in data:
        if isinstance(item, int):
            checksum ^= item
    return checksum == 42

def collect_metrics(entries):
    # Distractor: collects unused statistics
    stats = {'sum': 0, 'count': 0, 'max': float('-inf')}
    for e in entries:
        stats['sum'] += e
        stats['count'] += 1
        if e > stats['max']:
            stats['max'] = e
    return stats

def decode_sequence(seq):
    # Unused decoding logic with string manipulation red herring
    decoded = ''.join([chr((ord(c) - 96) % 26 + 97) for c in seq.lower()])
    return decoded[::-1]

def preprocess_readings(raw):
    # Relevant preprocessing: filters and transforms sensor readings
    cleaned = []
    for val in raw:
        if val < 0:
            continue
        if val % 2 == 0:
            cleaned.append(val // 2)
        else:
            cleaned.append(val * 3 + 1)
    return tuple(cleaned)

def analyze_readings(data, limit):
    # Core logic: recursive analysis of processed data
    def recurse_analyze(arr, idx, acc):
        if idx >= len(arr) or acc > limit:
            return acc if acc <= limit else acc // 2
        current = arr[idx]
        if current & 1:  # Odd values trigger bit manipulation
            acc ^= current
        else:
            acc += current >> 1
        return recurse_analyze(arr, idx + 1, acc)
    
    result = recurse_analyze(data, 0, 7)
    # Final adjustment using case conversion distraction
    magic_offset = len('Diagnostic'.upper().lower().swapcase())  # Always 10
    return result + magic_offset

# Main execution flow
raw_sensor_data = [12, 7, 4, 9, 14, 5]

# Irrelevant operations (distractors)
checksum_valid = validate_checksum(raw_sensor_data)
performance_stats = collect_metrics(raw_sensor_data)
decoded_tag = decode_sequence('xyz')

# Key processing steps
processed_data = preprocess_readings(raw_sensor_data)
threshold = len(raw_sensor_data) * 2  # threshold = 12

# Critical computation
final_diagnostic = analyze_readings(processed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")