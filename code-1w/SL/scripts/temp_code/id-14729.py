def calculate_agricultural_yield():
    # Simulate a multi-step agricultural productivity calculation
    base_rates = [0.85, 0.92, 0.78, 0.96, 0.88]
    weather_impact = {'drought': 0.6, 'normal': 1.0, 'rainy': 1.1}
    soil_quality = {'clay': 0.8, 'loam': 1.2, 'sand': 0.7}
    
    crop_data = [
        ('wheat', 'loam', 'normal', 250),
        ('corn', 'clay', 'drought', 300),
        ('soy', 'loam', 'rainy', 200),
        ('barley', 'sand', 'normal', 180)
    ]
    
    total_input = 0
    total_potential = 0
    temp_buffer = []
    scaling_factor = 1.0
    
    # Irrelevant transformation (distraction)
    for i in range(len(base_rates)):
        scaled = base_rates[i] * 1.05
        temp_buffer.append(round(scaled, 3))
    
    # Primary logic with nested structure
    cumulative_multiplier = 1.0
    for idx, (crop, soil, climate, area) in enumerate(crop_data):
        input_energy = area * 10  # per hectare assumption
        total_input += input_energy
        
        # Real computation path
        base = base_rates[idx % len(base_rates)]
        weather_mod = weather_impact[climate]
        soil_mod = soil_quality[soil]
        
        if soil == 'loam' and climate != 'drought':
            base *= 1.15  # fertility boost
        
        adjusted_rate = base * weather_mod * soil_mod
        total_potential += adjusted_rate * area
        
        # Distractor: tracking unused stats
        if climate == 'rainy':
            scaling_factor *= 0.95
        
        # Nested conditional with partial relevance
        if area > 200:
            for j, rate in enumerate(base_rates):
                if j % 2 == 0:
                    cumulative_multiplier *= (rate + 0.1) / 1.0
    
    # Secondary distraction: unused data aggregation
    zipped = list(zip(base_rates, temp_buffer))
    variance_drift = 0.0
    for orig, mod in zipped:
        variance_drift += (mod - orig) ** 2
    
    # Key computational chain
    gross_output = total_potential * 0.93
    loss_factor = 0.07 * len(crop_data)
    final_output = gross_output * (1 - loss_factor)
    
    efficiency_factor = 0.88
    net_yield = final_output * efficiency_factor
    
    # Red herring computation
    phantom_yield = sum(temp_buffer) * scaling_factor * variance_drift
    
    print(f"Target result: {net_yield}")
    return net_yield

result = calculate_agricultural_yield()