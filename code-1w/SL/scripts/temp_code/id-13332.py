import math

def transform_value(x):
    if x <= 0:
        return 0
    log_val = math.log(x, 2)
    shifted = int(log_val * 100)
    return shifted ^ 543  # Irrelevant bit manipulation


def filter_anomalies(records):
    threshold = sum(r['metric'] for r in records) / len(records)
    filtered = [r for r in records if r['metric'] > threshold * 0.7]
    sorted_data = sorted(filtered, key=lambda r: r['timestamp'], reverse=True)
    return sorted_data  # Some are used, some not

def decode_sequence(seq):
    decoded = []
    for s in seq:
        if s.isdigit():
            decoded.append(int(s) ** 2)
        else:
            decoded.append(ord(s[0]) % 19)
    adjustment = sum(decoded) // len(decoded) if decoded else 0
    return [d + adjustment for d in decoded]  # Unused transformation

def compute_weighted_score(entries):
    weights = {k: v % 7 for k, v in enumerate([3, 7, 2, 9, 1, 5])}
    total = 0
    for i, e in enumerate(entries):
        factor = weights.get(i % 6, 1)
        total += e['value'] * factor
    return total

def evaluate_integrity(checksum, data):
    calculated = sum(data) % 1000
    return abs(calculated - checksum) < 50

def analyze_packet(payload):
    raw_parts = payload.split('|')
    numeric_data = [int(p) for p in raw_parts if p.isdigit()]
    stats = {
        'count': len(numeric_data),
        'sum': sum(numeric_data),
        'max': max(numeric_data),
        'min': min(numeric_data)
    }
    stats['range'] = stats['max'] - stats['min']
    stats['avg'] = stats['sum'] / stats['count']
    return stats

def process_pipeline(stream):
    # Parse and split stream
    segments = stream.split(',')
    parsed = [{'id': i, 'data': s} for i, s in enumerate(segments)]

    # Extract metrics (only some matter)
    extracted = []
    for p in parsed:
        val = 0
        if 'A' in p['data']:
            val += 17
        if 'X' in p['data']:
            val *= 2
        if 'Z' in p['data']:
            val += 41
        extracted.append({'index': p['id'], 'metric': val, 'timestamp': len(p['data'])})

    # Filter meaningful entries
    filtered_records = filter_anomalies(extracted)

    # Transform using irrelevant function
    _ = [transform_value(r['metric']) for r in filtered_records]

    # Real computation path
    base_values = [r['metric'] for r in filtered_records]
    weighted_input = [{'value': v * 3} for v in base_values]

    score = compute_weighted_score(weighted_input)

    # Decoy logic with string operations
    temp_str = ''.join(segments)
    case_swapped = temp_str.swapcase()
    split_back = case_swapped.split('x')
    _ = [len(part) for part in split_back if 'A' in part]

    # Final integrity check
    packet_analysis = analyze_packet(stream.replace(',', '|'))
    valid = evaluate_integrity(packet_analysis['sum'], base_values)

    final_adjustment = packet_analysis['avg'] if valid else 100
    intermediate = score + int(final_adjustment)

    # Critical execution point
    final_output = intermediate * 2  # This is the target

    print(f"Result: {final_output}")
    return final_output

# Simulated input
data_stream = "AXZ,BAZ,XAA,ZAB,BBX"

# Execution entry point
final_output = process_pipeline(data_stream)