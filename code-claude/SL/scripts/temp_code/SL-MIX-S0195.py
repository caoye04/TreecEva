def apply_filter(data, threshold=75):
    # Apply noise reduction filter
    filtered = []
    for value in data:
        if value > threshold:
            filtered.append(value - (value % 10))
        else:
            filtered.append(value)
    return filtered

def calculate_metrics(values):
    # Calculate various signal metrics
    if not values:
        return 0, 0, 0
    
    avg = sum(values) / len(values)
    peak = max(values) if values else 0
    low = min(values) if values else 0
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    
    return avg, peak, variance

def process_signal(signal_chunk):
    # Process the signal chunk and return final result
    if not signal_chunk:
        return 0
    
    # Filter out noise
    filtered_data = apply_filter(signal_chunk)
    
    # Calculate metrics for reporting purposes
    mean, peak, variance = calculate_metrics(filtered_data)
    
    # Apply bit manipulation to extract features
    features = []
    for value in filtered_data:
        # Extract binary features through bit operations
        feature = (value & 0x0F) | ((value >> 4) & 0x0F)
        features.append(feature)
    
    # Calculate primary and secondary indicators
    primary = sum(features) // len(features)
    secondary = peak - mean if peak > mean * 1.5 else mean - (mean % 10)
    
    # Apply final transformation
    result = (primary ^ 0x3A) + int(secondary / 10)
    
    return result

# Main signal processing pipeline
raw_data = [62, 97, 145, 86, 129, 42, 103, 114, 52, 74, 152, 139, 88, 104]

# Configuration parameters
filter_mode = "high_pass"
window_size = 4
start_offset = 2
quality_threshold = 65

# Processing variables
total_samples = len(raw_data)
processed_chunks = []
quality_scores = []

# Calculate optimal processing parameters
if filter_mode == "low_pass":
    start_idx = 1
    end_idx = 9
    chunk_size = 3
else:  # high_pass mode
    start_idx = 3
    end_idx = 10
    chunk_size = window_size - 1

# Calculate quality scores for monitoring
for i in range(0, total_samples - chunk_size + 1, 2):
    chunk = raw_data[i:i+chunk_size]
    avg_val = sum(chunk) / len(chunk)
    quality = (avg_val / 2) + (max(chunk) & 0x0F)
    quality_scores.append(quality)

# Simulate different filter configurations
test_filters = [(60, 0.8), (70, 0.9), (80, 1.0)]
filter_results = {}
for threshold, gain in test_filters:
    filtered = [v if v < threshold else v * gain for v in raw_data]
    filter_results[threshold] = filtered

# Process the target signal chunk
final_signal = process_signal(raw_data[start_idx:end_idx])

# Calculate alternative metrics for comparison
alt_signal = 0
for i, v in enumerate(raw_data[start_idx:end_idx]):
    if i % 2 == 0:
        alt_signal += (v & 0x3F) >> 2
    else:
        alt_signal += v % 15

print(f"Result: {final_signal}")