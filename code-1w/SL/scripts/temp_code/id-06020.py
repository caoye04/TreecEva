from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation with noise filtering
def collect_sensor_data():
    raw_readings = [124, 127, 130, 135, 128, 124, 129, 131, 133, 136, 125, 123]
    filtered_readings = []
    for val in raw_readings:
        if val > 120 and val < 140:
            filtered_readings.append(val)
    return filtered_readings

# Irrelevant auxiliary function – dead code path
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Noise injection simulation – misleading distraction
temporary_buffer = [x ^ 0xCAFEBABE for x in range(8)]
decoy_checksum = sum(temporary_buffer) % 997

# Data transformation pipeline
def transform_readings(readings):
    transformed = []
    offset = 100
    for i, r in enumerate(readings):
        shifted = (r - offset) ** 2
        if i % 2 == 0:
            shifted = int(math.sqrt(shifted)) + 5
        else:
            shifted *= 2
        transformed.append(shifted)
    return transformed

# Complex pattern analyzer with multiple internal states
def analyze_pattern(data):
    state_log = defaultdict(int)
    history = []
    accumulator = 0
    
    for i, x in enumerate(data):
        if x < 30:
            state_log['low'] += 1
            accumulator += x * 1.5
        elif x < 40:
            state_log['medium'] += 1
            accumulator += x * 0.8
        else:
            state_log['high'] += 1
            accumulator -= 10
        
        # Nested conditional with red herring logic
        temp_flag = False
        if i > 0 and data[i] > data[i-1]:
            temp_flag = True
            decoy_value = (data[i] + data[i-1]) // 3  # unused
            if decoy_value > 20:
                for j in range(2):  # artificial nesting
                    pass
        
        # Bit manipulation side calculation – irrelevant
        bit_analysis = (x << 2) ^ 0xFF
        parity = bin(bit_analysis).count('1') % 2
        
        history.append({'index': i, 'val': x, 'parity': parity})
    
    # Core logic masked by distractions
    critical_sum = sum([h['val'] for h in history if h['parity'] == 1])
    adjustment = state_log['low'] * 3 - state_log['high'] * 2
    final_score = int(critical_sum + adjustment + accumulator)
    
    # Final computation – actual answer source
    validation_key = 4187
    final_diagnostic = (final_score * 3) ^ validation_key
    return final_diagnostic

# Unused statistical helper – distractor
def rolling_average(lst, window=3):
    avgs = []
    for i in range(len(lst) - window + 1):
        avgs.append(sum(lst[i:i+window]) / window)
    return avgs

# Main execution flow
if __name__ == '__main__':
    collected_data = collect_sensor_data()
    processed_data = transform_readings(collected_data)
    
    # Decoy analysis with no effect
    if len(processed_data) > 5:
        dummy_analysis = Counter(processed_data)
        anomaly_count = 0
        for k, v in dummy_analysis.items():
            if v > 1:
                anomaly_count += 1
    
    final_diagnostic = analyze_pattern(processed_data)
    print(f"Result: {final_diagnostic}")