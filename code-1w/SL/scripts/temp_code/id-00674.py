import itertools

# Simulated system performance metrics with noise
def generate_metrics():
    raw_data = [120, 150, 130, 160, 145, 135, 140]
    noise = [i % 3 for i in range(len(raw_data))]
    return [raw_data[i] + noise[i] for i in range(len(raw_data))]

# Irrelevant helper: computes variance but not used in final path
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Misleading function: looks important but never called
def legacy_normalization(vec):
    max_val = max(vec)
    return [v / max_val for v in vec]

# Decoy accumulator - used in dead branch
def accumulate_weights(values):
    weights = []
    for v in values:
        if v > 135:
            weights.append(v * 0.1)
        else:
            weights.append(v * 0.05)
    return sum(weights)

# Real processing begins here
def filter_outliers(data, threshold=125):
    return [x for x in data if x > threshold]

def calculate_moving_avg(seq, window=3):
    avgs = []
    for i in range(len(seq) - window + 1):
        avgs.append(sum(seq[i:i+window]) / window)
    return avgs

# Bit manipulation red herring
def encode_flags(value):
    flag_a = (value << 2) & 0xFF
    flag_b = (value >> 1) | 0x0A
    return flag_a ^ flag_b

# Unused complex structure
class PerformanceNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)

# Core logic buried among distractions
def evaluate_trend(moving_averages):
    increasing = 0
    for i in range(1, len(moving_averages)):
        if moving_averages[i] > moving_averages[i-1]:
            increasing += 1
    return increasing > (len(moving_averages) // 2)

# Heavily distractor-laden main evaluation
def evaluate_performance(metrics, baseline):
    # Step 1: Filter meaningful data
    filtered = filter_outliers(metrics)
    
    # Step 2: Compute moving averages
    mov_avgs = calculate_moving_avg(filtered)
    
    # Step 3: Assess trend direction
    has_upward_trend = evaluate_trend(mov_avgs)
    
    # Step 4: Baseline comparison with bit-noise distraction
    base_offset = 0
    for b in baseline:
        base_offset += (b ^ 0x5) & 0xF  # Irrelevant bit arithmetic
    
    # Step 5: Real scoring logic
    score = len(filtered) * 10
    if has_upward_trend:
        score += 25
    
    # Dead branch - looks active but condition never met
    temp_debug = [encode_flags(x) for x in filtered]
    if any(x < 0 for x in temp_debug):  # Impossible due to encoding
        score -= 10
    
    # Step 6: Apply multiplier based on length patterns
    pattern_match = any(len(list(group)) >= 3 for k, group in itertools.groupby(filtered) if k > 1)
    if pattern_match:
        score *= 2
    else:
        score += 5
    
    # Final adjustment using obscure but valid logic
    adjustment = sum(1 for a, b in zip(filtered, filtered[1:]) if b - a == 1)
    final_score = score + adjustment * 3
    
    # Critical execution point
    return final_score

# Global constants and decoy initializations
BASELINE_REF = [100, 105, 110]
data_cache = {"version": "deprecated", "values": []}
activation_key = sum(encode_flags(i) for i in range(10))  # Unused

# Main execution flow
if __name__ == "__main__":
    metrics = generate_metrics()
    final_score = evaluate_performance(metrics, BASELINE_REF)
    print(f"Target result: {final_score}")