from collections import defaultdict, Counter

# Simulate sensor data aggregation and anomaly filtering
def main():
    raw_readings = [107, 110, 105, 108, 106, 109, 111, 104, 107, 105, 103, 108, 110, 106]
    baseline_threshold = 105
    adjustment_factor = 0.9
    temp_storage = []
    
    # Step 1: Filter anomalies (values too far from rolling average)
    filtered_readings = []
    for i in range(len(raw_readings)):
        window = raw_readings[max(0, i-3):i]
        if not window:
            window_avg = baseline_threshold
        else:
            window_avg = sum(window) / len(window)
        
        if abs(raw_readings[i] - window_avg) <= 5:
            filtered_readings.append(raw_readings[i])
    
    # Misleading distraction: unused transformation
    inverted_readings = [max(raw_readings) + min(raw_readings) - x for x in raw_readings]
    shadow_buffer = [x * 0.85 for x in inverted_readings if x > 106]
    
    # Step 2: Group by proximity to threshold
    groups = defaultdict(list)
    for val in filtered_readings:
        key = 'high' if val >= baseline_threshold else 'low'
        groups[key].append(val)
    
    # Step 3: Compute adjusted means
    high_avg = sum(groups['high']) / len(groups['high']) if groups['high'] else 0
    low_avg = sum(groups['low']) / len(groups['low']) if groups['low'] else 0
    
    # Distractor: irrelevant statistical computation
    all_counter = Counter(filtered_readings)
    mode_val = all_counter.most_common(1)[0][0] if all_counter else 0
    mode_adjusted = (mode_val * adjustment_factor) if mode_val > 100 else mode_val
    
    # Step 4: Prepare processed data with normalization
    processed_data = []
    for val in filtered_readings:
        normalized = (val - baseline_threshold) * adjustment_factor
        processed_data.append(round(normalized, 2))
    
    # Unused backup logic (dead path)
    def fallback_correction(data):
        return [x + 1 for x in data if x < 0]
    
    # Step 5: Calculate final score based on weighted deviation
    def calculate_final_score(data):
        positive_dev = [x for x in data if x > 0]
        negative_dev = [x for x in data if x < 0]
        neutral_count = len(data) - len(positive_dev) - len(negative_dev)
        
        pos_sum = sum(positive_dev)
        neg_sum = sum(negative_dev)
        
        # Weighting logic
        weight = 1.2 if len(positive_dev) > len(negative_dev) else 0.8
        score = (pos_sum * weight) + (neg_sum * 1.1) + (neutral_count * 0.5)
        return round(score, 2)
    
    final_score = calculate_final_score(processed_data)
    
    # Additional red herring variables
    diagnostic_report = {
        'entries': len(raw_readings),
        'filtered_out': len(raw_readings) - len(filtered_readings),
        'peak': max(filtered_readings),
        'adjusted_peak': max(filtered_readings) * adjustment_factor
    }
    
    temp_storage.append(diagnostic_report)  # Not used further
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()