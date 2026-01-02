def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] % 3 == 0 and i % 2 == 1:
            count += sequence[i]
    return count

# Simulate sensor readings
temperature_readings = [23, 36, 45, 60, 72, 81, 90, 105]

# Misleading computation - not directly used
dummy_sum = sum(x for x in temperature_readings if x > 50)
avg_temp = sum(temperature_readings) / len(temperature_readings)
adjusted_values = [x - avg_temp for x in temperature_readings]

# Core logic begins
baseline = analyze_pattern(temperature_readings)

# Weighting function using lambda
weight_func = lambda x: 0.1 if x < 30 else (0.25 if x < 70 else 0.4)
weights = list(map(weight_func, temperature_readings))
data = [x * 0.1 for x in temperature_readings]

# String-based flag check (using string method)
status_flag = 'critical_high_warning'
flag_active = status_flag.upper().startswith('CRITICAL')

# Secondary distraction: modular arithmetic with no impact
cyclic_index = 0
for _ in range(100):
    cyclic_index = (cyclic_index + 7) % 13

# Main processing function
def process_metrics(values, scaling_factors):
    result = 0.0
    temp_offset = 0
    
    # Nested condition and loop
    for i in range(len(values)):
        if i % 2 == 0:
            contribution = values[i] * scaling_factors[i]
            if contribution > 3.0:
                temp_offset += 1
            result += contribution
        else:
            # Apply correction based on baseline
            corrected = values[i] * (scaling_factors[i] + (baseline % 5) * 0.01)
            result += corrected
    
    # Red herring: unused tracking variable
    final_adjustment_magnitude = abs(result - baseline)
    
    # Final adjustment
    if flag_active:
        result *= 1.1
    
    return int(result * 100) / 100  # Round to two decimal places

# Execute main logic
interim_total = baseline * 1.5
final_score = process_metrics(data, weights)
print(f"Result: {final_score}")