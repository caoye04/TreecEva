def analyze_crop_performance(data_entries):
    # Irrelevant preprocessing: normalize string labels
    normalized_labels = [label.strip().lower().replace('_', ' ') for label in data_entries['labels']]
    category_map = {label: idx for idx, label in enumerate(set(normalized_labels))}

    # Distractor: unused transformation
    scaled_values = [round(val * 1.07 + 3, 2) for val in data_entries['readings'] if val > 0]

    # Relevant computation begins
    raw_sequences = data_entries['sequences']
    processed_cycles = []
    for seq in raw_sequences:
        adjusted_seq = [x for x in seq if x % 2 == 1]  # Keep only odd numbers
        if len(adjusted_seq) > 0:
            avg_val = sum(adjusted_seq) / len(adjusted_seq)
            processed_cycles.append(avg_val)

    # Secondary distractor: dead code path (never executed due to filter above)
    temp_buffer = []
    for i in range(len(scaled_values)):
        if scaled_values[i] < 0:  # This will never happen
            temp_buffer.append(i)

    # Core logic: simulate growth cycles and area yield interaction
    growth_cycles = [int(max(cycle, 1)) for cycle in processed_cycles]
    base_area = len(data_entries['labels'])
    expansion_factor = len([v for v in data_entries['readings'] if v > 50])
    area_metrics = [base_area + expansion_factor]

    def calculate_harvest_efficiency(area_list, cycles):
        efficiency = 0
        for area in area_list:
            for cycle in cycles:
                # Complex but deterministic formula
                potential = (area ** 2) / (cycle + 1)
                decay = 0.1 * cycle
                efficiency += potential - decay
        return int(efficiency)

    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
    return final_yield

# Input data
input_data = {
    'labels': ['crop_A', 'crop_B', 'crop_C'],
    'readings': [45, 67, 89, 12, 53],
    'sequences': [
        [4, 7, 2, 9, 6],
        [1, 3, 5],
        [8, 10, 12]
    ]
}

result = analyze_crop_performance(input_data)
print(f"Target result: {result}")