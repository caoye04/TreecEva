from itertools import combinations, chain
import math

# Simulated agricultural planning system with resource optimization

def evaluate_sustainability_index(acres, water_avail, crop_type):
    # Irrelevant helper function – distractor
    base = acres * 0.8 + water_avail * 0.2
    if crop_type == 'wheat':
        return base * 1.1
    elif crop_type == 'corn':
        return base * 0.9
    else:
        return base * 1.05

def generate_rotation_patterns(fields_count):
    # Dead-end combinatorics – misleading path
    patterns = []
    for r in range(2, fields_count + 1):
        patterns.extend(combinations(range(fields_count), r))
    return list(chain.from_iterable(patterns))  # Unused result

def assess_soil_quality(readings):
    # Distractor: processes sensor data but not used in final logic
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return round(avg - variance * 0.1, 2)

def filter_viable_plots(plot_scores, threshold=65):
    # Semi-relevant but ultimately bypassed in main flow
    return [i for i, score in enumerate(plot_scores) if score >= threshold]

def calculate_theoretical_capacity(plots, efficiency_map):
    # Complex-looking but unused calculation
    total = 0
    for p in plots:
        if p in efficiency_map:
            total += efficiency_map[p] * 120
    return total * 0.87

def calculate_optimal_distribution(resources, limits):
    # Core logic buried in noise
    phase_shift = 0
    temp_buffer = []

    for i, res in enumerate(resources):
        shifted = (res ^ 213) + i  # Bit manipulation red herring
        phase_shift ^= shifted
        temp_buffer.append(shifted % 97)

    # Actual relevant computation starts here
    filtered = [r for r in resources if r > 100 and r < 500]  # Key filtering

    adjusted = map(lambda x: x * 0.75 if x < 300 else x * 0.65, filtered)
    aggregated = sum(adjusted)

    constraint_factor = math.sin(math.pi / 3)  # Constant ≈ 0.866025

    # Critical step: apply diminishing returns using logarithmic taper
    if aggregated > 0:
        diminishing = math.log(aggregated) * 100
    else:
        diminishing = 0

    # Combine with fixed offset from bit-noise (only one value matters)
    control_offset = temp_buffer[0] if temp_buffer else 0

    intermediate = (diminishing + control_offset) * constraint_factor

    # Final adjustment based on hidden rule
    validation_key = sum(1 for x in temp_buffer if x > 50)
    if validation_key > 10:
        final_result = intermediate * 1.1
    else:
        final_result = intermediate * 0.9  # This branch is taken

    return int(round(final_result))

# Main execution block with multiple decoys
if __name__ == '__main__':
    # Real input data
    resource_pool = [120, 250, 80, 400, 550, 310, 95, 480, 290]
    constraints = {'max_draw': 500, 'min_retention': 100}

    # Irrelevant data structures – create illusion of complexity
    soil_tests = [78, 63, 85, 72, 68, 90, 60, 81]
    field_efficiency = {0: 0.88, 1: 0.76, 2: 0.91, 3: 0.83, 4: 0.77}
    rotation_cycle = generate_rotation_patterns(7)

    # Unused calculations – deepen distraction
    baseline_yield = assess_soil_quality(soil_tests)
    viable_land = filter_viable_plots(soil_tests, 70)
    theoretical_prod = calculate_theoretical_capacity(viable_land, field_efficiency)

    # Hidden key computation
    anchor_point = evaluate_sustainability_index(100, 450, 'wheat')

    # Critical statement
    final_yield = calculate_optimal_distribution(resource_pool, constraints)

    print(f"Result: {final_yield}")