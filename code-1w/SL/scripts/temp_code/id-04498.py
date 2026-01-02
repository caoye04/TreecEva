def analyze_growth_factors(data_str):
    factors = {}
    entries = data_str.split(',')
    temp_sum = 0
    moisture_count = 0

    for entry in entries:
        key, value = entry.strip().split(':')
        val = float(value)
        if key == 'temperature':
            factors['temp'] = val * 0.8 + 2
            temp_sum += val
        elif key == 'moisture':
            factors['wetness'] = max(val, 10)
            moisture_count += 1
        elif key == 'ph_level':
            factors['acidity'] = abs(val - 7.0)

    # Distractor computation: irrelevant average
    fake_avg = temp_sum / (moisture_count + 1) if moisture_count else 0
    dummy_result = fake_avg * 0.1

    return factors


def evaluate_stress_conditions(factors):
    stress_index = 0
    warnings = []

    if 'temp' in factors and factors['temp'] > 35:
        stress_index += factors['temp'] * 0.3
        warnings.append('high_temp')
    if 'wetness' in factors and factors['wetness'] < 25:
        stress_index += 5
        warnings.append('low_moisture')
    if 'acidity' in factors and factors['acidity'] > 2.5:
        stress_index += 4
        warnings.append('improper_ph')

    # Dead code path - never accessed in normal flow
    if len(warnings) == 0:
        stress_index = min(stress_index, 1)  # unreachable due to prior increments

    return stress_index


def calculate_harvest_potential(climate_data):
    parsed = analyze_growth_factors(climate_data)
    index = evaluate_stress_conditions(parsed)

    base_yield = 100
    loss_rate = index * 2.5
    projected_loss = base_yield * (loss_rate / 100)

    # Secondary adjustment based on wetness presence
    bonus = 0
    if 'wetness' in parsed:
        if parsed['wetness'] > 40:
            bonus += 8
        elif parsed['wetness'] >= 25:
            bonus += 3

    # Irrelevant intermediate calculation (distractor)
    hypothetical_max = base_yield * 1.5
    decay_factor = hypothetical_max * 0.02

    final_yield = base_yield - projected_loss + bonus

    # Additional noise variables
    efficiency_ratio = (final_yield / base_yield) if base_yield else 0
    normalized = round(efficiency_ratio * 100, 2)

    return final_yield

# Main execution
climate_input = "temperature:40.0,moisture:30.0,ph_level:4.5"
result_dict = {}
interim_values = []

for i in range(1):  # Simulated single-run loop (adds nesting)
    raw = climate_input
    clean_data = raw.strip()
    temp_store = len(clean_data)
    interim_values.append(temp_store)

    final_yield = calculate_harvest_potential(climate_input)
    result_dict['yield'] = final_yield

    # Print required output
    print(f"Result: {final_yield}")