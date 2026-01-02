import math

def preprocess_data(entries):
    cleaned = []
    outlier_count = 0
    for entry in entries:
        if entry < 0:
            cleaned.append(0)
        elif entry > 100:
            outlier_count += 1
            cleaned.append(100)
        else:
            cleaned.append(entry)
    return cleaned, outlier_count

def calculate_entropy(values):
    # Irrelevant helper function (dead weight)
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def calculate_final_score(data, thresholds):
    normalized = [x / 100.0 for x in data]
    boosted = [math.sqrt(x) if x > 0.5 else x ** 2 for x in normalized]
    
    # Track state across transformations
    high_performers = [b for b in boosted if b > 0.7]
    low_performers = [b for b in boosted if b <= 0.3]
    
    # Intermediate metrics (some irrelevant)
    avg_boost = sum(boosted) / len(boosted)
    peak = max(boosted)
    stability_score = (peak - avg_boost) * 100
    
    # Core logic: weighted scoring
    base_score = sum(normalized)
    bonus = len(high_performers) * thresholds['bonus_per_high']
    penalty = len(low_performers) * thresholds['penalty_per_low']
    adjustment = 1 + (avg_boost * 0.1)
    
    # Simulate conditional scaling
    scale_factor = 1.2 if len(high_performers) >= 3 else 1.0
    
    temp_result = (base_score + bonus - penalty) * adjustment
    final_score = temp_result * scale_factor
    
    # Unused debug variables (distractors)
    debug_snapshot = {
        'input_len': len(data),
        'high_count': len(high_performers),
        'low_count': len(low_performers),
        'stability': stability_score
    }
    
    return int(round(final_score))

# Main execution
raw_data = [85, 92, 45, 67, 53, 96, 22, 78, 81, 89]
config_thresholds = {
    'bonus_per_high': 8,
    'penalty_per_low': 5,
    'activation_limit': 70
}

# Preprocessing step (with side outputs not used later)
processed_data, anomalies = preprocess_data(raw_data)

# Extra computation to increase cognitive load
entropy_value = calculate_entropy(processed_data)
sorted_data = sorted(processed_data, reverse=True)
top_three_avg = sum(sorted_data[:3]) / 3

# Key statement
final_score = calculate_final_score(processed_data, config_thresholds)

# Print result
print(f"Result: {final_score}")