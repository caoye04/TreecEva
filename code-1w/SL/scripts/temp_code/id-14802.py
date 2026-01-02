import itertools

def main():
    # Sensor data from multiple environmental stations
    raw_readings = [
        (101.3, 22.5, 45.0), (102.1, 23.0, 47.2), (98.7, 21.8, 44.1),
        (115.6, 35.2, 52.8), (105.4, 25.1, 49.9), (97.3, 20.9, 43.5),
        (103.2, 24.0, 48.7), (100.8, 22.7, 46.3)
    ]

    # Irrelevant baseline metadata (distractor)
    station_metadata = {
        'location': 'Area-51',
        'established': 1947,
        'active_sensors': 12,
        'calibration_interval_days': 30
    }

    # Thresholds for anomaly detection (used later)
    threshold_map = {
        'pressure': (99.0, 104.0),
        'temperature': (21.0, 25.0),
        'humidity': (44.0, 50.0)
    }

    # Decoy function that looks important but isn't used
    def compute_entropy(data):
        import math
        total = sum(data)
        return sum(-x/total * math.log2(x/total) for x in data if x > 0)

    # Simulated historical averages (red herring)
    historical_averages = {
        'pressure_avg': 101.5,
        'temp_avg': 22.8,
        'humidity_avg': 46.2
    }

    # Filter readings based on valid pressure range only (key preprocessing)
    valid_pressure_range = (98.0, 110.0)
    filtered_data = [r for r in raw_readings if valid_pressure_range[0] <= r[0] <= valid_pressure_range[1]]

    # Misleading transformation: appears to normalize but unused
    normalized = [( (p-100)/5, (t-22)/3, (h-45)/5 ) for p, t, h in raw_readings]

    # Grouping by temperature bands (partially relevant grouping)
    sorted_by_temp = sorted(filtered_data, key=lambda x: x[1])
    grouped = {k: list(g) for k, g in itertools.groupby(sorted_by_temp, key=lambda x: int(x[1]))}

    # Unused statistical summary (dead code path)
    stats_summary = {}
    for temp_key, group in grouped.items():
        if len(group) > 1:
            pressures = [g[0] for g in group]
            stats_summary[temp_key] = {
                'pressure_mean': sum(pressures) / len(pressures),
                'count': len(group)
            }

    # Core analysis logic
    def is_anomalous(reading, thresholds):
        p, t, h = reading
        p_low, p_high = thresholds['pressure']
        t_low, t_high = thresholds['temperature']
        h_low, h_high = thresholds['humidity']
        return not (p_low <= p <= p_high and t_low <= t <= t_high and h_low <= h <= h_high)

    # Count anomalies per category (complex counting with cross-reference)
    anomaly_flags = [is_anomalous(reading, threshold_map) for reading in filtered_data]
    total_anomalies = sum(anomaly_flags)
    normal_count = len(filtered_data) - total_anomalies

    # Diagnostic scoring with bit manipulation (irrelevant but plausible)
    diagnostic_code = 0
    if total_anomalies > 2:
        diagnostic_code |= 1 << 3
    if normal_count == 0:
        diagnostic_code |= 1 << 1
    if len(filtered_data) < 5:
        diagnostic_code |= 1 << 2

    # Final computation using tuple unpacking and conditional expressions
    base_score = 100 if normal_count > total_anomalies else 75
    penalty = 5 * total_anomalies
    adjustment = -10 if diagnostic_code & 8 else 0  # Only if high anomaly bit set

    final_diagnostic = base_score - penalty + adjustment

    # Output required result
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main()