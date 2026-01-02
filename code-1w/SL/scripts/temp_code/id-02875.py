import itertools

def preprocess_readings(sensor_data):
    filtered = [x for x in sensor_data if x > 0]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    return [round(x, 2) for x in smoothed]

def generate_pairs(elements):
    # Distractor function: generates pairs but not used in final result
    return list(itertools.combinations(elements, 2))

def normalize_vector(vec):
    magnitude = sum(x ** 2 for x in vec) ** 0.5
    return [round(v / magnitude, 3) for v in vec] if magnitude else vec

def evaluate_performance(weights, readings):
    score = 0
    for i, reading in enumerate(readings):
        weight = weights[i % len(weights)]
        adjusted = reading * weight
        penalty = 0
        if adjusted < 0.5:
            penalty = 0.1
        score += adjusted - penalty
    return round(score, 4)

def main():
    raw_sensors = [0.1, -0.2, 0.5, 0.8, 1.3, 0.4, 0.9, 2.1, -0.5]
    temp_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
    
    # Irrelevant processing
    paired_temps = generate_pairs(temp_readings)
    avg_temp = sum(temp_readings) / len(temp_readings)
    temp_anomaly_count = len([t for t in temp_readings if abs(t - avg_temp) > 0.5])
    
    # Relevant data flow
    processed_signal = preprocess_readings(raw_sensors)
    normalized_signal = normalize_vector(processed_signal)
    metric_weights = [0.7, 1.2, 0.9]
    
    # Key distraction: unused intermediate
    reshaped_data = [normalized_signal[i:i+2] for i in range(0, len(normalized_signal), 2)]
    reshaped_data.append([0.1])  # Padding
    
    # Actual computation chain
    trimmed_data = normalized_signal[:len(metric_weights)]  # Truncate to match weight size
    final_score = evaluate_performance(metric_weights, trimmed_data)
    
    # Print required output
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()