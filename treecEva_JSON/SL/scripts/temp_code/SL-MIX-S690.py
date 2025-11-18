from collections import defaultdict

def process_buffer_ops(ops_sequence):
    buffer_state = 0
    op_counts = defaultdict(int)
    
    for op_code in ops_sequence:
        op_counts[op_code] += 1
        
        # Switch-like dictionary mapping
        operation_map = {
            'XOR': lambda x: x ^ 0x5F,
            'ADD': lambda x: (x + 127) % 256,
            'ROT': lambda x: ((x << 3) | (x >> 5)) & 0xFF,
            'NEG': lambda x: (~x) & 0xFF
        }
        
        # Apply operation if exists, else do nothing
        buffer_state = operation_map.get(op_code, lambda x: x)(buffer_state)
        
        # Conditional update based on operation count
        buffer_state = buffer_state + 1 if op_counts[op_code] % 3 == 0 else buffer_state
    
    return buffer_state

# Main execution
operation_sequence = ['XOR', 'ADD', 'ROT', 'XOR', 'NEG', 'ADD', 'XOR', 'ROT', 'ADD']
intermediate_result = process_buffer_ops(operation_sequence)

# Additional processing with ternary operator and modular arithmetic
final_hash_state = (intermediate_result * 17 + 42) % 100 if intermediate_result > 100 else (intermediate_result * 23 + 73) % 100

print(f'Result: {final_hash_state}')