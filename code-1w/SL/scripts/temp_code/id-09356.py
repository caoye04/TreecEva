import itertools

def analyze_sensor_data(data_stream):
    filtered = [x for x in data_stream if x > 25]
    return list(itertools.accumulate(filtered, lambda a, b: a + b * 0.9))

def calculate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val << 1) ^ i
    return checksum

def generate_efficiency_curve(base_value):
    curve = []
    temp = base_value
    for _ in range(7):
        temp = (temp * 1.05 + 2) % 100
        curve.append(temp)
    return [round(x, 3) for x in curve]

def validate_system_integrity(code_sequence):
    if len(code_sequence) < 5:
        return False
    even_sum = sum(code_sequence[::2])
    odd_product = 1
    for x in code_sequence[1::2]:
        odd_product *= (x + 1)
    return (even_sum % 7 == 0) and (odd_product % 3 != 0)

def calculate_thermal_rating(log_data):
    rating = 0
    for entry in log_data:
        if entry > 40:
            rating += entry * 1.3
        elif entry > 30:
            rating += entry * 0.8
        else:
            rating += entry * 0.4
    return int(rating)

# Simulated sensor input stream (irrelevant to final answer but looks important)
data_stream = [20, 32, 45, 28, 51, 33, 29, 44, 38, 53]

# Distractor: checksum calculation on transformed data (unused later)
processed_data = analyze_sensor_data(data_stream)
checksum = calculate_checksum(processed_data)

# Real computation path begins here
base_efficiency = 18

# Generate efficiency log - this is actually used
efficiency_log = generate_efficiency_curve(base_efficiency)

# Dead function call - appears relevant but isn't connected
dummy_validation = validate_system_integrity([1, 2, 3, 4, 5])

# Key transformation: filtering and scaling efficiency values (distractor)
scaled_log = [x * 1.1 for x in efficiency_log if x > 20]

# Another red herring: complex counting/grouping that leads nowhere
grouped = {k: len(list(g)) for k, g in itertools.groupby(sorted(scaled_log), key=lambda x: int(x))}
total_groups = sum(grouped.values())

# Critical statement: compute thermal capacity from original log (not scaled)
thermal_capacity = calculate_thermal_rating(efficiency_log)

# Additional distraction: conditional expression with unused result
status_flag = 'OK' if thermal_capacity > 300 else 'WARNING'

# Final irrelevant bit manipulation sequence
final_diagnostic = 0
for i in range(len(efficiency_log)):
    final_diagnostic |= (thermal_capacity >> i) & 0x0F

print(f"Result: {thermal_capacity}")