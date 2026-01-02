from itertools import compress, cycle
import math

# Simulate environmental sensor readings with noise
turbidity_readings = [0.4, 1.2, 3.5, 0.9, 2.1, 4.8, 1.3, 0.7, 5.6, 3.3]
ph_levels = [6.8, 7.2, 6.5, 7.0, 6.4, 7.5, 6.9, 7.1, 6.3, 7.4]
chlorine_residual = [0.2, 0.4, 0.1, 0.5, 0.0, 0.6, 0.3, 0.4, 0.1, 0.5]

# Irrelevant transformation: normalize ph to arbitrary scale (distraction)
normalized_ph = list(map(lambda x: round((x - 6) * 10), ph_levels))

# Generate time-based weighting for no clear purpose (red herring)
time_weights = [round(1 / (t + 1), 3) for t in range(len(turbidity_readings))]
weighted_turbidity = [a * b for a, b in zip(turbidity_readings, time_weights)]

# Mask high-turbidity events (partially relevant preprocessing)
high_alert_threshold = 3.0
turbid_alerts = [x > high_alert_threshold for x in turbidity_readings]

# Filter elements above threshold (actual signal path)
filtered_elements = [x for x, alert in zip(turbidity_readings, turbid_alerts) if alert]

# Decoy function: appears useful but unused
def analyze_purity(data):
    return sum(x ** 0.5 for x in data if x > 0.5)

# Fake diagnostic chain with dead-end logic
baseline_drift = sum(1 for x in ph_levels if x < 6.8)
countermeasures = []
if baseline_drift > 3:
    countermeasures = ['reagent_dose', 'aeration']
elif baseline_drift == 2:
    countermeasures = ['aeration']
else:
    countermeasures = ['monitor_only']  # Dead branch (never taken due to data)

# Efficiency map based on chlorine and turbidity interaction (critical lookup)
efficiency_map = {}
for i, (turb, chlor) in enumerate(zip(turbidity_readings, chlorine_residual)):
    if chlor >= 0.3:
        efficiency = max(0.3, 0.9 - (turb * 0.15))
    else:
        efficiency = max(0.1, 0.5 - (turb * 0.1))
    efficiency_map[i] = round(efficiency, 3)

# Spurious use of itertools: creates illusion of complex processing (distractor)
duplicated_indices = list(compress(range(len(turbidity_readings)), cycle([1, 0])))
decoy_projection = [efficiency_map[i] for i in duplicated_indices if i < len(efficiency_map)]

# Real processing function: computes weighted impact score
def process_contaminants(elements, efficiency_lookup):
    total_index = 0.0
    base_factor = 1.75
    
    # Map filtered elements back to original indices
    indices = [i for i, x in enumerate(turbidity_readings) if x in elements]
    
    # Apply efficiency-weighted scoring
    for elem, idx in zip(elements, indices):
        raw_score = elem * base_factor
        efficiency = efficiency_lookup.get(idx, 0.2)
        adjusted_score = raw_score * efficiency
        total_index += adjusted_score
    
    # Secondary adjustment using unused ph correlation (misleading intermediate)
    ph_influence = sum(abs(ph - 7.0) for ph in ph_levels) / len(ph_levels)
    final_adjustment = total_index * (1 + ph_influence * 0.1)  # Minor perturbation
    
    return int(round(final_adjustment))

# Critical statement: compute final filtration score
filtration_score = process_contaminants(filtered_elements, efficiency_map)

# Superfluous post-processing (distraction)
status_flags = {0: 'OK', 1: 'WARNING', 2: 'CRITICAL'}
alert_level = min(2, max(0, int(filtration_score // 10)))
system_status = status_flags.get(alert_level, 'UNKNOWN')

# Output target result
print(f"Result: {filtration_score}")