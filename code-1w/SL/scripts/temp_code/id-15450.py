from itertools import cycle, islice

def analyze_soil_composition(elements):
    # Irrelevant function: calculates sum of squares but not used in final result
    return sum(x ** 2 for x in elements if x > 0)


def preprocess_sensor_data(raw_data):
    # Distractor: processes data but ultimately unused
    cleaned = [x for x in raw_data if isinstance(x, (int, float))]
    normalized = [(x - min(cleaned)) / (max(cleaned) - min(cleaned)) for x in cleaned]
    return [round(x, 3) for x in normalized]


def generate_growth_phases(cycles):
    # Creates a sequence but only length matters
    phase_pattern = ['germination', 'growth', 'flowering']
    return list(islice(cycle(phase_pattern), cycles * 3))


def evaluate_stress_factors(temp_log, moisture_levels):
    # Complex logic with red herring variables
    stress_index = 0
    peaks = []
    for i, temp in enumerate(temp_log):
        if temp > 35:
            stress_index += 1
            if i < len(moisture_levels) and moisture_levels[i] < 30:
                peaks.append((i, temp))
    # Dead code path: never accessed
    if False:
        stress_index = stress_index << 2
    return stress_index  # Partially computed but not critical


def calculate_harvest_efficiency(metrics, cycles):
    # Core calculation hidden among distractions
    base_area = metrics.get('core_area', 0)
    loss_factor = metrics.get('edge_loss', 0.15)
    efficiency_ratings = metrics.get('ratings', [])
    
    # Real computation begins
    adjusted_area = base_area * (1 - loss_factor)
    
    # Simulate yield per cycle using bit manipulation trick
    cycle_mask = (1 << len(cycles)) - 1  # bitmask based on number of cycles
    base_yield_per_unit = (cycle_mask ^ 0b101) + (cycle_mask & 0b110)  # XOR and AND mix
    
    # Use of lambda and zip: relevant step
    modifiers = list(map(lambda x: round(1 + 0.1 * (x - 2), 2), range(len(cycles))))
    total_adjustment = sum(m * 0.5 for m in modifiers)  # only half applied
    
    # Key step: actual yield calculation
    raw_yield = adjusted_area * base_yield_per_unit
    
    # Apply rating multiplier: average of non-extreme ratings
    trimmed_ratings = [r for r in efficiency_ratings if 2 < r < 9]
    rating_multiplier = sum(trimmed_ratings) / len(trimmed_ratings) if trimmed_ratings else 1.0
    
    final_yield = int(raw_yield * rating_multiplier * (1 + total_adjustment / 10))
    
    # Decoy assignment
    final_yield = final_yield + 0  # no-op
    
    return final_yield

# Main execution block
if __name__ == '__main__':
    # Input data setup
    area_metrics = {
        'core_area': 127,
        'edge_loss': 0.18,
        'ratings': [3, 5, 7, 4, 8, 2, 9],  # 2 and 9 excluded in trimming
        'calibration': [0.1, 0.3, 0.2],
        'meta': 'irrelevant'
    }

    growth_cycles = [2, 4, 6, 8]

    # Irrelevant preprocessing calls
    sensor_input = [23, 36, 29, 41, 33, 37, 25]
    _ = preprocess_sensor_data(sensor_input)
    _ = analyze_soil_composition([12, 0, 8, -3, 5])

    # Unused complex structure
    timeline = dict(zip(generate_growth_phases(len(growth_cycles)), range(len(growth_cycles) * 3)))

    # Stress evaluation not affecting final yield
    _ = evaluate_stress_factors([34, 36, 38, 32], [40, 25, 20, 50])

    # Critical statement
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

    print(f"Result: {final_yield}")