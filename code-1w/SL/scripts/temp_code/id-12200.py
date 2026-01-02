def analyze_temperatures(raw_readings):
    adjusted = [x - 273.15 for x in raw_readings if x >= 0]
    positives = [t for t in adjusted if t > 0]
    avg_temp = sum(positives) / len(positives) if positives else 0
    temp_buckets = {"cold": 0, "moderate": 0, "hot": 0}
    for t in adjusted:
        if t < 15:
            temp_buckets["cold"] += 1
        elif t < 30:
            temp_buckets["moderate"] += 1
        else:
            temp_buckets["hot"] += 1
    return avg_temp, temp_buckets


def calculate_humidity_score(humidity_list):
    # Irrelevant helper with dead logic path
    baseline = 50
    adjustments = []
    for h in humidity_list:
        if h < 30:
            adjustments.append(-5)
        elif h > 70:
            adjustments.append(3)
        else:
            adjustments.append(0)
    total_adjustment = sum(adjustments)
    fake_metric = total_adjustment * 0.1  # Unused distraction
    return baseline + total_adjustment


def calculate_final_score(data_packet):
    temperature_contribution = data_packet['temp_avg'] * 1.8
    humidity_contribution = data_packet['humidity_score'] * 0.8
    stability_bonus = 10 if data_packet['stable_conditions'] else 0
    
    # Misleading intermediate calculation
    volatility_penalty = 0
    if data_packet['temp_buckets']['hot'] > data_packet['temp_buckets']['cold']:
        volatility_penalty = 5
    
    # Actual scoring formula
    raw_score = temperature_contribution + humidity_contribution + stability_bonus
    final_score = int(raw_score - volatility_penalty)  # Final integer score
    
    # Dead code branch (never executed under current logic)
    if False and data_packet['temp_avg'] < 0:
        final_score = 0
        
    return final_score

# Simulated sensor data
sensor_log = [-273.15, 280, 295, 310, 270, 305]
humidity_samples = [45, 52, 78, 80, 60]

# Process temperature
avg_temperature, categorized = analyze_temperatures(sensor_log)

# Compute humidity score (partially irrelevant due to fixed weight)
h_score = calculate_humidity_score(humidity_samples)

# Assemble processed data packet
processed_data = {
    'temp_avg': avg_temperature,
    'temp_buckets': categorized,
    'humidity_score': h_score,
    'stable_conditions': len([x for x in humidity_samples if 40 <= x <= 60]) >= 3
}

# Critical execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")