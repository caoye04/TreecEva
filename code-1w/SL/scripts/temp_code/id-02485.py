def analyze_performance(temperatures):
    adjusted = [temp + 5 for temp in temperatures if temp > 0]
    unique_adjusted = list(set(adjusted))
    sorted_scores = sorted(unique_adjusted, reverse=True)
    filtered_scores = [score for score in sorted_scores if score % 2 == 0]
    temp_backup = [x * 0.1 for x in temperatures]  # irrelevant auxiliary calculation
    result = filtered_scores.pop() * 2
    return result

# Main execution
sensor_readings = [12, -5, 23, 8, 8, 15]
final_output = analyze_performance(sensor_readings)
print(f"Result: {final_output}")