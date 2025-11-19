import math

class PrecisionHandler:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def apply_log_correction(self, value):
        return math.log(value) if value > 0 else 0

decay_constant = 0.5
initial_intensity = 100.0

with PrecisionHandler() as ph:
    exponential_decay = initial_intensity * math.exp(-decay_constant)
    adjusted_signal_intensity = ph.apply_log_correction(exponential_decay)

print(f"Result: {adjusted_signal_intensity}")