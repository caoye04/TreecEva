from collections import deque

class SignalProcessor:
    def __init__(self):
        self.frequency_stack = []
        self.temporal_queue = deque()
        
    def process(self, frequencies, time_events):
        # Initialize structures
        for freq in frequencies:
            self.frequency_stack.append(freq)
        
        for event in time_events:
            self.temporal_queue.append(event)
        
        signal_strength = 0
        
        # Process using stack and queue
        while self.frequency_stack and self.temporal_queue:
            freq = self.frequency_stack.pop()
            time = self.temporal_queue.popleft()
            
            # Ternary operator determining amplification
            adjustment = freq * 2 if time % 2 == 0 else freq // 2
            
            # Logical operations for signal conditioning
            is_valid_freq = freq > 0 and freq < 1000
            is_peak_time = time > 5 or time < 2
            
            if is_valid_freq and not is_peak_time:
                signal_strength += adjustment
            elif is_valid_freq or is_peak_time:
                signal_strength -= adjustment // 4
        
        # Recursive refinement
        def refine(signal, depth):
            if depth == 0:
                return signal
            # Divide and conquer approach
            half = signal // 2
            return refine(half, depth - 1) + refine(signal - half, depth - 1)
        
        # Apply refinement
        refined_strength = refine(signal_strength, 3)
        
        # Final adjustment using lambda
        adjust_lambda = lambda x: x + 10 if x < 50 else x - 5
        final_signal_strength = adjust_lambda(refined_strength)
        
        return final_signal_strength

# Execute processing
processor = SignalProcessor()
frequencies = [100, 250, 500, 750]
time_events = [1, 4, 6, 8]

final_signal_strength = processor.process(frequencies, time_events)
print(f"Result: {final_signal_strength}")