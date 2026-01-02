def analyze_trends(data, threshold):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append(1)
        elif data[i] < data[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return [x for x in trends if abs(x) == 1]


def compute_volatility(seq):
    if len(seq) < 2:
        return 0.0
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs)


def filter_outliers(values, factor=1.5):
    if len(values) == 0:
        return []
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    low = q1 - factor * iqr
    high = q3 + factor * iqr
    return [v for v in values if low <= v <= high]


def generate_checksum(sequence):
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum ^= (val + idx) % 256
    return checksum


def evaluate_performance(metrics, base):
    adjusted = [m - base for m in metrics]
    squared_errors = [(m - base) ** 2 for m in metrics]
    mse = sum(squared_errors) / len(squared_errors) if squared_errors else 0
    rmse = mse ** 0.5
    direction_bias = sum(1 for m in adjusted if m > 0) - sum(1 for m in adjusted if m < 0)
    normalized_bias = direction_bias / len(adjusted) if adjusted else 0
    
    # Irrelevant intermediate computations (red herrings)
    temp_analysis = []
    for x in adjusted:
        if x > 0.5:
            temp_analysis.append(x * 2)
        elif x < -0.5:
            temp_analysis.append(x / 2)
    temp_stats = {
        'max_temp': max(temp_analysis) if temp_analysis else 0,
        'min_temp': min(temp_analysis) if temp_analysis else 0
    }
    
    # Decoy function call with no side effects
    _ = compute_volatility([10, 20, 15, 25, 30])
    
    # Dead code path (never executed due to logic)
    debug_mode = False
    if debug_mode and len(metrics) > 100:
        print("Debug: Deep analysis initiated")
        for i in range(999):
            pass

    # Core logic buried among distractions
    weight_rmse = 0.7
    weight_bias = 0.3
    performance_index = (rmse * weight_rmse) + (abs(normalized_bias) * weight_bias)
    
    # More irrelevant variables
    dummy_list = [i**2 for i in range(10) if i % 3 == 0]
    shadow_value = sum(dummy_list) // 2 if dummy_list else 0
    
    # Actual answer computation
    final_score = int(100 - (performance_index * 10))
    
    # Unused transformation
    inverted_metrics = [base / m if m != 0 else 0 for m in metrics]
    
    return final_score

# Main execution block
raw_data = [85, 90, 87, 92, 88, 95, 89, 91, 86, 93]
baseline = 88

# Irrelevant preprocessing
filtered_data = filter_outliers(raw_data, factor=2.0)
trend_sequence = analyze_trends(raw_data, threshold=1)
checksum = generate_checksum(raw_data)

# Key statement
final_score = evaluate_performance(raw_data, baseline)

print(f"Result: {final_score}")