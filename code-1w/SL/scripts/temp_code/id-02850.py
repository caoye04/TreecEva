from itertools import combinations

# Simulate hourly network bandwidth usage (in Mbps) across different departments
tech_teams = ['alpha', 'beta', 'gamma']
schedule_hours = [9, 10, 11, 13, 14, 15]
base_loads = {'alpha': 12.5, 'beta': 18.3, 'gamma': 15.7}
dynamic_spikes = [2.1, 3.4, 1.8, 2.9, 3.3]

# Initialize tracking variables
hourly_contributions = {}
overlap_count = 0
temp_aggregates = []

# Generate synthetic load profile for each hour
for hour in schedule_hours:
    total_load = 0
    active_combinations = list(combinations(tech_teams, 2))  # Simulate pair collaborations

    # Calculate base + overlap effects
    for team in tech_teams:
        if team == 'beta' and hour == 13:
            total_load += base_loads[team] * 0.5  # Reduced load during lunch break
        else:
            total_load += base_loads[team]

    # Add spike only if not midday lull
    if hour != 13:
        spike_index = (hour + len(tech_teams)) % len(dynamic_spikes)
        total_load += dynamic_spikes[spike_index]

    # Track hourly contribution for later analysis
    hourly_contributions[hour] = round(total_load, 2)

    # Count overlaps (distractor logic)
    if len(active_combinations) > 2:
        overlap_count += 1

# Extract usage levels from the recorded data
usage_levels = list(hourly_contributions.values())

# Apply smoothing filter (irrelevant to final answer but adds cognitive load)
smoothed = [round((usage_levels[i] + usage_levels[i-1]) / 2, 2) for i in range(1, len(usage_levels))]
temp_aggregates.append(sum(smoothed))

# Normalize values just before peak detection (distraction)
normalized_offsets = [x - min(usage_levels) for x in usage_levels]

# Key statement: determine maximum observed capacity
peak_capacity = max(usage_levels)

# Additional irrelevant post-processing
if peak_capacity > 60:
    adjusted_peak = peak_capacity * 0.95
else:
    adjusted_peak = peak_capacity + 2.1

temp_aggregates.append(adjusted_peak)

# Output target result
print(f"Result: {peak_capacity}")