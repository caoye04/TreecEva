from collections import defaultdict

def encrypt_phase(state, depth=0):
    if depth == 4:
        return state
    # Bitwise transformation based on depth
    next_state = (state << 1) ^ (state >> 2) & 0xFF
    # Recursive call with modified state
    return encrypt_phase(next_state, depth + 1)

class EncryptionMachine:
    def __init__(self):
        self.phase = 0
        self.state = 0b10101010
        self.checksum = 0.0
    
    def run(self):
        while self.phase < 3:
            match self.phase:
                case 0:
                    self.state = encrypt_phase(self.state)
                    self.phase += 1
                case 1:
                    # Apply floating-point transformation
                    self.state = int((self.state * 1.5) + 0.5) & 0xFF
                    self.phase += 1
                case 2:
                    # Final checksum calculation
                    self.checksum = float(self.state ^ 0b11110000)
                    self.phase += 1
                case _:
                    break

# Initialize and run encryption machine
machine = EncryptionMachine()
machine.run()
print(f"Result: {int(machine.checksum)}")