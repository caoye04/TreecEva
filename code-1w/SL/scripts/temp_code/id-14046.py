import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(math.sqrt(i) > 1 for i in x if i > 0)

# Misleading transformation chain
def decoy_transform(seq):
    temp = [x ** 2 for x in seq if x % 2 == 0]
    temp = [t - 5 for t in temp]
    return sorted(temp, reverse=True)

# Actual core logic disguised among distractors
def bitwise_weight(seq):
    total = 0
    for val in seq:
        if val > 0:
            # Bit manipulation mixed with arithmetic
            bits = bin(val).count('1')
            total += bits * (val % 7)
    return total

# String-based filtering mask (uses string method)
def create_mask(length):
    pattern = "101" * (length // 3 + 1)
    return [c == '1' for c in pattern[:length]]

# Core processing pipeline
def process_pipeline(raw_data):
    # Step 1: Initial slicing and filtering
    segment = raw_data[3:10]  # slicing operation
    
    # Irrelevant list transformations
    shadow_copy = [x + 10 for x in raw_data if x < 0]
    shadow_copy.extend([0] * (5 - len(shadow_copy)))
    
    # Step 2: Apply masking using string-generated pattern
    mask = create_mask(len(segment))
    filtered = [v for v, m in zip(segment, mask) if m]
    
    # Step 3: Decoy call (no side effects, but looks important)
    decoy_result = decoy_transform(filtered + [max(filtered) + 1])
    
    # Step 4: Real computation buried here
    aggregate = sum(filtered) // len(filtered) if filtered else 0  # integer division
    
    # Step 5: Use of bitwise logic on derived value
    binary_tag = bin(aggregate)[2:]
    parity_flip = binary_tag.count('1') - binary_tag.count('0')
    
    # Step 6: Combine with weighted bitwise sum from original segment
    weight_score = bitwise_weight(segment)
    
    # Step 7: Final obfuscated calculation
    adjustment = len(decoy_result) if decoy_result else 3
    intermediate = (weight_score + parity_flip) // adjustment
    
    # Step 8: Key assignment
    final_output = abs(intermediate * 17) - 4
    
    # Red herring: unused variable with plausible name
    diagnostic_trace = {
        'input_size': len(raw_data),
        'filtered_count': len(filtered),
        'noise_level': math.log(1 + abs(parity_flip))
    }
    
    return final_output

# Main execution block
if __name__ == '__main__':
    # Input data with meaningful structure
    data_chunk = [8, 12, -5, 3, 7, 14, 9, 2, 11, 6, 13, -1, 4]
    
    # Dead variable assignments (distractors)
    baseline_metrics = [x for x in data_chunk if x % 3 == 0]
    normalization_factor = sum(baseline_metrics) / len(baseline_metrics) if baseline_metrics else 1
    
    # Key statement
    final_output = process_pipeline(data_chunk)
    
    # Output result
    print(f"Target result: {final_output}")