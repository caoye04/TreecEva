from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [127, 255, 192, 64, 31, 128, 95, 159]
    processed = []
    for val in raw_readings:
        if val & 128:  # Check high bit
            val ^= 128   # Toggle high bit
        if val > 100:
            val >>= 2    # Scale down large values
        processed.append(val)
    return processed

def apply_filter(data, mode='soft'):
    filtered = []
    buffer = defaultdict(int)
    temp_snapshot = []
    for i, x in enumerate(data):
        buffer[i] = x * 0.95
        adjusted = int(buffer[i])
        if mode == 'hard' and adjusted > 50:
            adjusted //= 2
        filtered.append(adjusted)
    
    # Irrelevant aggregation (distractor)
    stats = Counter(filtered)
    avg_freq = sum(stats.values()) / len(stats) if stats else 0
    
    # Dead code path - never executed due to mode
    if mode == 'extreme':
        filtered = [x**2 for x in filtered if x > 30]
    
    return filtered

def generate_sequence(n):
    # Unused function - red herring
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def transform_signal(values):
    result = []
    offset = len(values) // 2
    for i, v in enumerate(values):
        shifted = (v << 1) & 255
        if i % 2 == 0:
            shifted ^= 17
        result.append(shifted)
    # Additional transformation layer
    normalized = [round(x * 1.05) for x in result]
    return normalized[:offset + 3]  # Truncate to subset

def analyze_pattern(data, limit):
    score = 0
    history = []
    peak_magnitude = 0
    
    for idx, item in enumerate(data):
        # Complex conditional expression
        contribution = item if item < limit else (item // 3 if item % 2 == 0 else (item + 1) // 4)
        
        if contribution > 20:
            score += contribution
            history.append(contribution)
            
        # Bit manipulation side calculation (partially irrelevant)
        parity_check = bin(item).count('1') % 2
        debug_flag = True if parity_check else False
        
        # Update peak only under certain conditions
        if contribution > peak_magnitude and idx != 4:
            peak_magnitude = contribution
    
    # Secondary logic path with early termination condition
    if len(history) < 5:
        fallback = sum(data[i] for i in range(0, len(data), 2))
        score += fallback // 4
    
    # Final adjustment based on pattern shape
    if history and history[-1] > history[0]:
        score = int(score * 1.1)
    
    return score

# Main execution flow
sensor_data = collect_sensor_readings()
filtered_data = apply_filter(sensor_data, mode='soft')
transformed_data = transform_signal(filtered_data)

# Unused variables and misleading intermediate results
baseline_ref = sum(sensor_data) // len(sensor_data)
theoretical_max = max(transformed_data) * 2  # Not used in final computation

threshold = 75
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Spurious unrelated operations (distraction)
data_map = defaultdict(lambda: 'unknown')
for i in range(3):
    data_map[f'aux_{i}'] = generate_sequence(6)

# Noise injection (dead code)
if False:
    transformed_data.append(999)

print(f"Result: {final_diagnostic}")