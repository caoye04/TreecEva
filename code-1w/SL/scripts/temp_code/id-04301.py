def analyze_noise(data, threshold=0.5):
    """Irrelevant function: analyzes signal noise (dead code path)"""
    count = 0
    for val in data:
        if abs(val) > threshold:
            count += 1
    return count

# Irrelevant constants and decoy data
SIGNAL_NOISE_FLOOR = 0.17
CALIBRATION_OFFSETS = [0.01, -0.02, 0.003, -0.001]
TEMPORAL_WEIGHTS = {'t1': 0.8, 't2': 1.2, 't3': 0.9}

# Misleading intermediate computation with unused result
aggregate_score = sum([SIGNAL_NOISE_FLOOR * w for w in TEMPORAL_WEIGHTS.values()]) + len(CALIBRATION_OFFSETS)

# Real data: crop yield fluctuation factors over 6 seasons
fluctuations = [1.1, 0.9, 1.05, 1.2, 0.8, 1.15]

# Configuration dictionary — key to actual logic
config = {
    'base_yield_per_acre': 120,
    'acres': 85,
    'decay_rate': 0.015,
    'boost_multiplier': 1.25,
    'enable_boost': False  # This will be toggled conditionally
}

# Decoy transformation on fluctuations (not used in final calculation)
decayed_fluctuations = []
for i, f in enumerate(fluctuations):
    decayed_fluctuations.append(f * (1 - config['decay_rate']) ** i)

# Another red herring: sorting but storing in irrelevant variable
sorted_desc = sorted(fluctuations, reverse=True)
sorted_asc = sorted(fluctuations)  # unused
median_val = (sorted_desc[2] + sorted_desc[3]) / 2  # looks important, isn't used

# Conditional boost activation based on hidden pattern
if sum(1 for x in fluctuations if x > 1.0) >= 4:
    config['enable_boost'] = True

# Dictionary-based seasonal adjustment map (only some entries are logically relevant)
adjustment_map = {
    0: 1.02,  # spring
    1: 0.98,  # summer
    2: 1.01,  # monsoon
    3: 1.03,  # autumn
    4: 0.97,  # early winter
    5: 0.96   # late winter
}

# Core calculation function — combines arithmetic, conditional logic, dict lookup, and assignments
def calculate_harvest(factors, cfg):
    total_adjusted_yield = 0.0
    base = cfg['base_yield_per_acre']
    acres = cfg['acres']
    multiplier = cfg['boost_multiplier'] if cfg['enable_boost'] else 1.0

    # Apply season-specific adjustments and accumulate
    for idx, factor in enumerate(factors):
        adjusted_factor = factor * adjustment_map.get(idx % 6, 1.0)
        seasonal_yield = base * adjusted_factor * acres
        total_adjusted_yield += seasonal_yield

    # Final scaling with optional boost
    final = total_adjusted_yield * multiplier

    # Distractor: normalize by number of seasons (looks like correction, but not applied)
    average_per_season = final / len(factors)  # computed but unused

    return final

# Critical execution point
final_yield = calculate_harvest(fluctuations, config)

# Print target result
print(f"Target result: {final_yield}")