def detect_anomalies(sensor_readings):
    anomalies = set()
    baseline = sum(sensor_readings[::2]) / len(sensor_readings[::2])
    for i, reading in enumerate(sensor_readings):
        if i % 2 == 0:
            continue
        if abs(reading - baseline * (1 + i * 0.05)) > 15:
            anomalies.add(i)
    return anomalies

def compute_health_score(metrics, weights):
    score = 0
    for m, w in zip(metrics, weights):
        score += m * w
    return score if score > 0 else 0

def filter_valid_codes(codes):
    valid_set = {i for i in codes if i % 4 == 0 and i > 10}
    temp_invalid = {i for i in codes if i % 3 == 0}
    return valid_set.difference(temp_invalid)

def repair_sequence(seq):
    repaired = []
    for x in seq:
        if x < 0:
            repaired.append(abs(x) * 2)
        elif x % 2 == 0:
            repaired.append(x + 1)
        else:
            repaired.append(x)
    return repaired

def analyze_system_faults(codes):
    filtered = filter_valid_codes(codes)
    extended_codes = [c * 2 for c in codes if c < 50]
    merged = list(filtered) + extended_codes
    sorted_codes = sorted(set(merged), reverse=True)
    
    # Irrelevant aggregation
    total_pairs = 0
    for i in range(len(sorted_codes)):
        for j in range(i+1, len(sorted_codes)):
            if (sorted_codes[i] - sorted_codes[j]) % 7 == 0:
                total_pairs += 1
    
    # Decoy statistical calculation
    avg_gap = 0
    if len(sorted_codes) > 1:
        gaps = [sorted_codes[i] - sorted_codes[i+1] for i in range(len(sorted_codes)-1)]
        avg_gap = sum(gaps) / len(gaps) if gaps else 0
    
    # Core logic disguised among distractions
    critical_count = 0
    for code in sorted_codes:
        binary_rep = bin(code)[2:]
        if binary_rep.count('1') % 3 == 0:
            critical_count += 1
        if critical_count > 5:
            break
    
    # Misleading intermediate
    pseudo_entropy = 0
    if critical_count > 0:
        pseudo_entropy = (avg_gap + total_pairs) / critical_count
    
    # Actual key computation
    adjustment_factor = len(filtered) - len(extended_codes)
    base_value = sum(sorted_codes[:4]) if len(sorted_codes) >= 4 else sum(sorted_codes)
    final_diagnostic = base_value + (critical_count * 17) + adjustment_factor
    
    return final_diagnostic

def main():
    # Real input data
    sensor_data = [23, 45, 12, 67, 34, 89, 21, 56, 78, 33]
    performance_metrics = [88, 76, 92, 65]
    weight_vector = [0.2, 0.3, 0.4, 0.1]
    diagnostic_codes = [16, 21, 24, 33, 40, 48, 52, 64, 72]
    
    # Dead path 1: unused function call structure
    anomaly_indices = detect_anomalies(sensor_data)
    health_score = compute_health_score(performance_metrics, weight_vector)
    
    # Dead path 2: irrelevant transformation
    shuffled = [x ^ 5 for x in performance_metrics]
    processed_shuffled = repair_sequence(shuffled)
    
    # Key execution point
    final_diagnostic = analyze_system_faults(diagnostic_codes)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()