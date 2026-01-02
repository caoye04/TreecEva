def analyze_efficiency(metrics):
    efficiency_list = [m * 0.85 for m in metrics if m > 10]
    adjusted = sum(efficiency_list) / len(efficiency_list) if efficiency_list else 0
    return adjusted

metrics_data = [12, 15, 8, 20, 5, 18]
baseline_efficiency = analyze_efficiency(metrics_data)

status_flags = {1, 3, 4, 6, 7}
diagnostic_codes = {2, 4, 6, 8, 10}
overlap_diagnostics = status_flags & diagnostic_codes

redundant_checkpoints = []
for i in range(1, 10):
    if i % 2 == 0:
        redundant_checkpoints.append(i ** 2)

sequence_values = [x for x in range(5, 26, 3)]
filtered_sequence = [y for y in sequence_values if y % 2 == 1]

scaling_factor = 1.75
primary_units = [3, 7, 9, 11]
secondary_units = [(u + 1) // 2 for u in primary_units]

def calculate_system_capacity(units):
    temp_storage = []
    cumulative = 0
    
    for idx, val in enumerate(units):
        shifted = val << 1
        if idx % 2 == 0:
            shifted -= 3
        temp_storage.append(shifted)
        
        # Core logic step
        base = val * scaling_factor
        offset = (idx + 1) ** 2
        cumulative += int(base) - offset
    
    # Misleading intermediate calculation
    phantom_sum = sum(temp_storage) // 2 if temp_storage else 0
    decoy_value = phantom_sum >> 2
    
    final = cumulative + len(temp_storage)
    return final

auxiliary_data = tuple(z * 2 for z in filtered_sequence if z < 20)
dropped_elements = [x for x in auxiliary_data if x % 4 == 0]

# Key execution point
final_capacity = calculate_system_capacity(primary_units)

# Irrelevant tracking variable
status_summary = {"codes": diagnostic_codes, "flags": status_flags, "active": len(overlap_diagnostics)}

print(f"Result: {final_capacity}")