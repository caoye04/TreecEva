def calculate_adjusted_efficiency(records):
    base_efficiency = 0
    penalty_adjustment = 0
    temp_sum = 0
    outlier_count = 0

    for record in records:
        clean_record = record.strip().lower()
        if 'error' in clean_record:
            outlier_count += 1
            continue
        try:
            value = float(clean_record)
            temp_sum += value ** 0.5
            base_efficiency += value
            if value > 100:
                penalty_adjustment += 1
        except ValueError:
            continue

    # Irrelevant tracking variables (distractor)
    average_temp = temp_sum / len(records) if records else 0
    debug_info = f"Processed {len(records)} entries with {outlier_count} errors"

    efficiency_ratio = base_efficiency / (penalty_adjustment + 1)
    fluctuation_factor = abs(base_efficiency - temp_sum) % 17

    # Secondary unrelated computation (distractor)
    checksum = 0
    for i, r in enumerate(records):
        if i % 3 == 0:
            checksum += len(r)

    final_score = int(efficiency_ratio - fluctuation_factor + penalty_adjustment)
    return final_score


data_buffer = [' 144 ', '225', 'error: timeout', '32.5', '169.0', 'invalid', '81', '100']
final_score = calculate_adjusted_efficiency(data_buffer)
print(f"Result: {final_score}")