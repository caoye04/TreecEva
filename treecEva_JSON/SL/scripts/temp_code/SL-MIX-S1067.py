class SignalBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def push(self, val):
        if len(self.buffer) < self.size:
            self.buffer.append(val)
        else:
            self.buffer.pop(0)
            self.buffer.append(val)
    
    def get_buffer(self):
        return self.buffer[:]

# Signal transformation lambda using modular arithmetic
transform_signal = lambda x, mod_base: (x * 3 + 7) % mod_base

# Initialize variables
processed_signal_strength = 0
threshold = 50
modulus_base = 17

with SignalBuffer(5) as buf:
    input_signals = [4, 9, 2, 8, 1, 7, 3, 6]
    
    for i in range(len(input_signals)):
        current_signal = input_signals[i]
        transformed = transform_signal(current_signal, modulus_base)
        buf.push(transformed)
        
        # Nested loop to compute signal strength
        inner_sum = 0
        for j in range(i+1):
            if j >= len(buf.get_buffer()):
                break
            inner_sum += buf.get_buffer()[j] * (j + 1)
        
        processed_signal_strength = (processed_signal_strength + inner_sum) % modulus_base
        
        # Early termination condition
        if processed_signal_strength > threshold:
            break

print(f"Result: {processed_signal_strength}")