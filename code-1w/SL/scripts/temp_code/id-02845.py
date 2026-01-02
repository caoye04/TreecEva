def filter_anomalies(data, limit):
    anomalies = set()
    baseline = sum(data) / len(data)
    temp_result = []
    outlier_count = 0

    for val in data:
        if abs(val - baseline) > limit:
            anomalies.add(val)
            outlier_count += 1
        else:
            temp_result.append(val * 0.95)  # discounted values, not used later

    # Irrelevant transformation
    scaled_anomalies = {x * 1.1 for x in anomalies}
    return anomalies


def generate_checksum(sequence):
    # Dead function - never called but looks important
    return sum(x ** 2 for x in sequence) % 1000


def count_vowels(text):
    # Distractor function with no impact
    return sum(1 for c in text.lower() if c in 'aeiou')


def analyze_readings(abnormal_set, log_entries):
    severity = 0
    adjustment_factor = 0.0
    entry_count = len(log_entries)

    # Simulated log analysis (only uses length)
    if entry_count > 5:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 0.8

    base_score = len(abnormal_set)

    total_magnitude = 0
    for reading in abnormal_set:
        total_magnitude += abs(reading)

    # Secondary computation that seems relevant but isn't directly decisive
    average_magnitude = total_magnitude / base_score if base_score > 0 else 0

    # Core logic: diagnostic is based on modular interaction
    intermediate = (base_score * 37) % 100
    severity = (intermediate + entry_count) % 89

    # Final red herring calculation
    hypothetical = (average_magnitude * adjustment_factor) // 10
    final_diagnostic = severity + int(hypothetical)  # Only severity really matters

    return final_diagnostic


# Main execution
threshold = 15
sensor_data = [102, 104, 98, 150, 103, 97, 200, 101]
diagnostics_log = ['ERR_01', 'STATUS_OK', 'ERR_02', 'DEBUG_3', 'WARN_5']
irrelevant_string = "sensor_array_v2"
vowel_count = count_vowels(irrelevant_string)  # Distractor call

filtered = filter_anomalies(sensor_data, threshold)
final_diagnostic = analyze_readings(filtered, diagnostics_log)

Result: final_diagnostic