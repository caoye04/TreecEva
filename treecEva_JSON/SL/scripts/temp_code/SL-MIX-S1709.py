from collections import defaultdict
import statistics

def decode_sensor_data(raw_readings):
    decoded = []
    for reading in raw_readings:
        match reading['type']:
            case 'A':
                decoded.append(reading['value'] * 1.2)
            case 'B':
                decoded.append(reading['value'] + 5.5)
            case 'C':
                decoded.append(reading['value'] ** 0.5)
            case _:
                decoded.append(reading['value'])
    return decoded

sensor_network_1 = [
    {'type': 'A', 'value': 25.0},
    {'type': 'B', 'value': 30.0},
    {'type': 'C', 'value': 64.0},
    {'type': 'A', 'value': 20.0}
]

sensor_network_2 = [
    {'type': 'B', 'value': 28.0},
    {'type': 'A', 'value': 22.0},
    {'type': 'C', 'value': 49.0},
    {'type': 'B', 'value': 32.0}
]

decoded_net1 = decode_sensor_data(sensor_network_1)
decoded_net2 = decode_sensor_data(sensor_network_2)

all_temperatures = decoded_net1 + decoded_net2
baseline_avg = statistics.mean(all_temperatures)
anomalies_net1 = {t for t in decoded_net1 if abs(t - baseline_avg) > 5.0}
anomalies_net2 = {t for t in decoded_net2 if abs(t - baseline_avg) > 5.0}

common_anomalies = frozenset(anomalies_net1).intersection(frozenset(anomalies_net2))

anomaly_scores = defaultdict(float)
for anomaly in common_anomalies:
    anomaly_scores['shared'] += anomaly * 0.75

network_stats = {
    'net1_variance': statistics.variance(decoded_net1),
    'net2_variance': statistics.variance(decoded_net2)
}

final_anomaly_score = int(anomaly_scores['shared'] * network_stats['net1_variance'] / network_stats['net2_variance'])
print(f"Result: {final_anomaly_score}")