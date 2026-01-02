from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation and health diagnostic system
def collect_telemetry():
    raw_streams = [
        'S1:3.2,5.1,2.8|S2:4.5,3.9|S3:6.0,5.8,6.1,5.9',
        'S1:3.0,3.1|S2:4.7|S3:6.2,6.0,5.8',
        'S1:2.9|S2:4.6,4.8,4.5|S3:5.9'
    ]
    
    # Irrelevant parsing path (dead code)
    legacy_buffer = {}
    for entry in raw_streams:
        for pair in entry.split('|'):
            sid, vals = pair.split(':')
            legacy_buffer[sid] = len(vals.split(','))  # Unused metric
    
    return raw_streams

# Misleading preprocessing function (not used in final computation)
def normalize_readings(data):
    normalized = []
    total_values = 0
    for stream in data:
        count = 0
        for segment in stream.split('|'):
            values = segment.split(':')[1].split(',')
            count += len(values)
        total_values += count
    scaling_factor = 1.0 / max(1, total_values - 5)  # Distractor logic
    return scaling_factor  # Never actually applied

# Core processing pipeline
def parse_streams(streams):
    parsed = defaultdict(list)
    char_counter = Counter()

    for stream in streams:
        char_counter.update(stream.replace(':', '').replace('|', ''))  # Red herring: counts characters

        segments = stream.split('|')
        for seg in segments:
            sensor_id, readings_str = seg.split(':')
            readings = [float(x) for x in readings_str.split(',')]
            parsed[sensor_id].extend(readings)
    
    # Decoy transformation
    transformed = {}
    for k, v in parsed.items():
        if len(v) > 2:
            transformed[k] = sum(x ** 0.5 for x in v if x > 3)  # Computed but unused

    # Actual relevant structure being built
    stats = {}
    for sid, vals in parsed.items():
        avg = sum(vals) / len(vals)
        variance = sum((x - avg) ** 2 for x in vals) / len(vals)
        stats[sid] = {'mean': avg, 'variance': variance}
    
    return stats, char_counter

def generate_health_signature(metrics):
    # Bit manipulation red herring
    signature = 0
    shift_count = 0
    for key in sorted(metrics.keys()):
        mean_val = metrics[key]['mean']
        truncated = int(mean_val * 10)
        signature ^= (truncated << (shift_count % 5))  # Complex but irrelevant to final result
        shift_count += 1

    # Real signal extraction (obscured)
    total_weight = 0.0
    adjustment = 0
    for m in metrics.values():
        total_weight += m['mean'] * (1 + m['variance'])  # Key contributor
        if m['variance'] < 0.5:
            adjustment += 1
    
    # Final signature includes adjustment
    return total_weight + adjustment

def calculate_entropy(count_dict):
    # Independent distractor function
    total = sum(count_dict.values())
    entropy = 0.0
    for count in count_dict.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def process_metrics(sig, data_map):
    # Multiple assignment red herring
    base, offset, multiplier = sig, len(data_map), 1.0
    
    # Fake error correction
    checksum = 0
    for i, val in enumerate(data_map.get('S1', [])):
        checksum += val * (i + 1)
    correction = abs(checksum) % 3.0  # Looks important, not used
    
    # Critical calculation hidden among distractions
    aggregate = 0.0
    for readings in data_map.values():
        # Nested logic with actual relevance
        filtered = [r for r in readings if r >= 3.0]
        if filtered:
            # Multi-step transformation
            squared_avg = sum(r**2 for r in filtered) / len(filtered)
            root_term = math.sqrt(squared_avg)
            aggregate += root_term * 0.75
    
    # Final integration with signature
    intermediate = sig * 0.8 + aggregate * 0.2
    
    # Destructuring distraction
    coords = (intermediate % 10, intermediate // 10, intermediate % 7)
    x, y, z = coords
    
    # Final answer depends only on intermediate and adjustment from earlier
    final_diagnostic = intermediate + y * 0.1
    
    # Dead code branch
    if final_diagnostic < 0:
        fallback = 0
        for k in sorted(data_map.keys()):
            fallback += len(data_map[k])
        final_diagnostic = fallback
    
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    # Initial data collection
    telemetry_data = collect_telemetry()
    
    # Parse into structured format
    sensor_metrics, char_freq = parse_streams(telemetry_data)
    
    # Generate diagnostic signature
    health_signature = generate_health_signature(sensor_metrics)
    
    # Calculate irrelevant entropy
    entropy_score = calculate_entropy(char_freq)  # Nowhere used
    
    # Normalize call (distractor)
    _ = normalize_readings(telemetry_data)  # Result ignored
    
    # Core diagnostic computation
    final_diagnostic = process_metrics(health_signature, sensor_metrics)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")