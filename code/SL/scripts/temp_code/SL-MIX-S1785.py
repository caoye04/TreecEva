import itertools
from functools import reduce

def compute_waveform_signature(samples):
    # Compute pairwise differences between adjacent samples
    differences = [abs(b - a) for a, b in zip(samples[:-1], samples[1:])]
    
    # Apply threshold filter: only keep differences greater than threshold
    threshold = 2
    filtered_diffs = list(filter(lambda x: x > threshold, differences))
    
    # If no differences exceed threshold, return 0
    if not filtered_diffs:
        return 0
    
    # Calculate weighted sum using positions as weights
    weighted_sum = sum(pos * val for pos, val in enumerate(filtered_diffs, 1))
    return weighted_sum

# Audio sample data
audio_samples = [10, 15, 13, 20, 18, 25, 30, 28, 35]

# Process the waveform
waveform_signature = compute_waveform_signature(audio_samples)

# Apply normalization factor
normalization_factor = 1.5
normalized_signature = int(waveform_signature * normalization_factor)

# Generate sliding window averages of size 3 from normalized values
if len(audio_samples) >= 3:
    window_size = 3
    windows = [
        audio_samples[i:i+window_size] 
        for i in range(len(audio_samples) - window_size + 1)
    ]
    avg_window_values = [sum(window)//len(window) for window in windows]
else:
    avg_window_values = []

# Find maximum average window value
max_avg_window = max(avg_window_values) if avg_window_values else 0

# Final computation combines signature and window analysis
processed_signal_strength = (
    normalized_signature + 
    (max_avg_window if max_avg_window > 15 else 0) -
    len(list(itertools.takewhile(lambda x: x < 15, audio_samples)))
)

print(f"Result: {processed_signal_strength}")