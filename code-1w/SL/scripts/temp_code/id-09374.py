from itertools import compress, count

def analyze_sensor_data(data_stream):
    baseline = 23.5
    adjustment_factor = 0.89
    temp_offsets = []
    for i, reading in enumerate(data_stream):
        if i % 3 == 0:
            offset = (reading - baseline) * adjustment_factor
        elif i % 3 == 1:
            offset = (reading + baseline) * 0.11
        else:
            offset = reading * 0.01 - baseline * 0.02
        temp_offsets.append(offset)
    
    # Irrelevant filtering path (dead-end computation)
    valid_readings = list(compress(temp_offsets, [abs(x) > 0.5 for x in temp_offsets]))
    avg_valid = sum(valid_readings) / len(valid_readings) if valid_readings else 0.0

    # Distractor: unused transformation
    scaled_offsets = [x * 1.05 for x in temp_offsets]
    normalized = [round(x, 2) for x in scaled_offsets]

    return temp_offsets


def calculate_thermal_rating(log_entries):
    initial_rating = 100.0
    decay_rate = 0.07
    boost_multiplier = 1.2
    penalty_threshold = 12.0
    
    rating = initial_rating
    boost_applied = False
    
    index_counter = count(1)
    for idx, entry in zip(index_counter, log_entries):
        if entry > penalty_threshold and idx % 2 == 1:
            rating -= entry * decay_rate
        elif entry < 5.0:
            rating += 3.5
            if not boost_applied and rating > 80:
                rating *= boost_multiplier
                boost_applied = True
        else:
            rating -= 1.2
    
    # Dead code: this block never executes due to logic above
    final_adjustments = []
    for val in log_entries:
        if val < 0:
            final_adjustments.append(val * -1)
    
    return round(rating, 4)

# Main execution sequence
sensor_input = [25.0, 18.3, 42.1, 16.7, 30.2, 10.5, 50.0, 12.8, 8.9, 40.3]
efficiency_log = analyze_sensor_data(sensor_input)

# Key computational step — target of the question
temperature_buffer = sum(efficiency_log[:4])
thermal_capacity = calculate_thermal_rating(efficiency_log)

# Output result as required
print(f"Target result: {thermal_capacity}")