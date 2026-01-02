def analyze_trends(data, threshold):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1] * 1.1:
            trends.append('growth')
        elif data[i] < data[i-1] * 0.9:
            trends.append('decline')
        else:
            trends.append('stable')
    return trends

# Irrelevant helper function (decoy)
def calculate_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

# Unused transformation (dead code path)
def transform_signal(signal):
    return [x * 2 + 1 for x in signal if x % 2 == 0]

# Decoy metric with misleading name
phantom_metric = [3, 5, 7, 11, 13, 17, 19]
phantom_baseline = 8

# Real data inputs
metrics = [12, 15, 14, 18, 20, 22, 19, 21]
baseline = 16

# Distractor: complex slicing and filtering with no impact on result
shadow_slice = metrics[2:6][::-1]
filtered_noise = [x for x in shadow_slice if x > 15]

# Logical operation chain with red herring condition
is_optimal = len(filtered_noise) > 2 and all(x % 2 == 0 for x in filtered_noise)
override_flag = False

if is_optimal or sum(phantom_metric) < 100:
    override_flag = True  # Misleading branch never taken due to logic

# Real evaluation logic buried among distractions
def evaluate_performance(data, ref):
    above_count = sum(1 for x in data if x > ref)
    below_count = sum(1 for x in data if x < ref)
    equal_count = len(data) - above_count - below_count
    
    # Bit manipulation decoy
    magic_shift = (above_count << 2) ^ below_count
    
    # Actual score computation
    raw_score = (above_count * 10) - (below_count * 5) + (equal_count * 2)
    
    # Normalization via slicing-based window
    window = sorted(data)[-len(data)//2:]  # Top half
    bonus = sum(1 for w in window if w > ref + 2)
    
    # Final adjustment using logical operations
    multiplier = 1.5 if above_count >= 5 and bonus >= 2 else 1.0
    
    # Key distraction: unused intermediate
    phantom_result = (magic_shift + bonus * 3) % 100
    
    return int(raw_score * multiplier)

# Simulated trend analysis (irrelevant to final score)
trend_data = [10, 11, 13, 16, 17, 20, 24]
detected_trends = analyze_trends(trend_data, threshold=15)

count_stable = sum(1 for t in detected_trends if t == 'stable')

# Dead assignment with plausible name
effective_stability = count_stable >= 3

# Core execution point
final_score = evaluate_performance(metrics, baseline)

# Output requirement
print(f"Result: {final_score}")