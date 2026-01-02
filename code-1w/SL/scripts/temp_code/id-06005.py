def analyze_metrics(data):
    total = sum(data)
    average = total / len(data) if data else 0
    variance = sum((x - average) ** 2 for x in data) / len(data) if data else 0
    return average, variance

# Simulate system performance metrics
data_stream = [85, 90, 78, 92, 88]
avg, var = analyze_metrics(data_stream)

# Extraneous calculation - distractor
fluctuation_index = var / (avg + 1e-5)
stability_ratio = (100 - var) / 100 if var < 100 else 0

# Core logic inputs
efficiency = int(avg // 10) * 10  # Rounded down to nearest 10
errors = len([x for x in data_stream if x < 80])

# Secondary derived values - some irrelevant
peak_performance = max(data_stream)
consistency_bonus = 5 if stability_ratio > 0.8 else 0
overhead_cost = fluctuation_index * 2  # Not used in final result

# Conditional expression used as required
penalty = 10 if errors > 0 else 0
adjustment_factor = 1.05 if efficiency >= 80 and errors == 0 else 0.95

# Key function with mixed logic
def assess_performance(eff, errs):
    base = eff * 1.2
    if errs == 0:
        if efficiency >= 80:
            base += 15
        elif efficiency >= 70:
            base += 5
    else:
        base -= errs * 4
    # Apply adjustment factor via conditional expression
    base = base * adjustment_factor if efficiency >= 80 else base
    return int(base)

# Misleading intermediate computation - dead-end path
temporary_result = peak_performance * consistency_bonus / (overhead_cost + 1)
scaling_factor = temporary_result % 7 if temporary_result > 0 else 1  # Unused

# Critical execution point
final_score = assess_performance(efficiency, errors)

# Print result as required
print(f"Result: {final_score}")