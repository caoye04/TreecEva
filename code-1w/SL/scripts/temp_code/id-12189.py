def analyze_distribution(data_flow):
    base_offset = 17
    temp_cache = [0] * len(data_flow)
    audit_log = []

    for idx, value in enumerate(data_flow):
        shifted = value ^ base_offset
        if shifted > 30:
            shifted = shifted % 13
        temp_cache[idx] = shifted * 2

    # Simulate zone-based aggregation with redundant tracking
    zone_bounds = [i for i in range(0, len(temp_cache), 3)]
    active_zones = 0
    zone_weights = []

    for bound in zone_bounds:
        if bound + 2 < len(temp_cache):
            region_sum = sum(temp_cache[bound:bound+3])
            normalized = region_sum % 11
n            zone_weights.append(normalized)
            if normalized > 5:
                active_zones += 1

    # Dummy correlation pass (distractor)
    correlations = set()
    for a, b in zip(zone_weights, zone_weights[1:]):
        correlations.add((a % 4, b % 4))

    # Secondary scan for outlier detection (partially irrelevant)
    outlier_flags = {}
    for i, val in enumerate(temp_cache):
        if val % 7 == 0 and val > 10:
            outlier_flags[i] = True

    # Core logic disguised among noise
    aggregate = 0
    multiplier = 1
    for i, v in enumerate(temp_cache):
        if i % 2 == 0:
            aggregate += v * multiplier
            multiplier += 1

    # Additional red herring computation
    dummy_series = []
    for _ in range(3):
        dummy_val = (multiplier * 19) % 23
        dummy_series.append(dummy_val)
        multiplier -= 1

    final_tally = aggregate % 97

    # Critical statement
    equilibrium_score = final_tally // (active_zones + 1)

    print(f"Target result: {equilibrium_score}")

# Input setup
input_sequence = [24, 18, 15, 30, 22, 10, 40]
analyze_distribution(input_sequence)