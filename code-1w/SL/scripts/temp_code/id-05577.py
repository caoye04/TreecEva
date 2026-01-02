def analyze_condition(x, y):
    if x < 0 or y > 100:
        return False
    return True

# Simulate environmental sensor array (distractor: not all values are used)
def generate_diagnostics(temp_list, press_list):
    diagnostics = []
    for t, p in zip(temp_list, press_list):
        status = 'OK' if t * 0.3 + p * 0.05 < 40 else 'ALERT'
        diagnostics.append(status)
    return diagnostics

# Core calculation with list comprehension and filtering
def calculate_optimal_yield(temps, pressures):
    # Normalize inputs using a scaling factor (relevant)
    scaled_temps = [t * 0.85 for t in temps if t >= 20]
    scaled_pressures = [p * 1.15 for p in pressures if p >= 10]

    # Misleading intermediate: average computation that isn't directly used
    avg_temp = sum(scaled_temps) / len(scaled_temps) if scaled_temps else 0
    avg_pressure = sum(scaled_pressures) / len(scaled_pressures) if scaled_pressures else 0

    # Apply conditional adjustment based on joint thresholds (key logic step)
    adjusted_values = []
    for i in range(min(len(scaled_temps), len(scaled_pressures))):
        temp_adj = scaled_temps[i] + (5 if scaled_pressures[i] > 15 else 0)
        if analyze_condition(scaled_temps[i], scaled_pressures[i]):
            adjusted_values.append(temp_adj * 1.2)

    # Final aggregation using min/max/average pattern
    if not adjusted_values:
        return 0
    
    max_val = max(adjusted_values)
    min_val = min(adjusted_values)
    mid_range = (max_val + min_val) / 2
    
    # Secondary adjustment based on length (subtle but relevant)
    length_factor = len(adjusted_values) * 0.9
    final_score = mid_range * length_factor
    
    # Dead code path - never executed due to data constraints (distractor)
    if avg_temp < 10:
        final_score *= 0.5  # This does not trigger

    return final_score

# Main execution block
if __name__ == '__main__':
    # Input datasets (realistic domain: industrial process monitoring)
    temperature_data = [25, 30, 15, 40, 35]
    pressure_data = [12, 18, 8, 20, 14]
    
    # Generate unused diagnostic logs (interference)
    logs = generate_diagnostics(temperature_data, pressure_data)
    
    # Key computation
    final_yield = calculate_optimal_yield(temperature_data, pressure_data)
    
    # Print result as required
    print(f"Target result: {final_yield}")