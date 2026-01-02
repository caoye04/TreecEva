def analyze_trend(values):
    if len(values) < 2:
        return 0
    trend = sum(1 for i in range(1, len(values)) if values[i] > values[i-1])
    volatility = sum(abs(values[i] - values[i-1]) for i in range(1, len(values)))
    adjustment_factor = 0.9 if volatility > 50 else 1.1
    return trend * adjustment_factor


def filter_outliers(nums, limit=25):
    # Irrelevant filtering function (not used in final path)
    return [n for n in nums if abs(n - sum(nums)/len(nums)) < limit]

def compute_baseline(items):
    baseline = 0
    for item in items:
        if item % 4 == 0:
            baseline += item // 4
        elif item % 3 == 0:
            baseline -= item // 5
    return baseline + 10  # Distractor computation

def process_metrics(dataset, config):
    size = len(dataset)
    midpoint = size // 2
    first_half = dataset[:midpoint]
    second_half = dataset[midpoint:]
    
    # Conditional expression and slicing
    primary_segment = second_half if sum(second_half) > sum(first_half) else first_half
    
    growth = analyze_trend(primary_segment)
    
    # Misleading intermediate calculations
    temp_offset = (max(primary_segment) - min(primary_segment)) // 3
    noise_level = sum(1 for x in primary_segment if x % 2 == 1)
    score_modifier = 1.2 if noise_level < 6 else 0.85
    
    # Key logic step: counting even numbers above threshold
    threshold_ref = config['base']
    valid_entries = [x for x in primary_segment if x > threshold_ref]
    count_valid = len(valid_entries)
    even_count = sum(1 for x in valid_entries if x % 2 == 0)
    
    # Semi-relevant grouping operation
    grouped = {}
    for v in valid_entries:
        key = v // 10
        grouped[key] = grouped.get(key, 0) + 1
    
    peak_group = max(grouped.keys()) if grouped else 0
    
    # Final composite calculation
    raw_score = (even_count * 7) + (count_valid * 2) + (int(growth))
    final_score = int(raw_score * score_modifier + peak_group - temp_offset)
    
    return final_score

# Main execution
raw_data = [12, 15, 18, 14, 26, 31, 22, 25, 28, 34, 30, 36]
thresholds = {'base': 20}

# Dead code path - irrelevant preprocessing
filtered_data = filter_outliers(raw_data)
baseline_correction = compute_baseline(raw_data)

# Critical execution point
final_score = process_metrics(raw_data, thresholds)

print(f"Result: {final_score}")