def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

def modified_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a + b) * 2
    return b

@call_counter
def process_signal(raw_signal):
    base_strength = modified_fibonacci(raw_signal)
    encoded_metadata = ''.join(chr(ord(c) + 1) for c in "SIG")
    return base_strength if base_strength > 100 else base_strength * 3

signal_readings = [3, 4, 5]
signal_processor = lambda x: process_signal(x) if x > 3 else process_signal(x) * 2
processed_signals = {f'band_{i}': signal_processor(i) for i in signal_readings}

final_encoded_strength = sum(processed_signals.values()) * (1 if processed_signals['band_5'] > 500 else -1)
print(f'Result: {final_encoded_strength}')