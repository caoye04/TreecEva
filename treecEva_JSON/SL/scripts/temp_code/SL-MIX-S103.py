import math

def process_compression_stream(stream_data):
    states = ['init', 'proc', 'comp', 'flush']
    current_state = 0  # Index into states
    encoded_sum = 0
    
    for idx, value in enumerate(stream_data):
        state_name = states[current_state]
        
        if state_name == 'init':
            # Apply XOR with index and shift
            transformed = (value ^ idx) << 1
            encoded_sum += transformed
            # Transition based on a greedy condition
            if transformed > 10:
                current_state = 1
            else:
                current_state = 2
                
        elif state_name == 'proc':
            # Apply logarithmic weighting
            if value > 0:
                weighted = int(math.log(value) * 10)
                encoded_sum += weighted & 0xFF  # Mask to byte
            else:
                encoded_sum += 1
            # Check for early termination condition
            if value == 0:
                break
            # State transition using divide and conquer logic on index
            if idx < len(stream_data) // 2:
                current_state = 2
            else:
                current_state = 3
                
        elif state_name == 'comp':
            # Bitwise OR with exponentiation
            exp_val = min(10, value)  # Prevent overflow
            encoded_sum |= (2 ** exp_val)
            # Greedy state selection
            utility_a = math.log(encoded_sum + 1) if encoded_sum > 0 else 0
            utility_b = math.log(value + 1) if value > 0 else 0
            if utility_a > utility_b:
                current_state = 0
            else:
                current_state = 1
                
        elif state_name == 'flush':
            # Finalize with AND operation
            encoded_sum &= 0xFFFF  # Mask to 16-bit
            # No further transitions
            break
    
    return encoded_sum

# Input data for the compression stream
input_sequence = [7, 3, 12, 0, 5]

# Execute the compression process
final_encoded_value = process_compression_stream(input_sequence)
print(f"Result: {final_encoded_value}")