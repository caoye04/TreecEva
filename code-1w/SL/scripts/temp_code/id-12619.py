def temperature_diagnostic(temp, pressures):
    baseline = 98.6
    normal_pressure_range = set(range(70, 91))
    elevated = temp > baseline + 1.5
    
    # Irrelevant calculation (minor distraction)
    compensation_factor = 1.0 if len(pressures) > 5 else 0.9
    
    # Core logic
    pressure_set = set(pressures)
    stable_pressures = pressure_set.intersection(normal_pressure_range)
    instability_score = len(pressure_set) - len(stable_pressures)
    
    # Conditional expression determining result
    category = (lambda x: 1 if x == 0 else 2 if x == 1 else 3)(instability_score)
    
    # Final diagnostic result
    result = int(temp - baseline) * category
    return result

# Input data
pressure_readings = [75, 80, 95, 100, 72]

# Execution
result = temperature_diagnostic(98.6, pressure_readings)
print(f"Result: {result}")