from collections import defaultdict

def compute_longest_sequence(readings):
    if not readings:
        return 0, 0
    max_length = 1
    current_length = 1
    max_value = readings[0]
    for i in range(1, len(readings)):
        if readings[i] == readings[i-1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_value = readings[i-1]
            current_length = 1
    if current_length > max_length:
        max_length = current_length
        max_value = readings[-1]
    return max_length, max_value

sensor_data = {
    'sensor_3': [7, 7, 2, 2, 2, 9],
    'sensor_1': [5, 5, 5, 1, 1],
    'sensor_2': [3, 3, 3, 3, 8, 8],
    'sensor_4': [6, 6, 6, 6, 6, 4, 4]
}

stability_scores = {}
for sensor_id, readings in sensor_data.items():
    length, value = compute_longest_sequence(readings)
    stability_scores[sensor_id] = length * value

highest_score = max(stability_scores.values())
final_stability_index = None
for sid in sorted(stability_scores.keys()):
    if stability_scores[sid] == highest_score:
        final_stability_index = stability_scores[sid]
        break

print(f"Result: {final_stability_index}")