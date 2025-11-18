from collections import deque

def simulate_circuit():
    signals = deque([0b1101, 0b1011, 0b0110, 0b1001])
    accumulated_signal = 0b0000
    
    while signals:
        current_signal = signals.popleft()
        # Simulate XOR gate
        accumulated_signal ^= current_signal
        
        # Simulate AND gate with a mask
        mask = 0b1111
        accumulated_signal &= mask
    
    return accumulated_signal

accumulated_signal = simulate_circuit()
print(f"Result: {accumulated_signal}")