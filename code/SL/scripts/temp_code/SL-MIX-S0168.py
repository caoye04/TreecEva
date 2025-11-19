import math
from collections import deque

def process_packets():
    # Initialize state machine and data structures
    state = 0
    signature_stack = [0x1A, 0x2B, 0x3C]
    byte_queue = deque([0x4D, 0x5E, 0x6F, 0x70])
    anomaly_score = 0
    
    # Process packet bytes through state machine
    while byte_queue and state < 3:
        current_byte = byte_queue.popleft()
        
        if state == 0:
            # Initial transformation with XOR and bit shift
            transformed = (current_byte ^ signature_stack[-1]) << 1
            if transformed > 0xFF:
                state = 1
                continue
            signature_stack.append(transformed & 0xFF)
            
        elif state == 1:
            # Apply exponentiation and logarithmic scaling
            if current_byte == 0:
                break
            exp_val = pow(current_byte, 2)  # Exponentiation
            log_val = int(math.log2(exp_val)) if exp_val > 0 else 0  # Logarithm
            signature_stack.append(log_val)
            if log_val > 10:
                state = 2
                continue
                
        elif state == 2:
            # Final computation with bitwise AND/OR operations
            prev_signature = signature_stack.pop()
            and_result = prev_signature & 0x0F
            or_result = (current_byte | 0x30) & 0x7F
            anomaly_score = and_result ^ or_result
            break
            
        state += 1
    
    # Post-processing with generator expression and functional programming
    scaled_scores = (score * 2 for score in signature_stack if score > 0x20)
    filtered_sum = sum(filter(lambda x: x < 0xE0, scaled_scores))
    
    # Final anomaly score calculation
    if filtered_sum > 0:
        anomaly_score ^= (filtered_sum & 0xFF)
    
    return anomaly_score

# Execute packet processing
anomaly_score = process_packets()
print(f"Result: {anomaly_score}")