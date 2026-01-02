import itertools

# Simulate sensor timing data with noise and calibration parameters
timing_data = [1.2, 0.8, 1.5, 0.9, 1.1]
calibration_factor = 0.95
offset_threshold = 0.1

# Irrelevant intermediate calculations (distractors)
baseline_avg = sum(timing_data) / len(timing_data)
adjusted_readings = [x * calibration_factor for x in timing_data if x > 1.0]
drift_compensation = baseline_avg * 0.02

# Simulate packet sequence analysis (not used in final result)
packet_ids = ['A', 'B', 'C', 'D']
sequence_pairs = list(itertools.combinations(packet_ids, 2))
pair_count = len(sequence_pairs)

# Hidden state tracking with red herring variables
state_log = []
error_flags = []
accumulated_bias = 0.0

# Core processing function with nested logic
def process_results(data, factor):
    filtered = [x for x in data if abs(x - 1.0) > offset_threshold]
    scaled = [x * factor for x in filtered]
    
    # Bitwise manipulation of indices (semi-relevant)
    index_mask = 0
    for i in range(len(scaled)):
        index_mask ^= i  # XOR accumulation of indices
    
    # Multiple assignment distraction
    temp_sum, item_count = 0, 0
    for val in scaled:
        temp_sum += val ** 2
        item_count += 1
    
    # Actual computation path
    raw_total = sum(scaled)
    correction = index_mask * 0.1
    result = raw_total - correction
    
    # Dead code branch (never executed due to fixed condition)
    if False:
        fallback = temp_sum / (item_count + 1)
        return round(fallback, 3)
    
    return round(result, 3)

# Execute main logic
intermediate_flag = len(adjusted_readings) > 3
diagnostic_code = 200 if intermediate_flag else 404

# Key statement
final_score = process_results(timing_data, calibration_factor)

# Print result as required
print(f"Target result: {final_score}")