from collections import defaultdict, Counter
from itertools import cycle, islice

def main():
    # Sensor simulation setup (real data pipeline)
    raw_readings = [
        (101, 23.4, 'A'), (102, 24.1, 'B'), (103, 22.8, 'A'),
        (104, 25.6, 'C'), (105, 23.9, 'B'), (106, 26.1, 'C'),
        (107, 22.5, 'A'), (108, 24.7, 'B'), (109, 25.2, 'C')
    ]

    # Irrelevant calibration sequence (distractor)
    calibration_sequence = [0.1, -0.2, 0.05, -0.15, 0.3]
    adjusted_offsets = []
    for i, offset in enumerate(calibration_sequence):
        if i % 2 == 0:
            adjusted_offsets.append(offset * 1.5)
        else:
            adjusted_offsets.append(offset * 0.8)

    # Decoy transformation (dead code path)
    def transform_legacy(x):
        return (x + 32) * 5 / 9  # Unused conversion

    # Real preprocessing logic
    sensor_map = defaultdict(list)
    for sid, temp, group in raw_readings:
        sensor_map[group].append(temp)

    avg_readings = {}
    for grp, temps in sensor_map.items():
        avg_readings[grp] = sum(temps) / len(temps)

    # Threshold policy setup (critical)
    base_thresholds = {'A': 23.0, 'B': 24.0, 'C': 25.0}
    fluctuation_scores = []
    for _, temps in sensor_map.items():
        mean_temp = sum(temps) / len(temps)
        variance = sum((t - mean_temp) ** 2 for t in temps) / len(temps)
        fluctuation_scores.append(variance * 100)

    # Red herring: fake anomaly detection (irrelevant)
    anomaly_flags = []
    for val in fluctuation_scores:
        if val > 2.0:
            anomaly_flags.extend(['WARNING', 'REVIEW'])
        elif val > 1.0:
            anomaly_flags.append('MONITOR')

    # Real threshold adjustment logic
    threshold_map = {}
    for k, v in base_thresholds.items():
        adjustment = 0.5 if avg_readings[k] > v else -0.3
        threshold_map[k] = v + adjustment

    # Filtering valid readings (key step)
    filtered_data = []
    for sid, temp, group in raw_readings:
        if temp > 22.0 and group in ['A', 'B', 'C']:
            filtered_data.append((sid, temp, group))

    # Bit manipulation decoy (misleading intermediate)
    encoded_id_sum = 0
    for sid, _, _ in filtered_data:
        encoded_id_sum ^= sid  # XOR chain distraction
        encoded_id_sum = (encoded_id_sum << 1) & 0xFF  # Shift and mask noise

    # Core processing function (contains answer)
    def process_readings(data, thresholds):
        result = 0
        group_count = Counter(g for _, _, g in data)
        for sid, temp, group in data:
            if temp > thresholds[group]:
                weight = group_count[group] * 0.1
                result += (temp * weight) // 1
        return int(result * 10)

    # Execution point of interest
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Unused visualization prep (distractor block)
    time_series = list(enumerate([r[1] for r in raw_readings]))
    paired_stream = list(zip(
        islice(cycle(['morning', 'afternoon', 'night']), len(time_series)),
        time_series
    ))

    # Output the target result
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()