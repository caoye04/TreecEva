def analyze_readings(sensor_readings):
    filtered = [x for x in sensor_readings if x > 20 and x < 80]
    offset = 5
    adjusted = [x + offset for x in filtered]
    squared_devs = [(x - 50) ** 2 for x in adjusted]
    avg_sq_dev = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    return avg_sq_dev


def preprocess_records(raw_entries):
    cleaned = []
    temp_sum = 0
    for entry in raw_entries:
        parts = entry.strip().split(',')
        value = float(parts[1])
        temp_sum += value
        if parts[0] == 'VALID':
            cleaned.append(value)
    normalization_factor = temp_sum / 100.0 if temp_sum else 1.0
    return [x / normalization_factor for x in cleaned]


def calculate_final_score(data_chunk):
    base = sum(data_chunk)
    penalty = 0
    for val in data_chunk:
        if val > 60:
            penalty += (val - 60) * 0.5
    bonus = len([v for v in data_chunk if v < 30]) * 2
    stability = analyze_readings(data_chunk)
    adjustment = bonus - penalty - (stability / 10)
    final_score = base + adjustment
    
    # Distractor variables and computations
    dummy_accum = 0
    for i in range(len(data_chunk)):
        if i % 2 == 0:
            dummy_accum += data_chunk[i] * 0.1
        else:
            dummy_accum -= data_chunk[i] * 0.05
    shadow_copy = [x * 1.01 for x in data_chunk]
    temp_analysis = sum(shadow_copy) / (len(shadow_copy) + 1e-5)
    
    return final_score

# Main execution
raw_input_data = [
    'INVALID,15.0', 'VALID,25.0', 'VALID,35.0', 'VALID,75.0',
    'VALID,22.0', 'INVALID,80.0', 'VALID,45.0', 'VALID,65.0'
]

interim_results = preprocess_records(raw_input_data)
processed_data = [x * 1.2 for x in interim_results]
processed_data.append(50.0)
processed_data.remove(processed_data[1])  # Remove index 1 to perturb

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")