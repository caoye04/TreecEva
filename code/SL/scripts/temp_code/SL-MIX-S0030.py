from collections import deque

def process_signals(signal_stream):
    state = 'INIT'
    accumulator = 0
    key_rotation = deque([3, 7, 11, 5])
    processed_count = 0
    
    for signal in signal_stream:
        if state == 'INIT':
            if signal < 0:
                state = 'ERROR'
                break
            else:
                state = 'PROCESS'
        
        if state == 'PROCESS':
            key = key_rotation[0]
            accumulator ^= (signal & key)
            key_rotation.rotate(-1)
            processed_count += 1
            
            if processed_count >= 3:
                state = 'FINALIZE'
                break
    
    if state == 'FINALIZE':
        accumulator &= 0xFF  # Mask to 8 bits
        accumulator |= (accumulator >> 4) & 0x0F
    
    return accumulator

signal_data = [15, 29, 42, 8]
final_accumulator = process_signals(signal_data)
print(f"Result: {final_accumulator}")