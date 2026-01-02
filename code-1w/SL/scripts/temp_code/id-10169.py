def analyze_throughput(data, threshold=150):
    filtered = [x for x in data if x > threshold]
    return sum(filtered) // len(filtered) if filtered else 0


def adjust_latency(base, factor):
    # Irrelevant computation
    temp = base * 1.8 + 32
    return base * (1 + 0.1 * min(factor, 3))

# Simulated sensor readings over time
readings = [120, 160, 180, 95, 200, 140, 210, 175]

# Extraneous list comprehension with unused result
smoothed_readings = [round((r + readings[i-1] + readings[i+1]) / 3) 
                     for i, r in enumerate(readings) 
                     if 0 < i < len(readings) - 1]

# Historical averages (distractor)
historical_avg = sum(readings) / len(readings)
spike_count = len([x for x in readings if x > 170])

# Core processing chain
baseline = analyze_throughput(readings)
adjusted_baseline = adjust_latency(baseline, spike_count)

# Buffer levels with slicing to extract recent trends
raw_levels = [baseline * 0.8, baseline * 1.1, baseline * 0.95, adjusted_baseline]
recent_levels = raw_levels[-3:]  # Use last three only

# Secondary adjustment path (not used but looks important)
projected = [level * 1.05 for level in recent_levels]
deferred_projection = sum(projected) / len(projected)

# Optimization function
def optimize_buffer(levels):
    total = sum(level for level in levels if level > baseline)
    penalty = 0
    for lvl in levels:
        if lvl < baseline * 0.9:
            penalty += 5
    return int(total - penalty)

final_capacity = optimize_buffer(recent_levels)
print(f"Result: {final_capacity}")