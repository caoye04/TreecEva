def analyze_sensor_data():
    temperatures = [23.5, 24.1, 22.8, 25.6, 26.3, 24.9, 23.0]
    humidity_readings = [45, 47, 50, 44, 48, 51, 46]
    
    # Irrelevant transformation (distractor)
    normalized_humidity = [round((h - min(humidity_readings)) / (max(humidity_readings) - min(humidity_readings)), 3) for h in humidity_readings]
    
    base_value = 0
    transient_sum = 0
    spike_count = 0
    
    # Primary logic with nested conditions and tracking
    for i, temp in enumerate(temperatures):
        if temp > 24.0:
            base_value += temp * 1.1
            transient_sum += temp
            if i > 0 and temperatures[i-1] < 23.5:
                spike_count += 1
        else:
            base_value += temp * 0.9
    
    # Secondary processing with zip (required feature)
    adjustment_factors = []
    for t, h in zip(temperatures, humidity_readings):
        factor = 1.0 + (h - 45) * 0.005
        adjusted_t = t * factor
        adjustment_factors.append(round(adjusted_t, 3))
    
    # Misleading statistical computation (dead-end)
    avg_adjusted = sum(adjustment_factors) / len(adjustment_factors)
    variance_proxy = sum((x - avg_adjusted) ** 2 for x in adjustment_factors)
    stability_score = 100 - variance_proxy  # Unused variable
    
    # Core calculation path
    total_spikes = spike_count + 1
    efficiency_factor = (10 - abs(47.5 - sum(humidity_readings)/len(humidity_readings))) / 10
    
    # Key assignment point
    thermal_capacity = base_value * efficiency_factor
    
    # Final red herring: complex but irrelevant aggregation
    composite_index = 0
    for idx, (t, h) in enumerate(zip(adjustment_factors, normalized_humidity)):
        if idx % 2 == 0:
            composite_index += t * (1 - h)
        else:
            composite_index -= t * h
    
    print(f"Result: {thermal_capacity}")

analyze_sensor_data()