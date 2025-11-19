from collections import defaultdict

class SignalProcessor:
    def __init__(self):
        self.register = 0b10101010
        self.accumulator = 0
        self.state = 'IDLE'
        self.transition_count = 0
    
    def process_signal(self, signal):
        if self.state == 'IDLE' and signal > 5:
            self.state = 'ACTIVE'
            self.register ^= (signal << 2)
        elif self.state == 'ACTIVE' and signal <= 5:
            self.state = 'LATCHED'
            self.register &= ~(signal | 0xF0)
        elif self.state == 'LATCHED' and signal % 3 == 0:
            self.state = 'IDLE'
            self.register |= (signal >> 1)
        
        self.accumulator = (self.accumulator + (self.register & 0xFF)) % 17
        self.transition_count += 1
        
signals = [7, 2, 9, 3, 6, 1, 8, 4]
processor = SignalProcessor()

for sig in signals:
    processor.process_signal(sig)
    
# Apply final transformation
if processor.transition_count % 2 == 0:
    processor.accumulator ^= 0x55
else:
    processor.accumulator &= 0xAA
    
print(f"Result: {processor.accumulator}")