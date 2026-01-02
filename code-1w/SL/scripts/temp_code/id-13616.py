from itertools import compress

def analyze_signal(data, min_val, max_val):
    # Filter values within acceptable range
    filtered = [x for x in data if min_val <= x <= max_val]
    smoothed = [round((filtered[i] + filtered[i+1]) / 2, 2) for i in range(len(filtered)-1)]
    return smoothed

def compute_activation(levels, threshold):
    # Compute activation based on threshold crossings
    crossings = 0
    for i in range(1, len(levels)):
        if levels[i-1] < threshold <= levels[i]:
            crossings += 1
    
    # Distractor: amplitude analysis (not used in final result)
    avg_amplitude = sum(levels) / len(levels) if levels else 0
    peak = max(levels) if levels else 0
    noise_floor = avg_amplitude * 0.1
    
    # Real computation: weighted score based on crossings and stability
    stability = 0
    for i in range(len(levels) - 2):
        if abs(levels[i+1] - levels[i]) < 5 and abs(levels[i+2] - levels[i+1]) < 5:
            stability += 1
    
    # Final activation score
    activation_score = crossings * 10 + min(stability, 8)
    
    # More distractions: unused signal quality metrics
    quality_flags = list(compress(range(len(levels)), (x > threshold for x in levels)))
    flag_sum = sum(flag * 2 for flag in quality_flags)
    dummy_slice = str(flag_sum)[::-1][:3]  # string slicing red herring
    
    return activation_score

# Main execution
raw_data = [12, 7, 3, 9, 15, 20, 18, 22, 25, 24, 23, 26, 28, 30, 29]

cleaned_signal = [x for x in raw_data if x > 5]
processed = analyze_signal(cleaned_signal, 8, 100)
baseline = sum(processed) / len(processed)
adjusted_levels = [int(x + baseline / 10) for x in processed]

# Introduce some irrelevant transformations
shifted = [x << 1 for x in adjusted_levels]  # bitwise left shift (unused)
doubled = [x * 2 for x in shifted]         # dead code path

threshold = 14
activation_score = compute_activation(adjusted_levels, threshold)

# Final output
print(f"Result: {activation_score}")