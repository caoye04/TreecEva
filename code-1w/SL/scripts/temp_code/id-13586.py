import math

def analyze_growth_rate(data):
    # Irrelevant helper function – dead code path
    return sum(x ** 0.5 for x in data if x > 10)

def preprocess_soil_metrics(raw):
    # Distractor transformation – never used in final computation
    processed = [x * 1.7 + 2 for x in raw]
    normalized = [p / max(processed) for p in processed]
    return [round(n, 3) for n in normalized]

def calculate_harvest_efficiency(area_data, limit):
    total_yield = 0
    penalty_factor = 0.85
    boost_count = 0

    # Real logic begins: filter zones above threshold
    valid_zones = [z for z in area_data if z['output'] > limit]

    # Decoy accumulator – looks important but unused
    fake_accumulator = 0
    for zone in valid_zones:
        fake_accumulator += zone['output'] * 0.1  # red herring

    # Actual yield calculation with nested logic
    for i, zone in enumerate(valid_zones):
        base = zone['output']
        elevation = zone['elev']

        # Bitwise condition to obscure control flow
        if (i + 1) & 3 == 0:  # every 4th index (when 1-indexed)
            base *= 1.1

        # Conditional boost based on elevation using short-circuit logic
        elevation_bonus = (elevation > 150) and (base * 0.05) or 0
        if elevation_bonus:
            boost_count += 1

        # Apply penalty if soil pH is missing (decoy check, always false)
        if 'ph' in zone and zone['ph'] < 5.5:
            base *= penalty_factor  # never reached

        total_yield += base + elevation_bonus

    # Secondary transformation with zip and enumerate (actual use)
    adjustments = [0.95, 1.05, 1.0, 0.9, 1.1]  # fixed adjustment curve
    chunks = [total_yield / 5] * 5
    for idx, (chunk, adj) in enumerate(zip(chunks, adjustments)):
        chunks[idx] = chunk * adj  # minor real adjustment

    adjusted_total = sum(chunks)

    # Final step: combinatorics-based correction factor
    n = len(valid_zones)
    k = boost_count or 1
    combinations = math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) if n >= k else 1

    # Real answer derivation
    final_yield = int(adjusted_total - combinations)  # deterministic integer result

    # Red herring: unrelated list comprehension with side-effect-free mutation
    _ = [z.update({'temp_flag': False}) for z in area_data if 'neighbors' in z]

    return final_yield

# Main execution block
if __name__ == '__main__':
    region_data = [
        {'output': 230, 'elev': 120, 'zone_id': 'A1'},
        {'output': 180, 'elev': 160, 'zone_id': 'A2'},
        {'output': 210, 'elev': 180, 'zone_id': 'A3', 'neighbors': ['A4']},
        {'output': 190, 'elev': 140, 'zone_id': 'A4'},
        {'output': 250, 'elev': 200, 'zone_id': 'A5', 'neighbors': ['A6']},
        {'output': 220, 'elev': 170, 'zone_id': 'A6'}
    ]

    # Unused variables – distractions
    baseline_metrics = [d['output'] for d in region_data]
    avg_output = sum(baseline_metrics) / len(baseline_metrics)
    scaled_outputs = [int(x * 0.97) for x in baseline_metrics]
    sorted_pairs = [(i, v) for i, v in enumerate(scaled_outputs)]

    # Noise: irrelevant bitwise operations
    magic_seed = 0
    for val in scaled_outputs:
        magic_seed ^= (val << 2) | 0x5F

    threshold = 200
    final_yield = calculate_harvest_efficiency(region_data, threshold)

    # Output must follow required format
    print(f"Target result: {final_yield}")