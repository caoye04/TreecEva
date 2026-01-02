from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [
        ("temp", 23.5), ("humidity", 45.2), ("temp", 24.1), ("pressure", 1013.25),
        ("humidity", 46.0), ("co2", 415), ("temp", 22.8), ("pressure", 1012.9),
        ("humidity", 47.3), ("co2", 423), ("temp", 24.0), ("pressure", 1013.1)
    ]
    return raw_readings

def filter_outliers(data, factor=1.5):
    # Irrelevant outlier filtering (not used in final path)
    values = [v for k, v in data]
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [(k, v) for k, v in data if lower <= v <= upper]

def aggregate_by_type(readings):
    aggregated = defaultdict(list)
    for sensor_type, value in readings:
        aggregated[sensor_type].append(value)
    return aggregated

def compute_rolling_average(values, window=3):
    # Dead code path — never called
    if len(values) < window:
        return values
    averages = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        averages.append(sum(values[start:i+1]) / (i - start + 1))
    return averages

def smooth_signal(signal):
    # Decoy function: looks important but unused
    return [signal[0]] + [
        0.3 * signal[i-1] + 0.4 * signal[i] + 0.3 * signal[i+1]
        for i in range(1, len(signal)-1)
    ] + [signal[-1]]

def calculate_entropy(values):
    count = Counter(values)
    total = len(values)
    entropy = -sum((freq/total) * math.log2(freq/total) for freq in count.values())
    return round(entropy, 4)

def normalize_readings(aggregated):
    normalized = {}
    for typ, vals in aggregated.items():
        avg = sum(vals) / len(vals)
        if typ == "temp":
            normalized[typ] = round(avg + 0.5, 2)  # artificial offset
        elif typ == "humidity":
            normalized[typ] = round(avg - 1.0, 2)
        else:
            normalized[typ] = round(avg, 2)
    return normalized

def derive_secondary_index(norm):
    # Complex but irrelevant secondary index computation
    index = 0
    if "temp" in norm and "humidity" in norm:
        index += (norm["temp"] * 1.8 + 32) * 0.4
        index -= norm["humidity"] * 0.3
    if "pressure" in norm:
        index += norm["pressure"] / 100 * 0.2
    if "co2" in norm:
        index += math.log(norm["co2"]) * 0.1
    return round(index, 3)

def generate_threshold_map():
    # Real threshold map used later
    thresholds = defaultdict(dict)
    thresholds["temp"]["warning"] = 25.0
    thresholds["temp"]["critical"] = 30.0
    thresholds["humidity"]["warning"] = 60.0
    thresholds["humidity"]["critical"] = 75.0
    thresholds["pressure"]["warning"] = 1030.0
    thresholds["pressure"]["critical"] = 970.0  # inverse logic
    thresholds["co2"]["warning"] = 450
    thresholds["co2"]["critical"] = 500
    return thresholds

def evaluate_stability_metrics(norm):
    # Distractor: computes stability but not used in final result
    metrics = {}
    for k, v in norm.items():
        base = {"temp": 20, "humidity": 50, "pressure": 1013, "co2": 400}[k]
        deviation = abs(v - base)
        metrics[k] = "stable" if deviation < 10 else "fluctuating"
    return metrics

def analyze_readings(processed, th_map):
    score = 0
    # Scoring based on threshold comparisons (key logic)
    if "temp" in processed:
        if processed["temp"] >= th_map["temp"]["critical"]:
            score += 50
        elif processed["temp"] >= th_map["temp"]["warning"]:
            score += 20
    if "humidity" in processed:
        if processed["humidity"] >= th_map["humidity"]["critical"]:
            score += 40
        elif processed["humidity"] >= th_map["humidity"]["warning"]:
            score += 15
    if "pressure" in processed:
        critical_low = th_map["pressure"]["critical"]
        warning_low = th_map["pressure"]["warning"]
        if processed["pressure"] <= critical_low:
            score += 45
        elif processed["pressure"] <= warning_low:
            score += 25
    if "co2" in processed:
        if processed["co2"] >= th_map["co2"]["critical"]:
            score += 60
        elif processed["co2"] >= th_map["co2"]["warning"]:
            score += 30
    
    # Introduce logical complexity with bit manipulation
    temp_flag = int(processed.get("temp", 0) > 23)
    humidity_flag = int(processed.get("humidity", 0) > 45)
    co2_flag = int(processed.get("co2", 0) > 420)
    
    flag_combo = (temp_flag << 2) | (humidity_flag << 1) | co2_flag
    
    # Additional scoring adjustment via bitwise logic
    adjustment_map = {
        0b111: -5, 0b110: -2, 0b101: 3, 0b100: 5,
        0b011: -8, 0b010: 0, 0b001: 2, 0b000: 4
    }
    adjusted_score = score + adjustment_map.get(flag_combo, 0)
    
    # Final transformation using logarithmic scaling
    if adjusted_score > 0:
        final_diagnostic = int(math.log(adjusted_score) * 100)
    else:
        final_diagnostic = 0
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw data
    raw_data = collect_sensor_readings()
    
    # Step 2: Aggregate by sensor type (relevant)
    grouped_readings = aggregate_by_type(raw_data)
    
    # Step 3: Normalize the aggregated readings (relevant)
    normalized_data = normalize_readings(grouped_readings)
    
    # Step 4: Generate threshold configuration (relevant)
    threshold_map = generate_threshold_map()
    
    # Irrelevant computations (distractors)
    entropy_profile = {k: calculate_entropy(v) for k, v in grouped_readings.items()}
    secondary_index = derive_secondary_index(normalized_data)
    stability_report = evaluate_stability_metrics(normalized_data)
    
    # Key statement: analyze readings to produce diagnostic
    final_diagnostic = analyze_readings(normalized_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")