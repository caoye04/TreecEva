def analyze_reactor_state(temperature, pressure, neutron_flux):
    safety_margin = 0.87
    critical_threshold = 950
    decay_factor = 0.91
    
    # Irrelevant diagnostic computations (distractors)
    status_code = 200 if temperature < 800 else 503
    recalibration_offset = (temperature * 0.03) % 7
    dummy_diagnostic = [recalibration_offset ** i for i in range(3)]
    system_health = sum(dummy_diagnostic) / len(dummy_diagnostic)

    # Real conditional branch affecting core logic
    if temperature > critical_threshold and pressure > 45:
        base_flux = neutron_flux * 0.65
    elif temperature < 700 and pressure < 30:
        base_flux = neutron_flux * 1.2
    else:
        base_flux = neutron_flux * 0.85

    # Unused alternate paths (dead code - red herring)
    def legacy_compensation(x):
        return x * 0.76 + 12  # Never called

    adjustment_log = []
    for i in range(5):
        adjusted = base_flux * (0.95 ** i)
        adjustment_log.append(adjusted)

    # Real efficiency loss calculation (used later)
    efficiency_loss = (temperature - 600) * 0.002 if temperature > 600 else 0.0

    # Fake aggregation (looks important but unused)
    avg_adjustment = sum(adjustment_log) / len(adjustment_log)
    max_deviation = max(adjustment_log) - min(adjustment_log)

    return base_flux, efficiency_loss


def adjust_thermal_rating(flux, loss):
    initial_rating = flux * 1.5
    corrected_rating = initial_rating * (1 - loss)
    
    # Distractor: complex-looking but irrelevant bit manipulation
    magic_mask = 0b101010
    obfuscation_key = (hash(str(corrected_rating)) ^ magic_mask) & 0xFFFF
    scrambled = obfuscation_key ^ int(corrected_rating % 100)

    # Conditional expression (required language feature)
    final_rating = corrected_rating if corrected_rating > 800 else (800 + (corrected_rating / 100))
    
    # Another decoy computation
    audit_trace = f"THERMAL_ADJUST_ID:{scrambled:04X}"
    
    return final_rating

# Simulated sensor inputs (real data)
temp_sensor = 860
pressure_sensor = 48
flux_sensor = 720

# Primary data processing chain
base_flux, efficiency_loss = analyze_reactor_state(temp_sensor, pressure_sensor, flux_sensor)

# Key statement - target of the question
thermal_output = adjust_thermal_rating(base_flux, efficiency_loss)

# Irrelevant post-processing (distractor)
diagnostic_summary = {"readings": [temp_sensor, pressure_sensor, flux_sensor],
                     "flags": ["NORMAL", "MONITOR"]}
summary_hash = hash(tuple(diagnostic_summary["readings"]))

# Final output (must print result)
print(f"Result: {thermal_output}")