import itertools
import math

def process_sensor_data(raw_values):
    processed = []
    for val in raw_values:
        if val >= 0:
            processed.append(math.sqrt(val))
        else:
            processed.append(-math.sqrt(abs(val)))
    return processed

def calculate_deviation_threshold(data_points):
    mean_val = sum(data_points) / len(data_points)
    squared_diffs = [(x - mean_val)**2 for x in data_points]
    return math.sqrt(sum(squared_diffs) / len(squared_diffs))

# Sensor readings from 4 different sources
sensor_readings = [16, -9, 25, -4, 36, -49, 64, -81]
processed_signals = process_sensor_data(sensor_readings)
threshold = calculate_deviation_threshold(processed_signals)

# Protocol decision matrix
protocol_action = lambda deviation: (
    'AMPLIFY' if deviation < 2 else
    'ATTENUATE' if deviation < 4 else
    'NORMALIZE' if deviation < 6 else
    'ISOLATE'
)

decision = protocol_action(threshold)
action_multiplier = {'AMPLIFY': 2, 'ATTENUATE': 0.5, 'NORMALIZE': 1, 'ISOLATE': 0}[decision]

# Apply transformation based on decision
transformed_values = list(map(lambda x: x * action_multiplier, processed_signals))

# Evaluation scoring system
score_weights = [1, -1, 1, -1, 1, -1, 1, -1]
weighted_scores = [a*b for a, b in zip(transformed_values, score_weights)]

final_evaluation_score = 0
for i, score in enumerate(weighted_scores):
    case_value = i % 4
    if case_value == 0:
        final_evaluation_score += score * 1.5
    elif case_value == 1:
        final_evaluation_score += score * 2
    elif case_value == 2:
        final_evaluation_score += score * 0.5
    else:  # case_value == 3
        final_evaluation_score -= score

print(f"Result: {final_evaluation_score}")