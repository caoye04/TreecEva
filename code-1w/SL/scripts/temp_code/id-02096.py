import math

# Simulated sensor data processing pipeline with red herrings
def analyze_signal(x):
    if x < 0:
        return abs(x) * 2
    else:
        return x + 1

# Irrelevant helper - decoy function (never called in critical path)
def deprecated_filter(arr):
    return [a for a in arr if a % 2 == 0]

# Bit manipulation distraction
def shift_cipher(n):
    temp = n << 3
    temp ^= 255
    temp >>= 2
    return temp  # Unused in final logic

# Recursive sum with conditional base case (partially relevant)
def recursive_sum(seq, index=0):
    if index >= len(seq):
        return 0
    if seq[index] == 0:
        return recursive_sum(seq, index + 1)
    return seq[index] + recursive_sum(seq, index + 1)

# Real transformation chain
def transform_value(v, mode=True):
    if mode:
        v = int(math.sqrt(v)) if v > 100 else v // 2
    else:
        v = v ** 0.5
    return v + 10

# Dead-end combinatorics function
def count_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == 10:
                count += 1
    return count  # Never used

# Core data processor
def process_element(e, flag):
    if e % 3 == 0 and flag:
        e = transform_value(e)
    elif e % 5 == 0:
        e = analyze_signal(e)
    else:
        e = e - 7
    return e ^ 13

# Higher-order orchestrator with slicing distraction
def process_sequence(raw_data):
    # Slice to mislead about importance of sub-segments
    segment_a = raw_data[::2]
    segment_b = raw_data[1::2]
    temp_result = []
    
    # Mixed processing with conditional expression
    for i, val in enumerate(segment_a):
        computed = process_element(val, flag=(i % 2 == 0))
        temp_result.append(computed)
    
    # Fake aggregation
    dummy_agg = sum([x * 0.1 for x in segment_b])  # Distractor
    offset = int(dummy_agg % 10) if dummy_agg > 5 else 5
    
    # Actual key computation
    main_vals = [raw_data[j] for j in range(0, len(raw_data), 3)]
    adjusted = [transform_value(v, mode=False) for v in main_vals]
    base_total = recursive_sum(adjusted)
    
    # Final adjustment using bitwise and arithmetic
    checksum = 0
    for x in adjusted:
        checksum = (checksum ^ int(x)) & 0xFFFF
    
    # Critical statement
    final_output = (base_total + checksum) // 2 + offset
    
    # Red herring print (commented)
    # print('Debug:', final_output - 100)
    return final_output

# Simulated input data
sensor_readings = [144, 25, 9, 169, 45, 8, 225, 10, 12, 36]
data_chunk = [analyze_signal(x) for x in sensor_readings]

# Introduce unused transformed copy to distract
transformed_copy = data_chunk[::-1]  # Slicing but irrelevant

# Trigger dead code to mislead control flow understanding
if len(transformed_copy) > 5:
    _ = shift_cipher(len(transformed_copy))

# Execute core logic
final_output = process_sequence(data_chunk)
print(f"Result: {final_output}")