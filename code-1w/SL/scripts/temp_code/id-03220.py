def analyze_pattern(seq):
    # Irrelevant analysis function (dead end)
    temp = [x ** 2 for x in seq if x % 2 == 0]
    stats = {'sum': sum(temp), 'max': max(temp) if temp else 0}
    return stats


def filter_edges(arr):
    # Distractor: complex slicing with no impact on final result
    left = arr[:len(arr)//2][::-1]
    right = arr[len(arr)//2:]
    combined = left + right
    # Red herring computation
    dummy_sum = sum([combined[i] * (i % 4) for i in range(len(combined))])
    return dummy_sum  # Unused return value


def transform_value(x, shift):
    # Bit manipulation distraction
    shifted = (x << 2) ^ 7
    masked = shifted & 0xFF
    return masked % 13


def compute_checksum(items):
    # Complex but irrelevant checksum
    chk = 0
    for i, v in enumerate(items):
        chk ^= (v + i * 3) % 256
    return chk


def evaluate_threshold(seq):
    # Another decoy path with conditional complexity
    if len(seq) > 5:
        mid = seq[len(seq)//2]
        if mid > 50:
            return sum(seq) // mid
        else:
            return seq.count(mid) * 10
    return -1


def process_sequence(raw_data):
    # Core logic hidden among distractions
    segment = raw_data[2:9:2]  # Slicing: indices 2,4,6,8
    
    # Multiple assignments and transformations
    a, b, c, d = segment  # Unpacking: values at indices 2,4,6,8 from raw_data
    
    # Actual relevant computation chain (8-12 steps)
    temp1 = a + b
    temp2 = temp1 * 2
    temp3 = temp2 - c
    temp4 = temp3 ^ d  # XOR operation
    temp5 = abs(temp4)  # Ensure positive
    temp6 = temp5 % 100
    temp7 = transform_value(temp6, 3)  # Reuses distractor function but only this call matters
    
    # Conditional branch affecting final output
    if temp7 > 10:
        final_adjust = 7
    else:
        final_adjust = 3
    
    result = temp7 + final_adjust
    
    # Critical red herring: multiple unused variables
    _ = filter_edges(raw_data)
    _ = compute_checksum(raw_data)
    _ = evaluate_threshold(raw_data)
    
    return result

# Main execution
if __name__ == '__main__':
    # Input data with meaningful structure
    sensor_readings = [15, 22, 44, 31, 58, 49, 26, 33, 14, 61, 77]
    
    # Irrelevant preprocessing
    normalized = [round(x / 1.7) for x in sensor_readings]
    scaled = [y * 2 for y in normalized]
    
    # Decoy function calls
    analysis = analyze_pattern(sensor_readings)
    edge_score = filter_edges(scaled)
    
    # Key assignment
    data = scaled  # Points to transformed data
    
    # Critical execution point
    result = process_sequence(data)
    
    # Output target result
    print(f"Target result: {result}")