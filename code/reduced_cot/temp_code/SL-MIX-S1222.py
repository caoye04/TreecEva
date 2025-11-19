def call_tracker(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

class SignalContext:
    def __init__(self, initial_state):
        self.state = initial_state
    
    def __enter__(self):
        self.state = (self.state * 3) % 7
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.state = (self.state + 5) % 7

def process_transform(signal_value):
    transforms = {
        'amplify': lambda x: (x * 2) % 13,
        'attenuate': lambda x: (x * 9) % 13,  # 9 is modular inverse of 2 mod 13
        'invert': lambda x: (-x) % 13
    }
    
    # Dictionary comprehension with conditionals
    active_transforms = {k: v for k, v in transforms.items() if len(k) > 6}
    
    result = signal_value
    for transform_func in active_transforms.values():
        result = transform_func(result)
    
    return result

@call_tracker
def apply_modulation(base_freq, modulation_index):
    return (base_freq + modulation_index * 3) % 11

# Main execution
initial_signal = 4
frequency = 7
mod_index = 2

with SignalContext(initial_signal) as ctx:
    adjusted_signal = ctx.state
    processed_signal = process_transform(adjusted_signal)
    
    # Nested logical operations
    if (processed_signal > 5) and not (frequency <= 5 or mod_index == 3):
        processed_signal = (processed_signal + apply_modulation(frequency, mod_index)) % 13
    elif (processed_signal <= 5) or (frequency > 8 and mod_index != 1):
        processed_signal = (processed_signal * 3) % 13
    else:
        processed_signal = (processed_signal - 2) % 13

print(f"Result: {processed_signal}")