import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.2, 20.9]
humidity_readings = [45, 50, 52, 60, 65, 70, 40, 55]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1005, 1014, 1016]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 1.002
CALIBRATION_FACTOR_B = 0.998
REFERENCE_VOLTAGE = 3.3
OFFSET_ADJ = -0.05

# Data transformation function with multiple responsibilities (complexity)
def transform_sensor_data(raw_temps, raw_humid, raw_press):
    transformed = []
    for i in range(len(raw_temps)):
        # Real processing step
        temp_c = raw_temps[i]
        temp_k = temp_c + 273.15
        humidity = raw_humid[i]
        rel_humid_ratio = humidity / 100.0
        pressure = raw_press[i]
        
        # Intermediate derived value (used later)
        saturation_vapor_pressure = 6.112 * math.exp((17.67 * temp_c) / (temp_c + 243.5))
        actual_vapor_pressure = rel_humid_ratio * saturation_vapor_pressure
        dew_point = (243.5 * math.log(actual_vapor_pressure / 6.112)) / (17.67 - math.log(actual_vapor_pressure / 6.112))
        
        # Compute heat index approximation (only valid above certain temp)
        heat_index = temp_c
        if temp_c > 26:
            heat_index = (-8.784695 + 1.61139411*temp_c + 2.338549 * humidity - 0.14611605*temp_c*humidity 
                        - 0.012308094*temp_c*temp_c - 0.016425 * humidity*humidity 
                        + 0.002211732*temp_c*temp_c*humidity + 0.00072546 * temp_c*humidity*humidity 
                        - 0.000003582 * temp_c*temp_c*humidity*humidity)

        # Pack into dictionary structure (relevant)
        entry = {
            'station_id': f'ST{i+1}',
            'temp_c': round(temp_c, 2),
            'temp_k': round(temp_k, 2),
            'humidity_pct': humidity,
            'pressure_hpa': pressure,
            'dew_point_c': round(dew_point, 2),
            'heat_index_c': round(heat_index, 2),
            'quality_flag': True
        }
        transformed.append(entry)
        
        # Dead code path - never accessed due to loop logic (red herring)
        if False:
            backup_entry = {
                'raw_seq': i,
                'calibrated_temp': temp_c * CALIBRATION_FACTOR_A + OFFSET_ADJ,
                'stable_conditions': pressure > 1010 and humidity < 60
            }
            transformed.append(backup_entry)
    
    return transformed

# Unused auxiliary function (distractor)
def validate_checksum(data_block):
    """Unused validation routine - misleading but plausible."""
    checksum = 0
    for char in str(data_block):
        checksum ^= ord(char)
    return checksum % 256 == 0

# Another decoy function that looks important but isn't called
def generate_report_snapshot(metrics, version='v1'):
    """Generates a diagnostic report (unused)."""
    report_id = f"RPT-{hash(str(metrics)) % 10000}"
    return {"report_id": report_id, "version": version, "anomalies": 0}

# Threshold configuration map (critical for final decision)
def build_threshold_map():
    # Complex dictionary construction with irrelevant fields
    config = {
        'temp_c': {
            'warning_low': 15.0,
            'warning_high': 26.0,
            'critical_low': 10.0,
            'critical_high': 28.0,
            'units': 'Celsius',
            'tolerance_band': 0.5
        },
        'humidity_pct': {
            'warning_low': 30,
            'warning_high': 70,
            'critical_low': 20,
            'critical_high': 80,
            'units': 'percent',
            'response_delay': 2
        },
        'pressure_hpa': {
            'baseline': 1013.25,
            'variation_limit': 15,
            'altitude_comp': True,
            'adjustment_factor': 0.12
        },
        # Extra unused keys (distractors)
        'metadata': {
            'created_by': 'sysadmin',
            'last_updated': '2023-10-05',
            'schema_version': '2.1'
        }
    }
    return config

# Data filtering with early termination (real logic)
def filter_anomalous_entries(data_list):
    filtered = []
    anomaly_count = 0
    for record in data_list:
        temp_ok = 15 <= record['temp_c'] <= 28
        humid_ok = 20 <= record['humidity_pct'] <= 80
        press_ok = abs(record['pressure_hpa'] - 1013.25) <= 15
        
        if temp_ok and humid_ok and press_ok:
            filtered.append(record)
        else:
            record['quality_flag'] = False
            anomaly_count += 1
            # Early skip - not actually used but shows complex flow
            continue
    
    # Attach summary stats (some used later)
    summary = {
        'valid_count': len(filtered),
        'anomaly_count': anomaly_count,
        'total_processed': len(data_list),
        'retention_rate': len(filtered) / len(data_list) if data_list else 0
    }
    
    return filtered, summary

# Core analysis logic that determines final output
def analyze_readings(clean_data, thresholds):
    score = 0
    max_score = len(clean_data) * 3  # One point per metric per station
    
    for entry in clean_data:
        temp = entry['temp_c']
        humid = entry['humidity_pct']
        
        # Scoring based on threshold proximity
        if temp < thresholds['temp_c']['warning_low']:
            points = 0
        elif temp <= thresholds['temp_c']['warning_high']:
            points = 1
        elif temp <= thresholds['temp_c']['critical_high']:
            points = 2
        else:
            points = 3
        score += points
        
        if humid < thresholds['humidity_pct']['warning_low']:
            points = 0
        elif humid <= thresholds['humidity_pct']['warning_high']:
            points = 1
        elif humid <= thresholds['humidity_pct']['critical_high']:
            points = 2
        else:
            points = 3
        score += points
        
        # Pressure contributes only if outside normal band (subtle logic)
        base_pressure = thresholds['pressure_hpa']['baseline']
        variation = abs(entry['pressure_hpa'] - base_pressure)
        limit = thresholds['pressure_hpa']['variation_limit']
        if variation > limit * 0.8:  # More sensitive threshold
            score -= 1
    
    # Final diagnostic computed from relative performance
    ideal = max_score if max_score > 0 else 1
    efficiency_ratio = score / ideal
    diagnostic_code = int(1000 + (efficiency_ratio * 500))  # Maps to 1000-1500 scale
    
    # Secondary adjustment based on data size (real effect)
    if len(clean_data) >= 5:
        diagnostic_code += 17  # Arbitrary stabilization bonus
    
    return diagnostic_code

# Auxiliary counting function (partially relevant)
def count_extreme_events(raw_temps):
    freeze_events = sum(1 for t in raw_temps if t < 0)
    heatwaves = sum(1 for t in raw_temps if t > 35)
    return {'frozen': freeze_events, 'hot': heatwaves}

# Main execution workflow
if __name__ == '__main__':
    # Step 1: Transform raw sensor inputs into structured format
    processed_data = transform_sensor_data(
        temperature_readings, 
        humidity_readings, 
        pressure_readings
    )
    
    # Step 2: Filter out clearly anomalous records
    filtered_data, stats = filter_anomalous_entries(processed_data)
    
    # Step 3: Build threshold configuration (must happen before analysis)
    threshold_map = build_threshold_map()
    
    # Step 4: Perform final diagnostic analysis
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Incidental computation (distractor - looks important)
    event_tally = count_extreme_events(temperature_readings)
    system_health = f"HEALTHY" if final_diagnostic > 1200 else "WARNING"
    
    # Output the required result (per specification)
    print(f"Result: {final_diagnostic}")