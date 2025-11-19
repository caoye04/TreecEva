import math
from functools import wraps

def execution_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        return result
    wrapper.call_count = 0
    return wrapper

def hash_transform(text):
    hash_val = 0
    for char in text:
        hash_val = (hash_val * 31 + ord(char)) % 1000000
    return hash_val

@execution_tracker
def process_signal_frequencies(freq_data):
    # Apply logarithmic transformation
    log_freqs = [math.log(x) for x in freq_data if x > 0]
    # Apply exponential weighting
    weighted_freqs = [math.exp(y/10) for y in log_freqs]
    return sorted(weighted_freqs)

# Initialize signal data
raw_signals = [10, 100, 1000, 10000]
signal_labels = ['alpha', 'beta', 'gamma', 'delta']

# Process signals
processed_spectrum = process_signal_frequencies(raw_signals)

# Calculate hash-based identifier for the processing session
session_id = hash_transform('signal_processing_v2')

# Compute final metric combining execution count and data characteristics
final_metric = int(process_signal_frequencies.call_count * 
                  (sum(processed_spectrum) + math.log(session_id)))

print(f'Result: {final_metric}')