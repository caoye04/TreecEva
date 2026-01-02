from itertools import combinations, chain
import math

# Simulated sensor readings with noise and redundancy
temperature_readings = [23.4, 24.1, 22.9, 25.0, 23.8, 24.2, 23.7]
humidity_readings = [45, 47, 44, 50, 46, 48, 45]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1013, 1011]

# Irrelevant derived metrics (distractors)
avg_temp = sum(temperature_readings) / len(temperature_readings)
temp_variance = sum((t - avg_temp) ** 2 for t in temperature_readings) / len(temperature_readings)
hum_max_window = max(humidity_readings[i:i+3] for i in range(len(humidity_readings)-2))

# Decoy function - looks important but unused
def analyze_trend(data):
    return [b - a for a, b in zip(data, data[1:])]

# Unused transformation pipeline
trend_hum = lambda seq: list(map(lambda x: x[1] - x[0], zip(seq, seq[1:])))
humidity_deltas = trend_hum(humidity_readings)  # Dead-end computation

# Red herring: complex combinatorics on pressure (not ultimately used)
pressure_pairs = list(combinations(pressure_readings, 2))
pressure_diffs = [abs(a - b) for a, b in pressure_pairs]
mean_pressure_diff = sum(pressure_diffs) / len(pressure_diffs)

# Key data preprocessing
valid_temps = [t for t in temperature_readings if 23.0 <= t <= 24.5]
filtered_humidity = [h for h, t in zip(humidity_readings, temperature_readings) if t > 23.5]

# Misleading intermediate fusion (looks like scoring but isn't final)
raw_fusion = []
for t, h in zip(valid_temps, filtered_humidity[:len(valid_temps)]):
    raw_fusion.append(t * 1.5 + h * 0.8)

baseline_offset = math.log(sum(filtered_humidity))

# Real processing begins here — nested logic with distractors
adjustment_factor = 0.0
if len(valid_temps) > 3:
    adjustment_factor += 0.3
    temp_range = max(valid_temps) - min(valid_temps)
    if temp_range < 1.5:
        adjustment_factor += 0.4
        # Bit manipulation red herring
        encoded = 0
        for val in pressure_readings:
            encoded ^= int(val % 8) << 2
        adjustment_factor -= (encoded & 7) * 0.05  # Minor misleading tweak

# More irrelevant calculations
synthetic_series = list(chain.from_iterable([(t*2, h//5) for t, h in zip(temperature_readings, humidity_readings)]))
synth_stats = {
    'max_pair': max(synthetic_series[::2]),
    'sum_quartile': sum(s for s in synthetic_series if s < 50)
}

# Core logic buried in distractions
def compute_aggregate(temps, hums, base_adj):
    n = len(temps)
    if n == 0:
        return 0.0
    
    # Weighted average with conditional scaling
    weights = [0.9 + 0.2 * (i / n) for i in range(n)]
    weighted_sum = sum(t * w for t, w in zip(temps, weights))
    
    # Conditional bonus based on humidity stability
    hum_stable = all(abs(h1 - h2) <= 3 for h1, h2 in zip(hums, hums[1:]))
    stability_bonus = 1.15 if hum_stable else 1.0
    
    # Integer division rounding effect
    base_floor = int(base_adj * 10) // 2  # Uses baseline_offset indirectly
    
    # Final composition
    intermediate = (weighted_sum * stability_bonus) / n
    final_value = intermediate + base_floor * 0.1 + adjustment_factor
    
    # Distractor: modify unused global
    globals()['last_intermediate'] = intermediate * 2  # Not used
    
    return round(final_value, 6)

# Secondary decoy function
def calculate_redundant_index(seq):
    return sum(math.sin(x) for x in seq) % 7

redundant_idx = calculate_redundant_index(temperature_readings)  # Dead end

# Critical execution point
final_score = compute_aggregate(valid_temps, filtered_humidity, baseline_offset)

# Output the required result
print(f"Result: {final_score}")