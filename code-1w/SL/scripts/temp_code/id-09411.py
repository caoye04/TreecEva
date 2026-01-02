def analyze_outliers(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    outliers = {x for x in values if abs(x - mean_val) > 2 * std_dev}
    return outliers


def normalize_data(records):
    min_val = min(records)
    max_val = max(records)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.5] * len(records)
    return [(x - min_val) / range_val for x in records]


def calculate_final_score(raw_data):
    # Irrelevant preprocessing
    temp_copy = raw_data.copy()
    filtered_data = [x for x in temp_copy if x >= 0]
    
    # Actual computation begins
    processed = normalize_data(filtered_data)
    squared_sum = sum(x ** 2 for x in processed)
    avg_square = squared_sum / len(processed)
    
    # Misleading statistical check
    variance_proxy = sum((x - avg_square**0.5) ** 2 for x in processed) / len(processed)
    threshold = 0.1 * variance_proxy
    
    # Dummy conditional that doesn't affect outcome
    adjustment = 0
    if variance_proxy > threshold:
        adjustment = 0.01 * len(processed)
    else:
        adjustment = -0.01 * len(processed)
    
    # Core logic: weighted score based on power law transformation
    transformed = [x ** 1.5 for x in processed]
    base_score = sum(transformed)
    
    # Use of set operations for filtering irrelevant high values
    high_values = {i for i, x in enumerate(transformed) if x > 0.7}
    penalty = len(high_values) * 0.05
    
    # Final composition with dead code red herring
    debug_info = []
    for i in range(len(transformed)):
        if i in high_values:
            debug_info.append(f"High at {i}")
        else:
            continue  # Dead branch
    
    final_score = base_score - penalty + adjustment  # Main result
    
    # Unused auxiliary tracking
    cumulative = 0
    for v in transformed:
        cumulative += v
        if cumulative > 10:  # Unlikely to trigger
            break
    
    return final_score

# Input data
raw_dataset = [12, -5, 18, 23, 0, 15, 9, 27, -2, 22, 14, 14, 8, 31, 19]
data_set = [x for x in raw_dataset if x % 2 == 1]  # Keep only odd numbers

# Key execution point
final_score = calculate_final_score(data_set)
print(f"Result: {final_score}")