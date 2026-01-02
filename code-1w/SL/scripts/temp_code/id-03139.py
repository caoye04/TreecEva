import math

# Simulated sensor fusion system for environmental monitoring
def collect_readings():
    # Real data sources
    temp_raw = [23.4, 24.1, 22.9, 25.3, 26.0]
    hum_raw = [55.2, 57.8, 53.1, 60.4, 62.0]
    press_raw = [1013, 1010, 1015, 1008, 1005]

    # Irrelevant decoy sensor (distractor)
    dummy_sensor = [0.0] * 5  # Unused in final calculation

    readings = []
    for i in range(len(temp_raw)):
        # Composite index with physical significance
        phys_index = temp_raw[i] * (hum_raw[i] / 100) * 0.3 + (1013 - press_raw[i]) * 0.1
        readings.append((temp_raw[i], hum_raw[i], press_raw[i], phys_index))
    
    return readings

# Decoy function – looks important but unused
def legacy_calibrate(data):
    adjusted = []
    for t, h, p, idx in data:
        adjusted.append((t*0.98, h*1.02, p*1.001, idx))
    return adjusted

# Signal preprocessing with red herrings
def preprocess(readings):
    normalized = []
    indices = []
    
    # Real transformation
    base_temp = sum(r[0] for r in readings) / len(readings)
    temp_deviation = [r[0] - base_temp for r in readings]
    
    # Distractor: complex but unused humidity clustering
    high_hum = {i for i, r in enumerate(readings) if r[1] > 58}
    mid_hum = {i for i, r in enumerate(readings) if 54 <= r[1] <= 58}
    low_hum = {i for i, r in enumerate(readings) if r[1] < 54}
    humidity_clusters = [high_hum, mid_hum, low_hum]
    
    # Another decoy: pressure trend analysis
    press_trend = []
    for i in range(1, len(readings)):
        press_trend.append(readings[i][2] - readings[i-1][2])
    avg_trend = sum(press_trend) / len(press_trend) if press_trend else 0
    
    # Actual relevant processing
    for i, r in enumerate(readings):
        norm_temp = r[0] / 50.0
        norm_hum = r[1] / 100.0
        scaled_pressure = (r[2] - 980) / 50
        stability_factor = math.cos(math.radians(abs(temp_deviation[i])))
        signal_power = (norm_temp * 0.4 + norm_hum * 0.3 + stability_factor * 0.2 + r[3] * 0.1)
        
        # Only this tuple structure is used downstream
        normalized.append((signal_power, stability_factor, i))
        indices.append(i)
    
    # Dead code path: never accessed
    if len(normalized) > 10:
        fallback = sum(p[0] for p in normalized) / len(normalized)
    else:
        fallback = -1.0  # Never used

    # Return includes irrelevant components to distract
    return {
        'processed': normalized,
        'indices_used': set(indices),
        'fallback_value': fallback,
        'decoy_cluster_info': humidity_clusters,
        'trend_analysis': avg_trend
    }

# Core analysis with conditional logic and bit manipulation distraction
def analyze_signal(data_packet):
    processed = data_packet['processed']
    total_power = 0.0
    phase_flags = 0
    
    # Real accumulation
    for power_val, stability, orig_idx in processed:
        if stability > 0.85:
            total_power += power_val * 1.2
        elif stability > 0.7:
            total_power += power_val * 1.0
        else:
            total_power += power_val * 0.8
        
        # Bit manipulation red herring (phase simulation)
        flag_bit = (orig_idx ^ 7) & 3
        phase_flags |= (flag_bit << (orig_idx * 2))
    
    # Conditional expression that depends on loop result
    adjustment_factor = 1.15 if total_power < 2.0 else (1.05 if total_power < 2.3 else 0.95)
    
    # Final diagnostic using only total_power and adjustment
    final_diagnostic = round(total_power * adjustment_factor * 1000)
    
    # More decoys below
    validation_checksum = 0
    for i, p in enumerate(processed):
        validation_checksum ^= int(p[0] * 100) & 0xFF
    
    # Unused complex structure
    diagnostics_report = {
        'raw_checksum': validation_checksum,
        'phase_state': phase_flags,
        'anomaly_bits': phase_flags & 0xFFFF,
        'meta': {
            'version': '2.1',
            'calibrated': False,
            'method': 'adaptive'
        }
    }
    
    # This print is irrelevant but looks important
    print(f"System check: {validation_checksum:02X}, Phase: {phase_flags & 0xFFFF:04X}")
    
    return final_diagnostic

# Orchestration with misleading setup
if __name__ == "__main__":
    # Collect real sensor data
    raw_data = collect_readings()
    
    # Apply preprocessing (contains distractors)
    processed_data = preprocess(raw_data)
    
    # DECOY: attempt to use legacy calibration (but doesn't affect anything)
    calibrated_data = legacy_calibrate(raw_data)  # Result ignored
    
    # Key execution point
    final_diagnostic = analyze_signal(processed_data)
    
    # Print required output format
    print(f"Result: {final_diagnostic}")