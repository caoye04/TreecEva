from collections import defaultdict

def process_signals():
    signals = [0b1101, 0b1010, 0b0110, 0b1001]
    register = 0b10101010
    accumulator = 0
    
    op_counts = defaultdict(int)
    
    for i, signal in enumerate(signals):
        # Control logic using switch-like dictionary
        control_op = (signal >> 2) & 0b11  # Extract bits 2-3
        
        operations = {
            0: lambda x, y: x & y,      # AND operation
            1: lambda x, y: x | y,      # OR operation
            2: lambda x, y: x ^ y,      # XOR operation
            3: lambda x, y: ((x << 1) & 0xFF) | (y >> 7)  # Shift left x, shift right y, combine
        }
        
        # Apply operation
        if control_op in operations:
            result = operations[control_op](register, signal)
            op_counts[control_op] += 1
        else:
            result = register
        
        # Update register
        register = result
        
        # Accumulate based on operation type and position
        accumulator += (result & 0xF) * (i + 1)
    
    # Final adjustment based on operation counts
    unique_ops = frozenset(op_counts.keys())
    if len(unique_ops) >= 3:
        accumulator ^= 0xFF
    
    return accumulator

accumulator = process_signals()
print(f"Result: {accumulator}")