from collections import Counter

def process_operations(data_sequence):
    # Primary operation: XOR-based filtering with set operations
    temp_xor = 0
    for value in data_sequence:
        temp_xor ^= value
    
    # Distractor: Unused calculation with misleading logic
    irrelevant_sum = sum([x * 2 for x in data_sequence if x % 3 == 0])
    dead_code_multiplier = len(data_sequence) * 7
    
    # Secondary operation: Bit manipulation with set intersection
    threshold = temp_xor & 0b1111
    valid_values = {x for x in data_sequence if (x | threshold) > 12}
    
    # More distractions: Counter operations that don't affect final result
    frequency_counter = Counter(data_sequence)
    common_items = frequency_counter.most_common(2)
    fake_result = common_items[0][1] if common_items else 0
    
    # Core logic: Filtered XOR calculation with arithmetic
    filtered_xor = 0
    for num in valid_values:
        filtered_xor ^= num
        
    # Final computation with arithmetic combination
    base_value = filtered_xor + (threshold << 2)
    
    # Dead code path that looks important but isn't used
    if base_value > 100:
        alternative_result = base_value // 3
    else:
        alternative_result = base_value * 2
    
    return base_value

def main():
    # Input sequence with deliberate pattern
    data_sequence = [8, 15, 23, 42, 8, 15, 7, 19, 42]
    
    # Execute the core operation
    final_result = process_operations(data_sequence)
    
    # Print the target result
    print(f"Result: {final_result}")

if __name__ == "__main__":
    main()