def filter_noise(signal, threshold):
    """Filter out values below noise threshold"""
    return list(filter(lambda x: abs(x) >= threshold, signal))

def calculate_metrics(signal):
    """Calculate signal metrics that aren't used in final processing"""
    if not signal:
        return 0, 0, 0
    avg = sum(signal) / len(signal)
    peak = max(abs(x) for x in signal)
    variance = sum((x - avg) ** 2 for x in signal) / len(signal)
    return avg, peak, variance

def process_signal(signal, noise_threshold):
    """Process signal data by filtering and transforming"""
    # Apply initial noise filtering
    filtered = filter_noise(signal, noise_threshold)
    
    # Calculate metrics (not directly used in result)
    avg, peak, variance = calculate_metrics(filtered)
    
    # Apply frequency domain transformation (simulated)
    freq_domain = [x * (-1 if i % 2 else 1) for i, x in enumerate(filtered)]
    
    # Track processing history (not used in final calculation)
    processing_steps = [
        f"Filtered: {len(filtered)} points",
        f"Average: {avg:.2f}",
        f"Peak: {peak:.2f}"
    ]
    
    # Apply signal amplification based on position
    amplified = []
    for i, value in enumerate(freq_domain):
        position_factor = (i + 1) / len(freq_domain)
        modified = value * position_factor
        amplified.append(modified)
    
    # Final aggregation - sum of amplified values
    result = sum(amplified)
    
    # Apply normalization factor
    normalization = 10 / (len(amplified) if amplified else 1)
    return round(result * normalization, 2)

# Signal data and parameters
data = [3, -1, 4, -2, 7, 0, -3, 5]
noise_threshold = 2

# Calculate some auxiliary metrics that aren't used
dummy_max = max(data)
dummy_min = min(data)
dummy_range = dummy_max - dummy_min

# Process the signal data
processed_data = process_signal(data, noise_threshold)

# Format and print the result
print(f"Result: {processed_data}")