from functools import reduce

def process_packets():
    # Packet security scores from initial scanning
    packet_scores = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
    
    # State machine definitions
    states = {
        'INIT': 0,
        'VALIDATE': 1,
        'TRANSFORM': 2,
        'SCORE': 3,
        'FINALIZE': 4
    }
    
    # Initialize state machine
    current_state = states['INIT']
    security_posture = 0x0F
    
    # Process each packet through state machine
    for idx, score in enumerate(packet_scores):
        # Early return for compromised packets
        if score & 0xF0 == 0x50:
            security_posture |= 0x80
            continue
            
        while current_state != states['FINALIZE']:
            if current_state == states['INIT']:
                # Transition to validation
                current_state = states['VALIDATE']
                
            elif current_state == states['VALIDATE']:
                # Check packet integrity with short-circuit evaluation
                if (score > 0x20) and (score < 0x60) or (score == 0x1A):
                    current_state = states['TRANSFORM']
                else:
                    security_posture &= ~0x0F
                    break
                    
            elif current_state == states['TRANSFORM']:
                # Apply bitwise transformation
                transformed = (score << 1) ^ (score >> 2)
                # Update score with functional approach
                adjusted_scores = list(map(lambda x: x ^ transformed, [score]))
                score = adjusted_scores[0]
                current_state = states['SCORE']
                
            elif current_state == states['SCORE']:
                # Calculate cumulative security posture
                temp_dict = {i: val for i, val in enumerate([security_posture, score])}
                merged_dict = {**temp_dict, **{2: score & 0x0F}}
                security_posture = reduce(lambda a, b: a ^ b, merged_dict.values())
                current_state = states['FINALIZE']
        
        # Reset state for next packet
        current_state = states['INIT']
    
    # Final adjustment based on packet count
    if len(packet_scores) >= 3 and security_posture != 0:
        security_posture ^= (len(packet_scores) << 4)
    
    return security_posture

# Execute the packet processing
final_security_value = process_packets()
print(f"Result: {final_security_value}")