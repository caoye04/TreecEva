import itertools

def process_signal_chain():
    # Initialize state machine components
    state_flags = 0b1010
    signal_power = 0.0
    modulation_index = 3
    
    # Define transformation functions
    transform_ops = [
        lambda x, s: x ^ (s << 1),
        lambda x, s: x & ~(s >> 1),
        lambda x, s: x | (s ^ 0xF)
    ]
    
    # Process signal through state machine
    for cycle, adjustment in enumerate(itertools.cycle([0.5, -0.25, 0.75])):
        if cycle >= 6:
            break
            
        # Apply bitwise transformation based on current cycle
        op_index = cycle % len(transform_ops)
        state_flags = transform_ops[op_index](state_flags, cycle+1)
        
        # Update power measurement with floating point operations
        signal_power += (state_flags & 0x7) * adjustment
        
        # Conditional state modification
        if signal_power > 8.0:
            state_flags >>= 1
        elif signal_power < 0:
            state_flags <<= 1
            signal_power = abs(signal_power)
    
    return signal_power

# Execute processing pipeline
final_measurement = process_signal_chain()
print(f"Result: {final_measurement}")