from collections import Counter

def compute_data_integrity(data_entries):
    # Distractor: Unused bitwise operations
    mask_shift = (0xFF << 3) & 0x7F
    redundant_check = mask_shift ^ 0b101010
    
    # Actual processing logic
    frequency_map = Counter(data_entries)
    
    # Distractor: Misleading intermediate calculation
    temp_sum = sum(len(str(x)) for x in data_entries) * 17
    
    # Core integrity computation
    unique_values = sorted(set(data_entries))
    hash_base = 0
    
    for idx, value in enumerate(unique_values):
        # Distractor: Dead code path
        if value > 1000:
            hash_base += value >> 2  # Never executed in this dataset
        
        # Actual hash accumulation
        hash_base = (hash_base * 31 + value) % 1000000
        
        # Distractor: Redundant operation
        shadow_var = hash_base | 0xFFFF
    
    # Final hash calculation with bit manipulation
    frequency_factor = sum(freq ** 2 for freq in frequency_map.values())
    integrity_hash = (hash_base ^ frequency_factor) % 10000
    
    # Distractor: Unused result
    validation_check = integrity_hash + temp_sum
    
    return integrity_hash

# Main execution with mixed data
sample_items = [42, 17, 42, 89, 17, 23, 42, 89, 17, 42]
processed_items = [x * 2 if x % 2 == 0 else x + 1 for x in sample_items]

# Distractor: Misleading computation path
secondary_analysis = [x // 3 for x in processed_items]
shadow_total = sum(secondary_analysis) * 8

# Target computation
final_hash = compute_data_integrity(processed_items)

# Distractor: Unrelated output
print(f"Secondary analysis sum: {shadow_total}")
print(f"Target result: {final_hash}")