import math

def analyze_efficiency(data, threshold):
    """Irrelevant function analyzing efficiency – distractor."""
    if not data:
        return 0
    avg = sum(data) / len(data)
    filtered = [x for x in data if x > threshold]
    return len(filtered) / len(data) if data else 0

def transform_sequence(seq):
    """Misleading transformation with no impact on final result – red herring."""
    shifted = [(x << 2) ^ 3 for x in seq]
    return [math.sin(x) for x in shifted if x % 2 == 0]

def compute_stability_index(values):
    """Decoy function that calculates variance-like metric – dead code path."""
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return round(variance, 3)

def evaluate_performance(metrics, base):
    """Core function that computes the actual answer."""
    # Initialize various variables (some are distractions)
    temp_offset = 0
    adjustment_factor = 1.75
    debug_trace = []
    cumulative_weight = 0
    
    # Irrelevant pre-processing block (distractor logic)
    if len(metrics) > 5:
        temp_offset += 2
        debug_trace.append('triggered')
    else:
        temp_offset -= 1
    
    # Real computation begins here
    weighted_sum = 0
    weights = [0.1, 0.2, 0.3, 0.25, 0.15]  # Must match metrics length
    
    for i in range(len(metrics)):
        weighted_sum += metrics[i] * weights[i]
    
    # Additional relevant adjustment based on baseline
    base_modifier = 1.0
    if base < 75:
        base_modifier = 1.1
    elif base > 90:
        base_modifier = 0.9
    
    intermediate = weighted_sum * base_modifier
    
    # Spurious nested condition (looks important but doesn't alter outcome)
    if intermediate > 80:
        for _ in range(2):
            adjustment_factor *= 0.95  # This value is never used later
    elif intermediate < 60:
        adjustment_factor = 2.0  # Also unused
    
    # Actual final calculation
    raw_score = intermediate + 5  # Key fixed adjustment
    
    # Dead branch – looks like it affects result but doesn't
    if raw_score % 1 == 0:
        noise = sum([i * 0.01 for i in range(len(debug_trace))])
        raw_score += noise  # Negligible effect, debug_trace is empty
    
    # Final scaling
    final_score = int(round(raw_score * 2))
    
    # Unused complex expression (bit manipulation decoy)
    security_checksum = (final_score ^ 0xABCDEF) >> 4
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Input data – realistic domain: system performance metrics (CPU, memory, latency, etc.)
    performance_metrics = [88, 76, 92, 81, 73]  # Out of 100
    baseline_average = 82
    
    # Distractor variables and computations
    historical_data = [78, 85, 80, 90, 77]
    current_cycle = 4
    max_threshold = max(performance_metrics) * 0.95
    
    # Call irrelevant functions to create confusion
    efficiency_ratio = analyze_efficiency(historical_data, 80)
    transformed = transform_sequence([1, 2, 3, 4])
    stability = compute_stability_index([5, 10, 15])
    
    # Core statement that produces the answer
    final_score = evaluate_performance(performance_metrics, baseline_average)
    
    # Print result as required
    print(f"Result: {final_score}")