import heapq
import math

temp_readings = [22.5, 23.1, 24.0, 23.7, 25.2, 26.8, 24.9, 27.3]
sensor_offsets = { 'S1': 0.3, 'S2': -0.2, 'S3': 0.1 }
base_calibration = frozenset(['S1', 'S3'])
active_sensors = {'S1', 'S2', 'S4'}
operational_set = base_calibration | active_sensors

adjusted_readings = []
for idx, temp in enumerate(temp_readings):
    sensor_id = f'S{(idx % 3) + 1}'
    offset = sensor_offsets.get(sensor_id, 0)
    calibrated_temp = temp + offset
    if sensor_id in operational_set:
        adjusted_readings.append(calibrated_temp)

anomaly_heap = []
for reading in adjusted_readings[:5]:
    heapq.heappush(anomaly_heap, -reading)

if len(anomaly_heap) >= 3:
    top_three_sum = 0
    for _ in range(3):
        top_three_sum += -heapq.heappop(anomaly_heap)
    average_spike = top_three_sum / 3
else:
    average_spike = max(adjusted_readings) if adjusted_readings else 0

peak_anomaly = round(average_spike * 100)
print(f'Result: {peak_anomaly}')