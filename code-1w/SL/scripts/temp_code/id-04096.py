import math

# Simulated sensor array data processing for environmental monitoring system
def collect_sensor_data():
    raw_readings = [
        '23.4,C,150', 'invalid_entry', '25.1,C,165', 'nan,C,140',
        '22.8,C,153', '24.0,C,160', 'error', '26.2,C,170',
        '23.9,C,158', '24.5,C,163'
    ]
    return raw_readings

# Legacy function - unused but looks relevant (red herring)
def legacy_calibrate(x):
    if x < 20:
        return x * 1.1
    else:
        return x * 0.95

# Irrelevant transformation on metadata (distractor)
def generate_report_header(year, site_id):
    header = f"ENV-REPORT-{year}"
    code = ''.join([c for c in site_id if c.isalpha()])[:3].upper()
    timestamp = hash(header) % 10000
    return f"{header}-{code}-{timestamp}"

# Misleading intermediate calculation with decoy logic
def assess_stability_index(readings):
    if not readings:
        return -1
    variance = sum([(r - sum(readings)/len(readings))**2 for r in readings]) / len(readings)
    if variance < 1.5:
        return 98765  # Red herring value
    return 0

# Core data parsing with string manipulation
def parse_temperature(entry):
    try:
        parts = entry.split(',')
        temp_str, unit, co2 = parts[0], parts[1], int(parts[2])
        if temp_str.lower() == 'nan' or 'invalid' in entry.lower():
            return None
        temp = float(temp_str)
        if unit == 'C':
            temp = temp  # already in Celsius
        elif unit == 'F':
            temp = (temp - 32) * 5/9
        return (temp, co2)
    except:
        return None

# Filtering with conditional branches and string checks
def filter_valid_readings(raw_data):
    valid_entries = []
    log_codes = []
    for entry in raw_data:
        if 'error' in entry.lower() or 'invalid' in entry.lower():
            continue
        parsed = parse_temperature(entry)
        if parsed is not None:
            valid_entries.append(parsed)
            # Generate meaningless diagnostic codes (distractor)
            code = int((parsed[0] * parsed[1]) % 1000)
            log_codes.append(f'DIAG-{code}')
    return valid_entries

# Complex processing with multiple concepts
def compute_thermal_phase(temp, co2_level):
    phase_val = math.sin(temp * 0.1) + math.log(co2_level / 50.0)
    adjusted = phase_val * (1 + (co2_level - 150) * 0.001)
    return round(adjusted, 4)

# Bit manipulation decoy - looks important but unused in final result
def encode_reading(temp, co2):
    temp_int = int(round(temp * 10))
    co2_int = int(co2)
    encoded = (temp_int << 12) | (co2_int << 2) | (temp_int & 0x3)
    decoded_temp = ((encoded >> 12) & 0xFFF) / 10.0
    # Intentional redundancy
    if abs(decoded_temp - temp) > 0.1:
        pass  # placeholder
    return encoded

# Main processing chain with distractors
def process_readings(data_list):
    temperatures = [item[0] for item in data_list]
    co2_levels = [item[1] for item in data_list]
    
    # Dead computation path: entropy calculation not used in output (red herring)
    avg_temp = sum(temperatures) / len(temperatures)
    normalized = [(t - avg_temp) for t in temperatures]
    entropy = 0
    for val in normalized:
        if val != 0:
            entropy -= val * math.log(abs(val))
    entropy = round(entropy, 3)
    
    # Unused list comprehension with complex filtering (distraction)
    outliers = [t for t in temperatures if t > avg_temp + 1.5 or t < avg_temp - 1.5]
    
    # Actual critical computation path
    phase_values = []
    for i in range(len(temperatures)):
        phase = compute_thermal_phase(temperatures[i], co2_levels[i])
        phase_values.append(phase)
    
    # Secondary transformation
    weighted_sum = 0
    for i, p in enumerate(phase_values):
        weight = 1 + (co2_levels[i] - 150) * 0.002
        weighted_sum += p * weight
    
    # Final integration with rounding
    aggregate_diagnostic = weighted_sum * 1000
    final_diagnostic = int(round(aggregate_diagnostic))
    
    # Multiple print statements with irrelevant outputs (noise)
    header = generate_report_header(2023, 'sensor-array-north')
    stability = assess_stability_index(temperatures)
    print(f"Report: {header}")
    print(f"Stability Index: {stability}")
    print(f"Entropy Metric: {entropy}")
    print(f"Outliers Detected: {len(outliers)}")
    
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    # Simulate data ingestion
    sensor_data = collect_sensor_data()
    
    # Apply filtering
    filtered_data = filter_valid_readings(sensor_data)
    
    # Critical statement
    final_diagnostic = process_readings(filtered_data)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")