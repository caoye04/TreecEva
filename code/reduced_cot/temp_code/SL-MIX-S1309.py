import re

def textile_qc_processor(batch_codes):
    # State definitions
    states = {'INIT': 0, 'INSPECTING': 1, 'TREATING': 2, 'PACKING': 3}
    current_state = states['INIT']
    
    # Lambda functions for transformations
    transform_ops = [
        lambda x: (x << 1) & 0xFF,
        lambda x: x ^ 0xAA,
        lambda x: (x + 17) % 256,
        lambda x: x | 0x0F
    ]
    
    score_accumulator = 0
    
    for code_str in batch_codes:
        # Extract numeric value from hex string using pattern matching
        match = re.match(r'0x([0-9A-F]{2})', code_str)
        if not match:
            continue
        base_value = int(match.group(1), 16)
        
        # Apply state-based transformation sequence
        temp_value = base_value
        for i in range(len(transform_ops)):
            temp_value = transform_ops[i](temp_value)
            
        # Update state machine (cycle through states)
        current_state = (current_state + 1) % len(states)
        
        # Accumulate scores with state weighting
        score_accumulator += temp_value * (current_state + 1)
    
    # Final adjustment using arithmetic operations
    final_score = (score_accumulator // 4) - sum(range(1, 5))
    return final_score

# Process the textile batches
batch_identifiers = ['0xA3', '0x5F', '0xC8', '0x91']
final_score = textile_qc_processor(batch_identifiers)
print(f"Result: {final_score}")