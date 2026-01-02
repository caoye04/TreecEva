def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x for x in data if x > threshold]


def preprocess_signals(signals):
    """Another decoy function that is never called."""
    processed = {}
    for idx, val in enumerate(signals):
        processed[idx] = val ** 2 + 1j * val
    return processed

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
DEBUG_MODE = True

# Real input data (but mixed with noise)
raw_metrics = [0.82, 0.74, 0.91, 0.67, 0.88]
weights = [3, 2, 4, 1, 3]

# Decoy data structures
auxiliary_cache = {
    'temp_data': [1, 1, 2, 3, 5, 8],
    'checksum': 0xDEADBEEF,
    'history': []
}

# Simulated system status (red herring)
current_state = {
    'active': True,
    'mode': 'production',
    'version': '2.1.0'
}

# Misleading intermediate calculation
aggregate = sum([x * 100 for x in raw_metrics]) // len(raw_metrics)
dropout_count = len([x for x in raw_metrics if x < 0.7])
penalty_factor = dropout_count * 0.05

# Core logic hidden among distractions
def compute_weighted_sum(values, multipliers):
    if len(values) != len(multipliers):
        return -1
    total = 0
    for i, (v, w) in enumerate(zip(values, multipliers)):
        if v >= 0.7:  # Only consider acceptable metrics
            total += v * w * 10
    return int(total)

# Another irrelevant utility
def generate_report(config):
    return f"Report: {config.get('mode', 'N/A')}"

# Key function that actually produces the answer
def evaluate_performance(metrics, weights):
    base = compute_weighted_sum(metrics, weights)
    
    # Additional adjustment based on distribution
    sorted_vals = sorted(metrics)
    median_offset = sorted_vals[len(sorted_vals)//2] * 10
    
    # Apply artificial inflation (part of logic)
    inflated = base * 1.05
    
    # Dummy branch (never taken, but looks important)
    if DEBUG_MODE and False:
        print("Debugging performance...")
        inflated -= 100  # Dead code path
    
    # Final transformation
    final_raw = int(inflated + median_offset)
    
    # Normalize against max possible (3*10 + 2*10 + 4*10 + 1*10 + 3*10) = 130 -> scaled by 10
    max_possible = 1300
    if final_raw > max_possible:
        final_raw = max_possible  # Clipping (not triggered)
    
    # Hidden modulo adjustment based on bitwise pattern
    flag_value = 0
    for w in weights:
        flag_value ^= w  # XOR all weights: 3 ^ 2 ^ 4 ^ 1 ^ 3 = 7
    
    final_adjusted = final_raw - (flag_value * 2)  # Subtract 14
    
    return final_adjusted

# Unused recursive red herring
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Critical execution point
final_score = evaluate_performance(raw_metrics, weights)

# Output result as required
print(f"Result: {final_score}")