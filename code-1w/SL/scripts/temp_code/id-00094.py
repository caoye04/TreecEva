import math
from collections import defaultdict

def calculate_signal_degradation(modulation_factors, time_points):
    degradation_map = defaultdict(float)
    for factor in modulation_factors:
        for t in time_points:
            log_gain = math.log(t + 1) if t > 0 else 0
            exp_decay = math.exp(-factor * t)
            degradation_value = exp_decay * log_gain
            degradation_map[factor] += degradation_value
    return degradation_map

mod_factors = [0.1, 0.2, 0.3]
time_points = range(1, 6)

signal_degradation = calculate_signal_degradation(mod_factors, time_points)

aggregate_degradation_score = 0.0
for factor in mod_factors:
    weighted_sum = signal_degradation[factor] * (1.5 if factor < 0.25 else 0.75)
    aggregate_degradation_score += weighted_sum if weighted_sum > 0.1 else 0

print(f"Result: {round(aggregate_degradation_score, 4)}")