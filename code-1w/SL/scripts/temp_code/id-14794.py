def analyze_trends(values):
    trends = []
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trends.append(1)
        elif values[i] < values[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

# Irrelevant helper function (decoy)
def compute_entropy(seq):
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p) if p > 0 else 0
    return round(entropy, 6)

# Unused transformation path
def transform_data(arr, mode='linear'):
    if mode == 'square':
        return [x**2 for x in arr]
    elif mode == 'log':
        return [__import__('math').log(x) if x > 0 else 0 for x in arr]
    else:
        return [x * 2 for x in arr]  # never used

# Core logic with distractors
def filter_outliers(series, threshold=2):
    mean_val = sum(series) / len(series)
    std_dev = (sum((x - mean_val) ** 2 for x in series) / len(series)) ** 0.5
    filtered = [x for x in series if abs(x - mean_val) <= threshold * std_dev]
    outlier_count = len(series) - len(filtered)  # distraction
    scaling_factor = 1.0 if outlier_count < 3 else 0.9  # unused
    return filtered

# Critical processing function
def process_metrics(data, weights):
    normalized = []
    for col in zip(*data):  # using zip
        min_val, max_val = min(col), max(col)
        if max_val - min_val == 0:
            norm_col = [0.0 for _ in col]
        else:
            norm_col = [(x - min_val) / (max_val - min_val) for x in col]
        normalized.append(norm_col)
    
    # Apply weights using enumerate
    weighted_sum = [0] * len(data)
    for i, weight in enumerate(weights):
        for j, row in enumerate(normalized):
            weighted_sum[j] += row[j] * weight  # careful indexing
    
    # Secondary adjustment based on trend consistency
    trends = analyze_trends(weighted_sum)
    adjustment = 0.0
    for idx, (val, trend) in enumerate(zip(weighted_sum, trends)):
        if idx > 0 and trends[idx-1] == trend:
            adjustment += 0.05 * val
    
    # Final aggregation
    base_result = sum(weighted_sum) * 1.1
    final_score = int(round(base_result + adjustment))  # key assignment
    
    # Dead code branch (never reached due to structure)
    if False:
        backup = compute_entropy(trends)
        final_score = int(round(base_result * (1 + backup / 10)))
    
    return final_score

# Irrelevant global variables
current_mode = 'diagnostic'
buffer_cache = [0] * 100
last_updated = '2023-09-15'

# Input data
raw_input = [120, 150, 130, 170, 200]
data_matrix = [
    [85, 90, 78, 92],
    [76, 88, 82, 85],
    [90, 94, 85, 88],
    [70, 75, 80, 73],
    [95, 99, 92, 96]
]

weights_list = [0.2, 0.3, 0.25, 0.25]

# Filtering irrelevant data
cleaned_input = filter_outliers(raw_input, threshold=1.8)

# Unused list comprehension variant
doubled = [x * 2 for x in raw_input if x > 80]

# Main execution
trend_analysis = analyze_trends(cleaned_input)
entropy_value = compute_entropy(trend_analysis)  # computed but not used

final_score = process_metrics(data_matrix, weights_list)
print(f"Result: {final_score}")