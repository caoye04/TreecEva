class SignalBuffer:
    def __init__(self):
        self.window = [0, 0, 0]
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.window.clear()
        
    def update(self, value):
        self.window = self.window[1:] + [value]
        return self.window[0]  # Return oldest value

# Lambda for signal thresholding
threshold_filter = lambda x: x if x > 10 else 0

# Modified Fibonacci generator with bitwise transformation
def modified_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        next_val = a + b
        # Apply bitwise XOR with 7 and then AND with 15
        transformed = (next_val ^ 7) & 15
        yield transformed
        a, b = b, next_val

# Process signal sequence
with SignalBuffer() as buffer:
    signal_values = list(modified_fibonacci(12))
    processed_signals = []
    
    for i, val in enumerate(signal_values):
        # Apply threshold filter and accumulate with arithmetic operations
        filtered = threshold_filter(val)
        if i > 0 and processed_signals:  # Short-circuit evaluation
            accumulated = (filtered * 2) + (processed_signals[-1] // 2 if processed_signals[-1] != 0 else 0)
        else:
            accumulated = filtered * 2
        
        # Update buffer and store processed value
        oldest = buffer.update(accumulated)
        processed_signals.append(accumulated)
    
    # Calculate peak value using arithmetic operations on buffered data
    signal_peak = sum(buffer.window) + (max(processed_signals) if processed_signals else 0) * 3

print(f"Result: {signal_peak}")