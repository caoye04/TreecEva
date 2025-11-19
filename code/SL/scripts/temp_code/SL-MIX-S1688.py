from collections import defaultdict

def process_fabric_batch(inspections):
    # State machine states: 'START', 'DEFECT_TRACKING', 'PASS_MONITORING'
    state = 'START'
    defect_streak = 0
    pass_streak = 0
    score = 0
    
    for report in inspections:
        token_value = 0
        binary_str = bin(report)[2:]  # Convert to binary string without '0b' prefix
        
        for bit in binary_str:
            if state == 'START':
                if bit == '1':
                    state = 'DEFECT_TRACKING'
                    defect_streak = 1
                else:
                    state = 'PASS_MONITORING'
                    pass_streak = 1
            elif state == 'DEFECT_TRACKING':
                if bit == '1':
                    defect_streak += 1
                else:
                    token_value += defect_streak * defect_streak
                    state = 'PASS_MONITORING'
                    pass_streak = 1
                    defect_streak = 0
            elif state == 'PASS_MONITORING':
                if bit == '0':
                    pass_streak += 1
                else:
                    if pass_streak > 3:
                        token_value -= pass_streak
                    state = 'DEFECT_TRACKING'
                    defect_streak = 1
                    pass_streak = 0
        
        # Handle terminal state
        if state == 'DEFECT_TRACKING' and defect_streak > 0:
            token_value += defect_streak * defect_streak
        elif state == 'PASS_MONITORING' and pass_streak > 3:
            token_value -= pass_streak
            
        score += token_value
        
        # Reset for next report
        state = 'START'
        defect_streak = 0
        pass_streak = 0
    
    return score

# Fabric inspection reports encoded as integers
fabric_reports = [0b1100101010001110, 0b1110001011100011, 0b1010101010101010, 0b1111000011110000]

final_score = process_fabric_batch(fabric_reports)
print(f"Result: {final_score}")