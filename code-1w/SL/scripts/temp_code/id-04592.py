from collections import defaultdict
from itertools import cycle

# Simulate hourly power grid load data over 3 days
time_slots = [f'H{i}' for i in range(24)]
days = ['Mon', 'Tue', 'Wed']
grid_loads = [
    [180 + (i * 2) % 25 - j*3 for i in range(24)] for j in range(3)
]

# Misleading auxiliary metrics (distractor variables)
wasted_energy = 0
redundant_metric_log = []
phase_shift = 0.0

# Secondary tracking structure with irrelevant aggregation
daily_stats = defaultdict(lambda: {
    'total': 0, 'fluctuation': 0, 'baseline_dev': 0
})

# Spurious helper function that is called but doesn't affect main result
def calculate_phase_stability(readings):
    stability_score = 0
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            stability_score += 0.5
        else:
            stability_score -= 0.2
    return round(stability_score, 2)

# Another red herring: frequency drift analysis (unused)
def analyze_drift(pattern):
    drift = 0
    for val in pattern[::3]:
        drift += (val % 7) / 2.5
    return drift

# Core diagnostic logic with key computation chain
def system_diagnostic(load_profiles):
    peak_capacity = 0
    cumulative_pressure = 0
    transient_buffer = []

    # Real processing with meaningful steps
    for day_idx, daily_load in enumerate(load_profiles):
        daily_peak = max(daily_load)
        baseline = sum(daily_load) / len(daily_load)
        
        # Track real-time pressure deviations
        for hour_load in daily_load:
            if hour_load > baseline * 1.15:
                cumulative_pressure += (hour_load - baseline) * 0.1

        # Update primary metric
        if daily_peak > peak_capacity:
            peak_capacity = daily_peak

        # Irrelevant per-day side calculation (distractor)
        fluctuation = sum(
            abs(daily_load[i] - daily_load[i-1]) 
            for i in range(1, len(daily_load))
        )
        daily_stats[days[day_idx]]['fluctuation'] = fluctuation
        daily_stats[days[day_idx]]['total'] = sum(daily_load)

        # Call to misleading function (adds cognitive load)
        stability = calculate_phase_stability(daily_load)
        redundant_metric_log.append(stability)

    # Additional distraction: simulate buffer overflow check
    for _ in range(5):
        transient_buffer.append(cumulative_pressure * 0.1)
        phase_shift += transient_buffer[-1] / 2.7

    # Final adjustment using combined factors (only peak_capacity matters)
    final_peak = peak_capacity + int(cumulative_pressure // 10)
    
    # This line is the key execution point
    return {'final_peak': final_peak, 'pressure_index': cumulative_pressure}

# Execute core workflow
load_cycle = cycle(grid_loads)
spurious_snapshot = next(load_cycle)  # Unused

# Critical statement
final_analysis = system_diagnostic(grid_loads)

# Extract and print the target result
peak_capacity = final_analysis['final_peak']
print(f"Result: {peak_capacity}")