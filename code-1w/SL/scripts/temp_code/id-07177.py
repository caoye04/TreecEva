def analyze_trends(data, threshold=0.5):
    """Irrelevant helper function for trend detection."""
    trends = []
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            trends.append('up')
        elif data[i-1] - data[i] > threshold:
            trends.append('down')
        else:
            trends.append('stable')
    return trends

# Decoy data structures with misleading names
trend_data = [0.1, 0.8, 0.3, 1.2, 0.9]
decoy_weights = [0.2, 0.4, 0.6, 0.8, 1.0]
scaling_factor = 3.7
offset_correction = -1.2

# Real operational data
metrics = [0.85, 0.92, 0.78, 0.96, 0.88]
baseline = 0.85

# Distractor: unused complex transformation
weighted_avg = sum(w * x for w, x in zip(decoy_weights, trend_data)) / sum(decoy_weights)

# Irrelevant sorting of unrelated tuples
event_log = [('login', 'user1'), ('action', 'user2'), ('login', 'user3')]
sorted_events = sorted(event_log, key=lambda x: x[0].lower())

# Bit manipulation red herring
device_flags = 0b10101010
masked_flags = device_flags & 0b11110000
shifted_flags = masked_flags >> 4

# Unused recursive function to increase nesting and distraction
def compute_depth(n):
    if n <= 1:
        return 1
    return compute_depth(n-1) + compute_depth(n-2)

# Real logic begins here — deeply nested within distractions
def normalize(value, low, high):
    return (value - low) / (high - low) if high != low else 0.0

def calculate_deviation(x, y):
    return abs(x - y)

# Core evaluation function buried among noise
def evaluate_performance(scores, reference):
    # Step 1: Calculate deviations
    deviations = [calculate_deviation(s, reference) for s in scores]
    
    # Step 2: Normalize deviations to 0-1 scale
    max_dev = max(deviations) if deviations else 1
    norm_deviations = [normalize(d, 0, max_dev) for d in deviations]
    
    # Step 3: Apply non-linear penalty using exponentiation
    penalties = [pow(p, 2.5) for p in norm_deviations]
    
    # Step 4: Compute base accuracy score
    accuracy_score = sum(scores) / len(scores)
    
    # Step 5: Aggregate penalty
    total_penalty = sum(penalties)
    
    # Step 6: Apply case-based adjustment (simulates policy rule)
    adjustment = 0.0
    if accuracy_score >= 0.9:
        adjustment = 0.05
    elif accuracy_score < 0.8:
        adjustment = -0.1
    else:
        adjustment = -0.05
    
    # Step 7: Combine components into final score
    raw_final = accuracy_score - total_penalty + adjustment
    
    # Step 8: Clamp to valid range
    clamped_final = max(0.0, min(raw_final, 1.0))
    
    # Step 9: Scale to integer-like precision (simulate scoring system)
    scaled_final = int(clamped_final * 10000) / 10000.0
    
    return scaled_final

# Misleading intermediate call with decoy data
dummy_result = analyze_trends(trend_data, threshold=0.25)

# Key statement: this is where the real answer is computed
final_score = evaluate_performance(metrics, baseline)

# Distraction: convert case of strings for no reason
dummy_strings = ['Hello', 'WORLD', 'PyThOn']
converted = [s.upper() if 'a' in s.lower() else s.lower() for s in dummy_strings]

# Output the target result
print(f"Target result: {final_score}")