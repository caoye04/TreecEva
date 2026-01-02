def calculate_engine_state(rpm, load, coolant_temp):
    base_pressure = 101.325
    dynamic_load = load * 1.23
    temperature_factor = 0.87 if coolant_temp < 90 else 1.15

    # Simulate intake phase adjustments
    if rpm < 2000:
        adjustment_curve = [0.9, 1.0, 1.05, 1.1][int(load // 25)]
        adjusted_base = base_pressure * adjustment_curve
    elif rpm < 4000:
        adjusted_base = base_pressure * (1.1 + (rpm - 2000) / 10000)
    else:
        adjusted_base = base_pressure * 1.3

    # Compression stage logic
    compression_ratio = 8 + (load / 10)
    knock_detected = (rpm > 3500) and (coolant_temp > 100)

    # Red herring: irrelevant fuel calculations
    fuel_map = {i: round(0.05 * i ** 1.1, 3) for i in range(1, 11)}
    target_afr = fuel_map.get(int(load // 10), 14.7)
    ignition_timing = 10 if rpm < 3000 else 8  # Unused variable

    # Emission scrubber status (dead code path)
    if coolant_temp > 110:
        scrubber_status = 'active'
        safety_margin = 0.95
    else:
        scrubber_status = 'standby'
        buffer_zone = 'nominal'

    # Final pressure synthesis
    final_pressure = adjusted_base + (temperature_factor * compression_ratio)

    # Diagnostic print (not affecting result)
    diagnostics = {
        'rpm': rpm,
        'pressure': final_pressure,
        'knock': knock_detected
    }

    # Irrelevant set operations for distraction
    active_sensors = {'temp', 'rpm', 'load'}
    failed_sensors = set()
    available_sensors = active_sensors - failed_sensors
    sensor_count = len(available_sensors)  # Not used

    # Extra slicing on diagnostic log (distraction)
    log_buffer = list(diagnostics.values())
    recent_entries = log_buffer[-2:]  # Unused

    return final_pressure

# Main execution
engine_rpm = 2400
engine_load = 60
coolant_temperature = 95

result = calculate_engine_state(engine_rpm, engine_load, coolant_temperature)
final_pressure = result
print(f"Result: {final_pressure}")