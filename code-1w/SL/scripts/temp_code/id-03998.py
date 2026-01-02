def calculate_adjusted_peak():
    temperatures = [23.5, 19.8, 27.3, 30.1, 22.0]
    scaling_factor = 2
    offset = 5
    min_threshold = 15.0  # Irrelevant threshold for filtering (not used)
    valid_temps = [t for t in temperatures if t > min_threshold]
    
    if len(valid_temps) > 3:
        result = temperatures[1:4][::-1][0] * scaling_factor - offset
        return result

result = calculate_adjusted_peak()
print(f"Result: {result}")