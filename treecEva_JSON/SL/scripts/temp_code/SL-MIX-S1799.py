from collections import defaultdict
import math

def compute_spectral_energy(freq_data, depth=0):
    if len(freq_data) <= 1:
        return freq_data[0] if freq_data else 0
    
    mid = len(freq_data) // 2
    left_part = freq_data[:mid]
    right_part = freq_data[mid:]
    
    left_energy = compute_spectral_energy(left_part, depth + 1)
    right_energy = compute_spectral_energy(right_part, depth + 1)
    
    # Calculate local statistics for current segment
    segment_sum = sum(freq_data)
    segment_len = len(freq_data)
    mean_val = segment_sum / segment_len if segment_len else 0
    variance = sum((x - mean_val) ** 2 for x in freq_data) / segment_len if segment_len else 0
    
    # Weighted combination of recursive results and local metrics
    weight_factor = 1.0 / (1 << depth)  # 1/(2^depth)
    local_contribution = math.sqrt(variance) * weight_factor if variance >= 0 else 0
    
    combined = (left_energy + right_energy) * (1 - weight_factor) + local_contribution
    
    return combined

# Frequency domain data representing power spectrum values
spectrum_values = [16, 9, 4, 25, 36, 49, 64, 81]

# Compute the modified spectral energy using divide and conquer
processed_metric = compute_spectral_energy(spectrum_values)

# Apply final transformation with ternary operator for thresholding
final_metric = processed_metric if processed_metric > 50 else processed_metric * 2

print(f"Result: {final_metric}")