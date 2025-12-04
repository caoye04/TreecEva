def calculate_memory_blocks(data_patterns):
    # Distractor: Unused calculation for cache optimization
    cache_optimization = len(data_patterns) * 2 + 7
    
    # Distractor: Misleading bitwise operation
    bitwise_temp = cache_optimization ^ 0b1010
    
    # Main logic: Count valid memory blocks
    valid_blocks = 0
    for pattern in data_patterns:
        if isinstance(pattern, str) and len(pattern) > 3:
            upper_count = sum(1 for char in pattern if char.isupper())
            if upper_count % 2 == 0:
                valid_blocks += upper_count
    
    # Distractor: Irrelevant string processing
    temp_string = "memory_allocation_temp"
    string_length = len(temp_string) * 2 - 5
    
    return valid_blocks

def process_memory_blocks(memory_config):
    # Distractor: Unused dictionary operations
    config_copy = memory_config.copy()
    unused_value = config_copy.get('threshold', 15) * 3
    
    # Main logic: Process data patterns
    data_patterns = memory_config.get('patterns', [])
    if not data_patterns:
        # Dead code path
        default_capacity = 42
        return default_capacity
    
    # Calculate base capacity
    base_capacity = calculate_memory_blocks(data_patterns)
    
    # Apply scaling factors
    scaling_factor = memory_config.get('scaling', 1.5)
    final_value = base_capacity * scaling_factor
    
    # Distractor: Misleading intermediate calculation
    temp_adjustment = final_value + len(data_patterns) * 0.25
    
    # Apply final adjustments
    if base_capacity > 10:
        final_capacity = final_value + 2.5
    else:
        final_capacity = final_value - 1.0
    
    # Distractor: Another unused operation
    unused_bitmask = int(final_capacity) & 0xFF
    
    return final_capacity

# Main execution
memory_map = {
    'patterns': ['RAMBlock1', 'CacheA2', 'MemoryUnitB3', 'StorageC4'],
    'scaling': 2.0,
    'threshold': 20
}

# Distractor: Unrelated calculation
unused_total = sum(range(1, 10))

# Target statement
final_capacity = process_memory_blocks(memory_map)

print(f"Target result: {final_capacity}")