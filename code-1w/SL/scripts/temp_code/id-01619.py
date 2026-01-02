def analyze_temperatures(temps):
    threshold = 20
    high_temps = [t for t in temps if t > threshold]
    low_temps = [t for t in temps if t <= threshold]
    
    # Irrelevant distraction: count how many times temperature fluctuates
    fluctuations = 0
    for i in range(1, len(temps)):
        if (temps[i] > threshold) != (temps[i-1] > threshold):
            fluctuations += 1
    
    # Core computation path
    scaled_values = [t * 1.5 for t in high_temps]
    processed = [round(t) for t in scaled_values]
    filtered_values = [t for t in processed if t % 2 == 0]
    filtered_sum = sum(filtered_values)
    return filtered_sum

# Main execution
recorded_temps = [18, 25, 30, 15, 22, 35]
result = analyze_temperatures(recorded_temps)
print(f"Result: {result}")