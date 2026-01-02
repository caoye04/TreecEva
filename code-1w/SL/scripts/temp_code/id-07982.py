from collections import defaultdict, Counter
import itertools

# Simulated sensor data stream with noise and redundant channels
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.4, 26.1]
humidity_readings = [45, 47, 44, 46, 48, 50, 52]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1017]

# Irrelevant auxiliary metrics (distractor)
signal_strengths = [88, 92, 85, 90, 87, 91, 89]
battery_levels = [78, 76, 79, 75, 77, 74, 72]

# Data alignment using zip (real use)
synchronized_data = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Compute baseline environmental index (relevant)
environment_index = 0
for i, (t, h, p) in enumerate(synchronized_data):
    environment_index += (t * 1.2) + (h * 0.5) - (p / 100)

# Misleading transformation on irrelevant data (red herring)
decoy_aggregate = 0
for strength, battery in zip(signal_strengths, battery_levels):
    decoy_aggregate += (strength ^ battery) & 15  # Bitwise red herring

def compute_stability_factor(data_stream):
    """Real processing function: computes variance-based stability"""
    mean_val = sum(data_stream) / len(data_stream)
    variance = sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)
    return 100 - (variance * 2)  # Higher = more stable

# Apply stability analysis to temperature (relevant)
temp_stability = compute_stability_factor(temperature_readings)

# Fake recursive diagnostic (dead path)
def recursive_noise_accumulator(n, acc=0):
    if n <= 0:
        return acc
    return recursive_noise_accumulator(n - 1, acc ^ (n % 7))

fake_diagnostic = recursive_noise_accumulator(len(battery_levels))  # Distractor

# Real health signal extraction via lambda filter
valid_readings_filter = lambda x: 22 <= x[0] <= 25 and 44 <= x[1] <= 50
filtered_data = list(filter(valid_readings_filter, synchronized_data))

# Aggregate from filtered set
aggregate_health_score = 0
for t, h, p in filtered_data:
    aggregate_health_score += int(t) + (h // 2) + (p % 50)

# Decoy dictionary with unused stats (distractor structure)
analysis_dump = defaultdict(int)
for reading in itertools.chain(temperature_readings, humidity_readings):
    analysis_dump[f'raw_{reading}'] += int(reading % 10)

# Unused combinatorial sweep (misdirection)
all_combinations = list(itertools.combinations([temp_stability, decoy_aggregate, fake_diagnostic], 2))
combination_weights = [abs(a - b) * 0.1 for a, b in all_combinations]  # Never used

# System offset derived from bit manipulation of key metrics
system_offset = int(temp_stability) & 255
system_offset ^= len(filtered_data)
system_offset += (environment_index // 10) % 100

# Final diagnostic fusion (key statement)
final_diagnostic = aggregate_health_score + system_offset

# Output target result
print(f"Result: {final_diagnostic}")