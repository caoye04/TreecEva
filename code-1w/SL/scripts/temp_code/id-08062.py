from collections import defaultdict

# Simulate agricultural yield analysis with noise and intermediate diagnostics
def analyze_growth_cycles(data, min_threshold):
    cycle_stats = defaultdict(int)
    diagnostic_trace = []
    total_cycles = 0
    valid_cycles = 0

    for entry in data:
        growth_cycle = entry.split('-')[-1]
        measurement = int(growth_cycle[1:])
        cycle_type = growth_cycle[0]

        cycle_stats[cycle_type] += 1
        total_cycles += 1

        # Irrelevant health check (distractor)
        if measurement > 90:
            diagnostic_trace.append(f"HighAlert:{cycle_type}")

        if measurement >= min_threshold:
            valid_cycles += 1

    # Dead computation: unused aggregation (distractor)
    avg_valid_proportion = valid_cycles / total_cycles if total_cycles else 0
    spike_count = sum(1 for d in diagnostic_trace if "HighAlert" in d)

    return cycle_stats, valid_cycles

# Secondary helper with misleading parameter (distractor)
def filter_aberrations(raw_values, limit=50):
    cleaned = [v for v in raw_values if v <= limit]
    outlier_margin = max(cleaned) * 0.1  # Not used later
    return cleaned

# Core calculation with key logic interwoven with noise
def calculate_harvest_efficiency(fields, threshold):
    cumulative_base = 0
    temp_buffer = []
    shift_offset = 3  # Distractor variable

    for field in fields:
        # Parse field string: e.g., "plotA:S23,T18,R45"
        name, readings = field.split(':')
        values = [int(r[1:]) for r in readings.split(',')]
        types = [r[0] for r in readings.split(',')]

        # Slice-based filtering (relevant)
        recent_phase = readings.split(',')[1:]  # Skip first reading
        recent_vals = [int(v[1:]) for v in recent_phase]

        # Count distribution using collections (required feature)
        type_counter = defaultdict(int)
        for t in types:
            type_counter[t] += 1

        # Key efficiency heuristic
        base_yield = sum(values) // len(values)
        diversity_penalty = len(type_counter) - 1

        # Noise: irrelevant transformation chain
        scaled_buffer = [v * 2 for v in recent_vals]
        shifted_back = [v // 2 for v in scaled_buffer]
        temp_buffer.extend(shifted_back)  # Accumulates but unused

        # Actual contribution to result
        if base_yield >= threshold:
            adjusted_yield = base_yield - diversity_penalty
            cumulative_base += adjusted_yield

        # Fake state tracking (distractor)
        status_log = []
        for idx, val in enumerate(values):
            if val > threshold:
                status_log.append(f"{name}-phase{idx}:OK")

    # Final adjustment using string method (required feature)
    debug_tag = "YIELD_FINAL"
    tag_parts = debug_tag.lower().split('_')
    correction_factor = len(tag_parts)  # Always 2

    final_yield = cumulative_base * correction_factor

    # Print required output format
    print(f"Result: {final_yield}")
    return final_yield

# Input data setup
field_data = [
    "plotA:S23,T18,R45",
    "plotB:T30,S40,R25",
    "plotC:R50,S20,T35",
    "plotD:S60,T55,R40"
]

threshold = 35

# Execute main logic
final_yield = calculate_harvest_efficiency(field_data, threshold)