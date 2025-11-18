def adaptive_filter(samples, window_base):
    if len(samples) == 0:
        return 0
    
    current_sample = samples[0]
    remaining_samples = samples[1:]
    
    # Recursive call to process remaining samples
    prev_filtered = adaptive_filter(remaining_samples, window_base)
    
    # Calculate dynamic window size using previous output
    dynamic_window = (window_base + abs(prev_filtered)) % 13 + 1
    
    # Apply modular arithmetic filtering
    filtered_output = (current_sample + prev_filtered * 2) % dynamic_window
    
    return filtered_output

def process_signal():
    audio_samples = [7, -3, 12, -8, 5]
    base_window = 9
    result = adaptive_filter(audio_samples, base_window)
    return result

# Main execution
filtered_output = process_signal()
print(f"Result: {filtered_output}")