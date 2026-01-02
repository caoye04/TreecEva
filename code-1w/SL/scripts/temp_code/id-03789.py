def analyze_phase_shift(data, reference):
    shift_count = 0
    temp_buffer = []
    for i in range(len(data)):
        if data[i] > reference:
            shift_count += 1
            temp_buffer.append(data[i] * 0.95)
    return shift_count

initial_readings = [23, 45, 67, 89, 12, 34, 56, 78]
baseline = 50

# Misleading computation - not used in final result
drift_compensation = sum(x ** 0.5 for x in initial_readings if x < baseline) / len(initial_readings)

adjusted_readings = [x * 1.05 for x in initial_readings]
fluctuations = [abs(adjusted_readings[i] - adjusted_readings[i-1]) for i in range(1, len(adjusted_readings))]

# Create threshold set using set operations (union and difference)
high_values = {x for x in fluctuations if x > 20}
low_values = {x for x in fluctuations if x < 10}
threshold_set = high_values.difference(low_values).union({5, 10, 15})

# Auxiliary function with red herring logic
def estimate_noise_level(vals):
    if len(vals) == 0:
        return 0
    peak = max(vals)
    avg = sum(vals) / len(vals)
    return (peak - avg) * 0.7  # Unused in main calculation

# Another irrelevant tracking block
counter_states = []
for val in fluctuations:
    if val > 25:
        counter_states.append('HIGH')
    elif val > 15:
        counter_states.append('MEDIUM')
    else:
        counter_states.append('LOW')

# Core calculation function
def calculate_thermal_capacity(seq, limit_set):
    total_energy = 0
    decay_factor = 0.8
    for i, val in enumerate(seq):
        if val in limit_set:
            contribution = val * (decay_factor ** i)
            total_energy += contribution
    return int(total_energy)  # Final answer is integer

# Critical statement
thermal_capacity = calculate_thermal_capacity(fluctuations, threshold_set)

print(f"Result: {thermal_capacity}")