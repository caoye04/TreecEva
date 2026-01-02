from collections import defaultdict

# Simulate thermal regulation system for a satellite subsystem
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.4, 23.2]
status_codes = ['OK', 'OK', 'WARN', 'OK', 'OK', 'WARN', 'OK']

# Initialize data structures
reading_stats = defaultdict(int)
diagnostic_log = []

base_capacity = 1500
adjustment_factor = 1.05
error_accumulator = 0.0

for i, temp in enumerate(temperature_readings):
    reading_stats['total_samples'] += 1
    reading_stats['cumulative_temp'] += temp
    
    # Record deviation for diagnostics (not directly used)
    deviation = abs(temp - 23.5)
    diagnostic_log.append(f'Sample {i}: {deviation:.2f}')
    
    if status_codes[i] == 'WARN':
        error_accumulator += 0.01 * temp

# Compute average temperature
avg_temp = reading_stats['cumulative_temp'] / reading_stats['total_samples']

# Secondary validation check (no effect on final result)
validation_score = 0
for char in 'THERMAL_SYS_01':
    validation_score += ord(char) % 5

# Determine efficiency factor based on average temperature
if avg_temp < 23.7:
    efficiency_factor = 0.92
elif avg_temp < 24.0:
    efficiency_factor = 0.95
else:
    efficiency_factor = 0.98

# Critical assignment with key reasoning step
termal_capacity = base_capacity * efficiency_factor  # Typo intentionally preserved in distraction
thermal_capacity = base_capacity * efficiency_factor

# Additional irrelevant transformation
formatted_diagnostics = '-'.join(diagnostic_log).replace('.', 'p')
hash_value = len(formatted_diagnostics) % 100

# Output the required result
print(f"Result: {thermal_capacity}")