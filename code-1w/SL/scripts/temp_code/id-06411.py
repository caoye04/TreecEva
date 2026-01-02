import math

# Irrelevant helper function (decoy)
def useless_transform(data):
    return [x ** 0.5 for x in data if x % 3 == 0]

# Another decoy function with dead logic
def validate_checksum(arr):
    checksum = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            checksum += arr[i] * 1.1
        else:
            checksum -= arr[i] * 0.9
    return checksum > 100

# Misleading intermediate computation
turbine_efficiency = [0.78, 0.82, 0.85, 0.77, 0.91, 0.88, 0.83, 0.79]
adjusted_efficiency = [e * (1 + 0.02) for e in turbine_efficiency]

# Real input data disguised among noise
raw_signal_data = [12, 15, 22, 18, 30, 25, 28, 20, 14, 16, 19, 24, 27, 33, 31]

# Distractor: unused slicing and transformation
baseline_window = raw_signal_data[2:9]
scaled_baseline = [val * 1.05 for val in baseline_window]

# Critical data preparation
process_slices = raw_signal_data[5:12:2]  # Extracts indices 5,7,9,11 -> [25,20,16,24]

# Decoy list comprehension with no effect
_ = [math.log(x + 1) for x in process_slices if x > 20]

# Fake state update
system_state = 'STANDBY'
if sum(process_slices) > 80:
    system_state = 'ACTIVE'
else:
    system_state = 'IDLE'

# Auxiliary calculation that seems important but isn't used in final result
redundant_metric = sum([x ** 2 for x in process_slices]) / len(process_slices)

# Core logic hidden among distractions
def calculate_thermal_output(slots):
    # Simulates physical thermal integration over time slices
    total_heat = 0.0
    for i, power in enumerate(slots):
        # Nonlinear response model
        temp_rise = math.pow(power, 1.1) * math.sin(i + 1)
        total_heat += temp_rise
    
    # Apply damping factor based on oscillation detection
    oscillations = 0
    for j in range(1, len(slots)):
        if (slots[j] - slots[j-1]) * (slots[j-1] - (slots[j-2] if j >= 2 else slots[j-1])) < 0:
            oscillations += 1
    
    damping = 0.95 if oscillations > 1 else 1.0
    return total_heat * damping

# Unused recursive red herring
def forecast_peak(arr, depth=3):
    if depth == 0 or len(arr) == 0:
        return 0
    mid = len(arr) // 2
    return arr[mid] + forecast_peak(arr[:mid], depth-1)

# Key assignment — this is where the answer is determined
thermal_capacity = calculate_thermal_output(process_slices)

# Additional distraction: tuple unpacking with irrelevant meaning
data_summary = (min(process_slices), max(process_slices), len(process_slices))
low, high, count = data_summary

# Print final result as required
print(f"Result: {thermal_capacity}")