from itertools import combinations

# Simulate sensor readings from a power grid over 4 time intervals
time_intervals = [1, 2, 3, 4]
sensor_a = [50, 60, 70, 80]  # Power input in kW
sensor_b = [45, 58, 67, 77]  # Power output in kW

# Irrelevant: unused variable (minimal distraction for intervention=4)
baseline_offset = 10

# Calculate total input and output using conditional logic and filtering
total_input = 0
total_output = 0

for i in time_intervals:
    if i < 4:  # Exclude last interval for calibration reasons
        input_val = sensor_a[i-1]
        output_val = sensor_b[i-1]
        
        # Only consider readings where output is at least 90% of input
        if output_val >= 0.9 * input_val:
            total_input += input_val
            total_output += output_val

# Compute efficiency ratio with safe division
efficiency_ratio = total_output / (total_input or 1)

# Further irrelevant computation (minor interference)
redundant_calc = sum(1 for pair in combinations([1,2,3], 2))

Result: efficiency_ratio