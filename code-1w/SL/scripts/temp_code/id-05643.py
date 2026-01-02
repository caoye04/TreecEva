def calculate_harvest_efficiency(output, stresses):
    # Normalize stress factors using logarithmic scaling
    normalized_stress = [max(0.1, min(1.0, abs(stress * 0.1))) for stress in stresses]
    
    # Simulate environmental interference (irrelevant to final result)
    temp_log = []
    for s in stresses:
        if s > 5:
            temp_log.append(s ** 0.5)
        else:
            temp_log.append(s + 0.1)
    
    # Core efficiency calculation (key logic)
    adjustment_factor = 1.0
    for ns in normalized_stress:
        adjustment_factor *= (1 - ns)
    
    # Apply adjustment to base output
    adjusted_output = output * adjustment_factor
    
    # Distractor: simulate redundant health check
    system_health = "OK"
    error_count = 0
    for val in temp_log:
        if val < 0:
            error_count += 1
            system_health = "ERROR"
    
    # Irrelevant string processing (uses string methods)
    report_id = "HARV-2023-final"
    report_id_upper = report_id.upper()
    report_checksum = len(report_id.replace("-", "")) * 11
    
    # Simulate historical averaging (unused)
    historical_data = [output * 0.92, output * 0.96, output * 0.89]
    avg_historical = sum(historical_data) / len(historical_data)
    
    # Final yield computed from current conditions only
    final_yield = int(round(adjusted_output))
    return final_yield

# Main execution context
base_output = 1500
stress_factors = [3, 7, 2, 9, 4]

# Dummy list processing with case conversion (distractor)
data_labels = ["sensor_A", "SENSOR_B", "Sensor_C"]
normalized_labels = [label.lower().replace("_", " ") for label in data_labels]

# Key computation
final_yield = calculate_harvest_efficiency(base_output, stress_factors)

# Output result as required
print(f"Target result: {final_yield}")