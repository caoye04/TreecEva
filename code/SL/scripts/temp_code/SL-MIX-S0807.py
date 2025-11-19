import math

def hamming_window(n, N):
    return 0.54 - 0.46 * math.cos(2 * math.pi * n / (N - 1))

def process_signal(N, threshold):
    squared_sum = 0.0
    valid_count = 0
    
    for i in range(N):
        window_val = hamming_window(i, N)
        if window_val > threshold:
            squared_sum += window_val ** 2
            valid_count += 1
    
    # RMS calculation would be sqrt(squared_sum / valid_count)
    # But we want just the squared_sum
    return squared_sum

# Main processing
signal_length = 16
cutoff_threshold = 0.3

accumulated_energy = process_signal(signal_length, cutoff_threshold)

print(f"Result: {accumulated_energy}")