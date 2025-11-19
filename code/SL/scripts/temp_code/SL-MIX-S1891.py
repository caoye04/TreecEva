from functools import wraps

def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

class SignalProcessor:
    def __init__(self):
        self.processed_samples = []
    
    @call_counter
    def is_peak(self, idx, samples):
        if idx == 0 or idx == len(samples)-1:
            return False
        return samples[idx] > samples[idx-1] and samples[idx] > samples[idx+1]
    
    def process_signal(self, raw_signal):
        detected_peaks = 0
        transformed = [(s * 3 + 7) % 16 for s in raw_signal]
        
        for i in range(len(transformed)):
            if self.is_peak(i, transformed) and (transformed[i] & 0b1010) != 0:
                detected_peaks += 1
                self.processed_samples.append(transformed[i])
        
        # Additional filtering based on processor state
        if self.is_peak.call_count > 0 and len(self.processed_samples) > 0:
            detected_peaks *= (self.is_peak.call_count % 5)
        else:
            detected_peaks = -1
            
        return detected_peaks

# Main execution
signal_data = [2, 8, 1, 9, 4, 6, 3, 7, 5, 0]
processor = SignalProcessor()
result = processor.process_signal(signal_data)
print(f"Result: {result}")