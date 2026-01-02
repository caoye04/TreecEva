from collections import defaultdict, Counter

# Simulate manufacturing line data with quality checks and throughput tracking
def analyze_production_efficiency(shift_data):
    item_counts = Counter()
    defect_log = defaultdict(list)
    total_items = 0
    total_defects = 0
    shift_averages = []

    for shift, records in shift_data.items():
        shift_output = 0
        shift_defects = 0
        temp_buffer = []

        for record in records:
            item_type = record['type']
            is_defective = record['defect']
            item_counts[item_type] += 1
            shift_output += 1
            total_items += 1

            if is_defective:
                defect_log[item_type].append(shift)
                shift_defects += 1
                total_defects += 1
                temp_buffer.append(item_type)

        # Irrelevant aggregation: average defect rate per shift (not used later)
        shift_rate = shift_defects / shift_output if shift_output > 0 else 0
        shift_averages.append(shift_rate)

        # Distractor calculation: peak buffer usage (never accessed again)
        peak_buffer = len(temp_buffer) if temp_buffer else 0

    # Real computation path begins
    base_output = sum(item_counts.values())
    adjustment_factor = 1.0

    # Conditional logic affecting final output
    if total_defects > 5:
        adjustment_factor -= 0.1
    if len(defect_log) > 2:
        adjustment_factor -= 0.05

    total_output = base_output * adjustment_factor

    # Multiple capacity definitions with red herring
    nominal_capacity = 95
    theoretical_max = 100
    max_capacity = theoretical_max * 0.9  # Actual constraint

    # Key statement - target of the question
    efficiency_score = total_output / max_capacity if max_capacity > 0 else 0

    # Additional irrelevant computations to increase cognitive load
    quality_ratio = (total_items - total_defects) / total_items if total_items > 0 else 0
    aggregated_stats = dict(item_counts)
    final_report = {"efficiency": efficiency_score, "quality": quality_ratio}

    # Print required result
    print(f"Result: {efficiency_score}")
    return efficiency_score

# Input data
shift_data = {
    'morning': [
        {'type': 'gear', 'defect': False},
        {'type': 'gear', 'defect': False},
        {'type': 'spring', 'defect': True},
        {'type': 'motor', 'defect': False},
        {'type': 'spring', 'defect': False},
        {'type': 'gear', 'defect': False},
        {'type': 'motor', 'defect': True}
    ],
    'evening': [
        {'type': 'spring', 'defect': False},
        {'type': 'gear', 'defect': False},
        {'type': 'motor', 'defect': False},
        {'type': 'gear', 'defect': True},
        {'type': 'spring', 'defect': False},
        {'type': 'motor', 'defect': False}
    ],
    'night': [
        {'type': 'gear', 'defect': False},
        {'type': 'spring', 'defect': True},
        {'type': 'motor', 'defect': False},
        {'type': 'gear', 'defect': False}
    ]
}

analyze_production_efficiency(shift_data)