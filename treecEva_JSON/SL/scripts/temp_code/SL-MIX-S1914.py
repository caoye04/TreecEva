import itertools
import re

def analyze_encrypted_blocks():
    hex_blocks = ['0x1A3F', '0x7B2C', '0xB4E1', '0x2F9D']
    xor_accumulator = 0
    pattern_matches = {}
    
    # Process each hex block
    for idx, block in enumerate(hex_blocks):
        # Convert hex to integer
        numeric_val = int(block, 16)
        
        # Apply XOR with accumulator
        xor_result = numeric_val ^ xor_accumulator
        xor_accumulator = xor_result
        
        # Check for specific bit patterns
        binary_str = bin(numeric_val)[2:].zfill(16)
        match_count = len(re.findall(r'101', binary_str))
        pattern_matches[idx] = match_count
    
    # Statistical transformation using matched patterns
    stats_map = {k: v * 3 + 1 for k, v in pattern_matches.items()}
    
    # Find maximum value in stats_map
    max_stat = max(stats_map.values())
    
    # Combine results using set operations
    even_keys = {k for k in stats_map if stats_map[k] % 2 == 0}
    high_value_keys = {k for k in stats_map if stats_map[k] > 10}
    intersection_keys = even_keys & high_value_keys
    
    # Final computation
    final_hash_component = xor_accumulator
    for key in sorted(intersection_keys):
        final_hash_component += stats_map[key] << key
    
    return final_hash_component

final_hash_component = analyze_encrypted_blocks()
print(f"Result: {final_hash_component}")