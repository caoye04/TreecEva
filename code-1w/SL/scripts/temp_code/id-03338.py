import math

# Simulated sensor data and calibration values
data_stream = [3, 8, 15, 22, 31, 40, 51, 64, 79, 96]
baseline_offset = 2
amplification_factor = 1.5
noise_floor = 5

# Irrelevant calibration curve (distractor)
calibration_lookup = {i: round(math.sin(i * 0.1) * 100, 2) for i in range(10)}

# Preprocessing: extract candidates above noise threshold
filtered_data = []
for val in data_stream:
    adjusted = val - baseline_offset
    if adjusted > noise_floor:
        filtered_data.append(adjusted)

# Secondary processing: map to growth rate using lambda (semi-relevant)
growth_mapper = lambda x: int(math.sqrt(x))
signal_strengths = [growth_mapper(x) for x in filtered_data]

# Accumulate trend deviations (only some contribute to final result)
trend_deviation = 0
deviation_count = 0
for i, strength in enumerate(signal_strengths):
    if i % 2 == 0:
        trend_deviation += strength * 1.1
        deviation_count += 1
    else:
        # Unused path (dead logic)
        temp_adj = strength * 0.9

# Helper function to compute weighted signal output
def process_signals(signals):
    base_sum = sum(signals)
    penalty = 0
    for s in signals:
        if s > 7:
            penalty += 2
    # Final adjustment based on empirical threshold
    if base_sum > 50:
        return int((base_sum - penalty) * 0.8)
    else:
        return int(base_sum - penalty)

# Critical execution point
final_output = process_signals(filtered_data)

# Print result for evaluation
print(f"Target result: {final_output}")