from functools import reduce

class SignalProcessor:
    def __init__(self):
        self.state = 0b1010
        self.transition_count = 0
    
    def process_signal(self, signal):
        # State transition logic with bitwise operations
        if signal & 0b1:
            self.state = (self.state << 1) & 0xF
        else:
            self.state = (self.state >> 1) | ((self.state & 0b1) << 3)
        
        # Additional state modification using XOR
        self.state ^= signal
        
        # Conditional update based on logical operations
        if (self.state > 0b1000) and not (signal & 0b10):
            self.state |= 0b1000
        elif (self.state < 0b0100) or (signal & 0b100):
            self.state &= 0b0111
        
        self.transition_count += 1
        return self.state

def simulate_circuit(input_sequence):
    processor = SignalProcessor()
    states = []
    
    for sig in input_sequence:
        current_state = processor.process_signal(sig)
        states.append(current_state)
    
    # Final state calculation using reduction
    final_state = reduce(lambda x, y: x ^ y, states, 0)
    return final_state

# Input sequence representing signal transitions
signals = [0b001, 0b010, 0b100, 0b011, 0b110]
final_state = simulate_circuit(signals)
print(f"Result: {final_state}")