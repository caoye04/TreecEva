from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for environmental monitoring system
def process_sensor_array(raw_readings):
    # Irrelevant preprocessing: normalize timestamps (distractor)
    base_time = raw_readings[0]['time']
    for reading in raw_readings:
        reading['offset'] = reading['time'] - base_time

    # Key transformation: extract and clean PM2.5 levels
    pm25_values = [r['pm25'] for r in raw_readings if 'pm25' in r]
    filtered_pm25 = [val for val in pm25_values if val > 0]  # Remove invalid readings

    # Dead code path: temperature correction (never used later)
    temp_data = [r['temp'] for r in raw_readings if 'temp' in r]
    if len(temp_data) > 5:
        avg_temp = sum(temp_data) / len(temp_data)
        corrected = list(map(lambda t: t * 1.02 if t < avg_temp else t * 0.98, temp_data))

    # Distractor: frequency analysis of sensor IDs (not used)
    id_counter = Counter(r['sensor_id'] for r in raw_readings)
    dominant_frequency = max(id_counter.values())

    # Actual relevant computation: statistical summary of PM2.5
    mean_pm25 = sum(filtered_pm25) / len(filtered_pm25)
    variance = sum((x - mean_pm25) ** 2 for x in filtered_pm25) / len(filtered_pm25)
    std_dev = math.sqrt(variance)

    # Composite metric calculation (partially relevant)
    stability_index = 1 / (std_dev + 0.1)
    exposure_risk = mean_pm25 * 1.5

    return {
        'raw_count': len(pm25_values),
        'valid_count': len(filtered_pm25),
        'mean': mean_pm25,
        'stability': stability_index,
        'risk': exposure_risk,
        'dof': len(filtered_pm25) - 1  # degrees of freedom
    }

# Secondary processor: atmospheric pressure adjustment (mostly irrelevant)
def adjust_pressure(readings):
    if not readings:
        return []
    
    pressures = [r.get('pressure', 1013.25) for r in readings]
    baseline = pressures[0]
    adjusted = []
    for p in pressures:
        if p > 1050:
            p = 1050
        elif p < 950:
            p = 950
        adjusted.append(p * (baseline / 1013.25))
    
    # This result is never used in final chain
    stats = {
        'min': min(adjusted),
        'max': max(adjusted),
        'range': max(adjusted) - min(adjusted)
    }
    
    return adjusted

# Core diagnostic aggregator - combines multiple sources but only uses specific fields
def aggregate_metrics(chains, diagnostics):
    # chains contains multiple processing results
    primary_chain = chains.get('particle_analysis')
    secondary_chain = chains.get('auxiliary')
    
    if not primary_chain:
        return -999
    
    # Extract key metrics (only these are actually used)
    valid_samples = primary_chain['valid_count']
    risk_score = primary_chain['risk']
    dof = primary_chain['dof']
    
    # Distractor: attempt to use secondary chain (but logic bypasses it)
    adjustment_factor = 1.0
    if secondary_chain and secondary_chain['status'] == 'calibrated':
        adjustment_factor = secondary_chain['factor']
    else:
        adjustment_factor = 0.85  # default
    
    # Complex conditional with misleading branches
    if valid_samples < 10:
        if dof < 5:
            base_diagnostic = risk_score * 0.3
        else:
            base_diagnostic = risk_score * 0.6
    elif valid_samples < 50:
        intermediate = risk_score * (0.7 + (dof * 0.01))
        # Red herring: transform through unused function
        def dummy_transform(x):
            return (x ** 2 + 1) / (x + 0.5)
        base_diagnostic = intermediate  # dummy_transform not applied
    else:
        base_diagnostic = risk_score * 0.9
    
    # Final adjustment using ignored pressure data (value overridden below)
    final_diagnostic = base_diagnostic * adjustment_factor
    
    # Late override based on hidden rule (key logic step)
    audit_log = diagnostics.get('audit', [])
    anomaly_count = sum(1 for log in audit_log if log['severity'] == 'critical')
    
    if anomaly_count > 2:
        final_diagnostic = final_diagnostic * 0.7
    elif anomaly_count == 0:
        final_diagnostic = final_diagnostic * 1.1
    # Otherwise unchanged
    
    # Additional distractor: bit manipulation on diagnostic code (not tied to output)
    code = diagnostics.get('diagnostic_code', 0x1A3B)
    masked = (code & 0xFF00) >> 8
    xor_key = 0x5A
    encrypted = masked ^ xor_key
    
    # Critical assignment point
    final_diagnostic = int(final_diagnostic)  # Round down to integer
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data setup
    sensor_data = [
        {'time': 1000, 'sensor_id': 'S1', 'pm25': 35.2, 'temp': 22.1, 'pressure': 1015.3},
        {'time': 1001, 'sensor_id': 'S2', 'pm25': 38.7, 'temp': 22.3, 'pressure': 1014.8},
        {'time': 1002, 'sensor_id': 'S1', 'pm25': 36.5, 'temp': 22.5, 'pressure': 1014.1},
        {'time': 1003, 'sensor_id': 'S3', 'pm25': 0,      'temp': 22.7, 'pressure': 1013.9},  # Invalid pm25
        {'time': 1004, 'sensor_id': 'S2', 'pm25': 40.1, 'temp': 22.8, 'pressure': 1013.2},
        {'time': 1005, 'sensor_id': 'S1', 'pm25': 37.3, 'temp': 23.0, 'pressure': 1012.7},
        {'time': 1006, 'sensor_id': 'S4', 'pm25': 39.8, 'temp': 23.2, 'pressure': 1012.1},
        {'time': 1007, 'sensor_id': 'S3', 'pm25': 36.9, 'temp': 23.4, 'pressure': 1011.8},
        {'time': 1008, 'sensor_id': 'S2', 'pm25': 41.2, 'temp': 23.6, 'pressure': 1011.2},
        {'time': 1009, 'sensor_id': 'S1', 'pm25': 38.0, 'temp': 23.8, 'pressure': 1010.9},
        {'time': 1010, 'sensor_id': 'S5', 'pm25': 42.5, 'temp': 24.0, 'pressure': 1010.3},
    ]

    # Pressure data processed but ultimately unused
    pressure_adjusted = adjust_pressure(sensor_data)
    
    # Primary analysis chain
    particle_results = process_sensor_array(sensor_data)
    
    # Auxiliary data structure with decoy information
    auxiliary_systems = {
        'status': 'uncalibrated',
        'factor': 1.2,
        'last_sync': 998,
        'readings': 12
    }
    
    # Audit trail with critical anomalies (affects final result)
    audit_trail = [
        {'timestamp': 1001, 'type': 'power', 'severity': 'minor'},
        {'timestamp': 1005, 'type': 'signal', 'severity': 'critical'},
        {'timestamp': 1008, 'type': 'sync', 'severity': 'critical'},
        {'timestamp': 1010, 'type': 'buffer', 'severity': 'critical'}  # Third critical
    ]
    
    # Build processing chain dictionary
    processing_chain = {
        'particle_analysis': particle_results,
        'auxiliary': auxiliary_systems
    }
    
    # Diagnostic metadata
    diagnostics = {
        'audit': audit_trail,
        'diagnostic_code': 0x1B2C,
        'version': '2.1.3'
    }
    
    # Key execution point
    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
    
    print(f"Result: {final_diagnostic}")