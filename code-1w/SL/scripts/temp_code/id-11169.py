def compute_integrity_code(sequence, mask=0xABC):
    # Initialize tracking and working variables
    history = {}
    temp_sum = 0
    running_xor = 0
    checksum = 0
    
    # Precompute auxiliary values (some not used)
    seq_length = len(sequence)
    avg_val = sum(sequence) / seq_length if seq_length else 0
    offset = (seq_length * 7) % 256
    
    for i, val in enumerate(sequence):
        # Irrelevant tracking: stores data but not used in final result
        history[i] = {
            'raw': val,
            'shifted': val >> (i % 4),
            'masked': val & mask
        }
        
        # Simulate sensor drift correction (unused in logic)
        corrected = val - (i * 0.01)
        temp_sum += int(corrected)
        
        # Core processing with meaningful operations
        clamped_val = max(1, min(val, 255))  # Ensure byte-range
        processed_value = (clamped_val ^ (i % 17)) & 0xFF
        
        # State update with bit manipulation
        checksum = (checksum << 1) ^ processed_value
        checksum &= 0xFFFF  # Keep within 16 bits
        
        # Secondary accumulator (distractor)
        running_xor ^= processed_value
        
    # Additional red herring computations
    final_ratio = running_xor / (temp_sum + 1)
    adjustment = int(final_ratio * 100) & 0xFF
    checksum = (checksum + adjustment) % 65536
    
    # Output target variable
    print(f"Result: {checksum}")

# Execute with deterministic input
sequence_data = [120, 85, 190, 47, 203, 77]
compute_integrity_code(sequence_data)