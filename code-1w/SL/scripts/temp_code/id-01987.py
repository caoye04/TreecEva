import math

# Simulated sensor data processing system with interference
raw_signals = [32, 64, 17, 45, 89, 23, 76, 54, 19, 88, 77, 41, 63, 91, 50]
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F']
noise_floor = 15
decoy_matrix = [[i * j for j in range(5)] for i in range(6)]

# Irrelevant transformation chain (dead path)
transform_cache = {}
def legacy_transform(x):
    if x in transform_cache:
        return transform_cache[x]
    result = 0
    for k in range(2, x // 2 + 1):
        if x % k == 0:
            result += k
    transform_cache[x] = result
    return result

# Unused recursive decoy
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Real signal filter based on dynamic thresholds
valid_ids = [i for i, val in enumerate(raw_signals) if val > noise_floor]
filtered_data = [raw_signals[i] for i in valid_ids if i % 2 == 0]

# Misleading intermediate calculation (no effect on final result)
weighted_sum = sum(val * (idx + 1) for idx, val in enumerate(filtered_data))
normalized_score = weighted_sum / len(filtered_data) if filtered_data else 0

# Threshold map generation with distractor logic
base_thresholds = {'low': 20, 'mid': 45, 'high': 70}
threshold_map = {}
for key, val in base_thresholds.items():
    # Complex but irrelevant adjustment
    adjusted = val + int(math.sin(math.radians(val)) * 10)
    threshold_map[key] = adjusted

# Decoy statistical analysis
stat_summary = {}
for label in dummy_labels:
    stat_summary[label] = {
        'count': len(decoy_matrix),
        'sum': sum(sum(row) for row in decoy_matrix)
    }

# Core processing function with nested logic
status_flags = []
def process_signals(data, thresholds):
    output = 0
    flag_log = []
    
    # Use of enumerate and zip as required
    for idx, val in enumerate(data):
        category = 'low'
        if val >= thresholds['mid']:
            category = 'mid'
        if val >= thresholds['high']:
            category = 'high'
        
        # Bit manipulation red herring
        bit_analysis = (val ^ 255) & 0xFF
        shift_adjusted = (bit_analysis >> 2) | (bit_analysis << 6)
        
        # Real contribution: modular arithmetic and conditional accumulation
        mod_key = (idx * 3 + 1) % 7
        if mod_key % 2 == 1:
            temp_offset = int(math.log(val + 1, 2))
            if category == 'high':
                temp_offset += 2
            elif category == 'mid':
                temp_offset += 1
            output += (val + temp_offset) % 13
        
        # Flag tracking (partially relevant)
        flagged = (category == 'high' and (val % 3 == 0))
        flag_log.append((idx, flagged))
    
    # Final transformation using string method (required feature)
    flag_str = ''.join(str(int(flag)) for _, flag in flag_log)
    padding_needed = (8 - len(flag_str) % 8) % 8
    padded_flag_str = flag_str + '0' * padding_needed
    
    # Chunk into bytes and extract control byte
    chunks = [padded_flag_str[i:i+8] for i in range(0, len(padded_flag_str), 8)]
    control_byte = sum(int(chunk, 2) for chunk in chunks) % 256
    
    # Update global flags
    nonlocal status_flags
    status_flags = flag_log
    
    # Final adjustment
    output = (output * 3) ^ control_byte
    return output

# Trigger secondary irrelevant list processing
reversed_pairs = list(zip(raw_signals[::-1], raw_signals))
median_approx = sorted(reversed_pairs, key=lambda x: abs(x[0] - x[1]))[len(reversed_pairs)//2]

# Actual execution path
final_output = process_signals(filtered_data, threshold_map)

# Print required result
print(f"Result: {final_output}")