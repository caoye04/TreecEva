def calculate_performance(base, data):
    adjustment_factor = 0.85
    filtered_data = [x for x in data if x > base * 0.7]
    
    # Irrelevant transformation (distractor)
    squared_offsets = [(x - base)**2 for x in data]
    mean_square_error = sum(squared_offsets) / len(squared_offsets) if squared_offsets else 0
    
    # Key computation path
    valid_count = len(filtered_data)
    if valid_count == 0:
        return 0
    
    avg_deviation = sum(abs(x - base) for x in filtered_data) / valid_count
    stability_index = (1 - (avg_deviation / (base * 0.5))) * 100
    
    # Secondary distractor: unused helper logic
    def analyze_trend(seq):
        return sum(seq[i] < seq[i+1] for i in range(len(seq)-1))
    trend_score = analyze_trend(data) * 0.1  # Computed but not used
    
    # Final score calculation
    reliability_bonus = 10 if valid_count >= 5 else 0
    raw_score = stability_index + reliability_bonus
    
    # Clamp result to realistic range
    final_score = max(0, min(raw_score, 100))
    
    # Dead code branch (misleading)
    if mean_square_error < 0:
        final_score += 5  # Never executed
    
    return final_score

# Simulated sensor readings relative to baseline
baseline = 74.0
readings = [76, 73, 78, 70, 75, 80, 68, 74, 77]

# Extraneous variable (distractor)
expected_variance = sum((x - baseline)**2 for x in readings) / len(readings)

# Key execution point
final_score = calculate_performance(baseline, readings)

print(f"Result: {final_score}")