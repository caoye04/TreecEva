import itertools

def analyze_sensor_noise():
    # Irrelevant function: simulates sensor noise but unused in final computation
    readings = [0.1, 0.3, 0.2, 0.4]
    noise_floor = sum([r ** 2 for r in readings])
    adjusted = list(map(lambda x: x + noise_floor * 0.01, readings))
    return adjusted

def generate_combinations(elements):
    # Distractor: generates combinations but not used in main logic
    return list(itertools.combinations(elements, 2))

def decode_transmission(signal):
    # Decoy function with bit manipulation red herring
    if not signal:
        return 0
    masked = signal & 0xFF
    rotated = ((masked << 3) | (masked >> 5)) & 0xFF
    return rotated ^ 0xAA

def preprocess_farm_data(raw_records):
    # Relevant preprocessing with embedded distractors
    filtered = []
    total_records = len(raw_records)
    null_count = 0

    for record in raw_records:
        if record.get('status') != 'active':
            null_count += 1
            continue
        if 'moisture' not in record or 'ph' not in record:
            null_count += 1
            continue
        # Only this branch contributes to final result
        moisture = record['moisture']
        ph_level = record['ph']
        if moisture > 30 and 5.5 <= ph_level <= 7.0:
            # Transform to normalized yield index
            index = (moisture * 0.7) + (abs(ph_level - 6.25) * -10) + 25
            filtered.append(index)
    
    # Dead code path - never executed due to logic above
    if null_count > 100:
        fallback = [0] * 5
        return fallback

    return filtered

def calculate_harvest_efficiency(yield_indices):
    # Core calculation with misleading intermediate steps
    if not yield_indices:
        return 0.0
    
    # Real computation begins
    base_total = sum(yield_indices)
    count = len(yield_indices)
    
    # Distractor variables
    peak = max(yield_indices)
    volatility = peak - min(yield_indices)
    adjustment_factor = 1.0
    
    # Fake adaptive logic that doesn't change anything
    if volatility > 20:
        adjustment_factor = 0.95
    elif volatility < 5:
        adjustment_factor = 1.05
    else:
        adjustment_factor = 1.0  # Neutral
    
    # Actual formula used
    efficiency_score = (base_total / count) * adjustment_factor
    
    # Extra transformation not affecting result
    normalized_score = round(efficiency_score, 3)
    final_rating = int(normalized_score * 10) / 10.0
    
    # This is the true answer variable
    final_yield = int(final_rating * 100) / 100.0
    return final_yield

# Simulated IoT farm sensor data (mixed quality)
data_source = [
    {'sensor_id': 'A1', 'moisture': 45, 'ph': 6.8, 'status': 'active'},
    {'sensor_id': 'A2', 'moisture': 25, 'ph': 6.5, 'status': 'inactive'},  # filtered out
    {'sensor_id': 'A3', 'moisture': 50, 'ph': 6.0, 'status': 'active'},
    {'sensor_id': 'A4', 'moisture': 35, 'ph': 7.2, 'status': 'active'},  # pH out of range
    {'sensor_id': 'A5', 'moisture': 60, 'ph': 6.3, 'status': 'active'},
    {'sensor_id': 'A6', 'moisture': 20, 'ph': 5.8, 'status': 'active'},  # moisture too low
    {'sensor_id': 'A7', 'moisture': 55, 'ph': 6.1, 'status': 'active'},
    {'sensor_id': 'A8', 'moisture': 40, 'ph': 6.9, 'status': 'active'},
]

# Irrelevant combinatorics on sensor IDs
dummy_ids = [d['sensor_id'] for d in data_source]
_ = generate_combinations(dummy_ids)

# Noise simulation not connected to pipeline
_ = analyze_sensor_noise()

# Main execution flow
processed_data = preprocess_farm_data(data_source)
final_yield = calculate_harvest_efficiency(processed_data)
print(f"Result: {final_yield}")