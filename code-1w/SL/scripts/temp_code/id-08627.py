def calculate_threshold(data, settings):
    baseline = sum(data) / len(data)
    deviation = sum((x - baseline) ** 2 for x in data) / len(data)
    variance = deviation ** 0.5
    
    # Irrelevant auxiliary calculation (minor distractor)
    peak = max(data)
    normalized_peak = peak / (variance + 1)
    
    adjustment = settings['sensitivity'] if variance > settings['noise_floor'] else 0.5
    filtered_baseline = baseline * (1 + adjustment * 0.1)
    
    return int(filtered_baseline) if settings['round_output'] else filtered_baseline

# Main execution
readings = [45, 67, 52, 89, 71, 58, 64]
config = {
    'sensitivity': 1.2,
    'noise_floor': 12.0,
    'round_output': True
}

# Key statement
threshold_score = calculate_threshold(readings, config)

# Output result
print(f"Result: {threshold_score}")