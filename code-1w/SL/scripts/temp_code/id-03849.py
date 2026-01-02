import itertools

def preprocess_readings(readings):
    filtered = [r for r in readings if r > -50 and r < 100]
    smoothed = list(map(lambda x: (x + readings[readings.index(x)-1]) / 2 if readings.index(x) > 0 else x, filtered))
    return smoothed

def calculate_efficiency(data, limit):
    count = 0
    total = 0.0
    temp_log = []
    
    for i, val in enumerate(data):
        if i % 2 == 0:
            for j in range(1, min(i+2, 4)):
                if j < len(data) and data[j] > limit:
                    count += 1
                    total += data[j] * 0.9
        temp_log.append(val * 1.1)  # logged but unused later
    
    avg_effect = total / (count or 1)
    extra_shift = sum(itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6]))  # red herring
    return avg_effect + 2.5

# Sensor simulation (fixed input)
sensor_offsets = [3, -1, 4, 0, 2]
base_readings = [23.5, 18.0, 35.2, 15.8, 22.1]
adjusted_readings = [base_readings[i] + sensor_offsets[i] for i in range(len(base_readings))]

# Irrelevant transformation chain
transformed = [x ** 0.5 for x in adjusted_readings if x > 20]
duplicate_check = list(set([int(x) for x in transformed]))
shadow_copy = transformed.copy()
shadow_copy.append(999)  # dead code

# Main processing pipeline
logged_data = preprocess_readings(adjusted_readings)
threshold = 20.0
scaling_factor = 1.75

# Dummy recursive helper (unused)
def recursive_sum(n):
    return n + recursive_sum(n-1) if n > 1 else 1

# Key computational branch
aggregate = 0
for x in logged_data:
    if x > 19:
        aggregate += x * 0.1

# Critical assignment point
target_buffer = [x for x in logged_data if x > threshold]
size_penalty = len(shadow_copy) - len(logged_data)  # distraction
thermal_capacity = calculate_efficiency(logged_data, threshold) * scaling_factor

# Print final result
print(f"Result: {thermal_capacity}")