def calculate_performance(data):
    # Preprocessing: extract key metrics
    raw_values = [x['metric'] for x in data]
    
    # Irrelevant transformation (distractor)
    normalized = [round((v - min(raw_values)) / (max(raw_values) - min(raw_values)) * 100) for v in raw_values]
    adjusted = [n + 5 for n in normalized if n < 85]  # Partial adjustment, not used later
    
    # Core logic begins: analyze trends
    trend_changes = 0
    for i in range(1, len(raw_values)):
        if raw_values[i] > raw_values[i-1]:
            trend_changes += 1
        elif raw_values[i] < raw_values[i-1]:
            trend_changes -= 1

    # Secondary analysis: windowed averages (partially relevant)
    windows = [raw_values[i:i+3] for i in range(len(raw_values)-2)]
    stability_score = sum(len(w) for w in windows if max(w) - min(w) < 5)  # measure of flatness

    # Red herring: unused complex structure
    summary_stats = {
        'peak': max(raw_values),
        'volatility': sum(abs(raw_values[i] - raw_values[i-1]) for i in range(1, len(raw_values))),
        'outliers': [v for v in raw_values if v > 90 or v < 10],
        'phantom_metric': stability_score * 2 if len(adjusted) > 10 else 0
    }

    # Conditional expression with slicing: critical step
    base_score = trend_changes * 10 if len(data) > 5 else sum(raw_values[:len(data)//2])
    
    # Final computation using slicing and conditional state
    bonus = sum(raw_values[-3:]) // 3 if raw_values[-1] > raw_values[0] else 0
    final_score = base_score + bonus
    
    # Dead code path (never reached in current control flow)
    if False:
        final_score = max(normalized) * 2
    
    return final_score

# Input data
benchmark_data = [
    {'id': 'A', 'metric': 12},
    {'id': 'B', 'metric': 15},
    {'id': 'C', 'metric': 14},
    {'id': 'D', 'metric': 18},
    {'id': 'E', 'metric': 22},
    {'id': 'F', 'metric': 25},
    {'id': 'G', 'metric': 24}
]

result = calculate_performance(benchmark_data)
print(f"Result: {result}")