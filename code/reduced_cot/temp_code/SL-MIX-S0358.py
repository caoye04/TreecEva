import itertools

def process_neuronal_signals(signals):
    # Apply combinatorial pairing and calculate XOR metrics
    paired_metrics = [
        a ^ b for a, b in itertools.combinations(signals, 2)
        if (a + b) % 3 == 0
    ]
    
    # Sort metrics in descending order
    sorted_metrics = sorted(paired_metrics, reverse=True)
    
    # Compute adaptive threshold using ternary logic
    threshold = sum(sorted_metrics[:3]) // len(sorted_metrics[:3]) if sorted_metrics else 0
    
    # Filter metrics above threshold
    filtered_metrics = [m for m in sorted_metrics if m > threshold]
    
    # Calculate final metric as alternating sum of top 4 values
    sign = 1
    aggregate = 0
    for i, val in enumerate(filtered_metrics[:4]):
        aggregate += sign * val
        sign *= -1
    
    # Normalize using ternary operator based on list length
    final_metric = aggregate // 2 if len(filtered_metrics) >= 4 else aggregate * 2
    return final_metric

# Neuronal signal dataset
signals_data = [13, 22, 35, 46, 57, 68, 79, 81, 92, 103]

# Process the signals
final_metric = process_neuronal_signals(signals_data)
print(f"Result: {final_metric}")