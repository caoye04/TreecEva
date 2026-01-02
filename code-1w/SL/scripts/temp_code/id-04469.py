def analyze_growth_patterns(data, limit):
    cumulative_score = 0
    temp_buffer = []
    for i in range(len(data)):
        if data[i] > limit:
            temp_buffer.append(data[i] * 0.85)
        else:
            temp_buffer.append(data[i] * 1.1)
    adjusted_values = [x for x in temp_buffer if x > 0]
    return sum(adjusted_values[:len(adjusted_values)//2])


def calculate_harvest_efficiency(fields, thresh):
    base_total = 0
    penalty_factor = 0.9
    buffer_sum = 0
    
    # Real logic begins: process field zones above threshold
    high_yield_zones = [zone for zone in fields if max(zone) > thresh]
    avg_sizes = [sum(zone) / len(zone) for zone in high_yield_zones]
    
    # Secondary derived metric (not used in final answer but looks important)
    size_variance = [abs(x - sum(avg_sizes)/len(avg_sizes)) for x in avg_sizes]
    for var in size_variance:
        buffer_sum += var * 0.1  # Distractor computation

    # Core calculation
    for i, zone in enumerate(high_yield_zones):
        if i % 2 == 0:
            base_total += sum(zone) * penalty_factor
        else:
            base_total += sum(zone) * 1.05
    
    # Additional red herring: simulate soil depletion
    depletion_rate = 0.03
    projected_loss = 0
    for _ in range(5):
        projected_loss += base_total * depletion_rate
        base_total -= projected_loss  # Not actually correct usage — misleading!

    # Reset correction: the previous loop was a simulation distraction
    base_total = 0
    relevant_zones = fields[1:-1]  # Exclude first and last
    filtered_zones = [z for z in relevant_zones if any(x >= thresh for x in z)]
    
    for zone in filtered_zones:
        slice_center = zone[len(zone)//4 : len(zone)//4*3]
        base_total += sum(slice_center)

    return int(base_total)

# Simulated agricultural field sensor data (unit: kg yield per hectare)
field_data = [
    [120, 135, 100, 98],
    [150, 160, 158, 152, 145],
    [180, 178, 182, 177, 185, 180],
    [140, 138, 142],
    [200, 190, 195]
]

threshold = 150

# Misleading preliminary analysis
initial_estimate = analyze_growth_patterns([sum(f) for f in field_data], 500)
dummy_correction = initial_estimate * 0.02

final_yield = calculate_harvest_efficiency(field_data, threshold)
print(f"Result: {final_yield}")