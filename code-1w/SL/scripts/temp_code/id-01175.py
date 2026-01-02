from collections import defaultdict

# Simulated sensor data processing with noise filtering and scoring
def preprocess_data(raw_data):
    filtered = []
    noise_count = 0
    for val in raw_data:
        if abs(val - 50) > 40:  # Likely noise
            noise_count += 1
            continue
        if val % 2 == 0:
            filtered.append(val + 1)  # Slight correction
        else:
            filtered.append(val)
    return filtered, noise_count

def compute_weights(length):
    weights = [0.1] * length
    mid = length // 2
    for i in range(length):
        if i < mid:
            weights[i] += 0.01 * (mid - i)
        else:
            weights[i] += 0.01 * (i - mid)
    # Dummy normalization (not actually used)
    total_weight = sum(weights)
    normalized = [w / total_weight for w in weights]
    return weights  # Return unnormalized for actual use

def calculate_stability_index(values):
    if len(values) < 2:
        return 0.0
    diffs = [abs(values[i+1] - values[i]) for i in range(len(values)-1)]
    return round(sum(diffs) / len(diffs), 4)

def calculate_final_score(data, thresholds):
    # Preprocess and filter noise
    cleaned_data, dropped = preprocess_data(data)
    
    # Irrelevant statistical distraction
    mean_val = sum(cleaned_data) / len(cleaned_data) if cleaned_data else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in cleaned_data) / len(cleaned_data) if cleaned_data else 0
    
    # Weighted scoring setup
    weights = compute_weights(len(cleaned_data))
    weighted_sum = sum(v * w for v, w in zip(cleaned_data, weights))
    
    # Stability analysis
    stability = calculate_stability_index(cleaned_data)
    stability_bonus = 10 if stability < thresholds['stability'] else 0
    
    # Threshold-based classification
    category_map = defaultdict(int)
    for val in cleaned_data:
        if val < 30:
            category_map['low'] += 1
        elif val < 70:
            category_map['medium'] += 1
        else:
            category_map['high'] += 1
    
    # Distraction: unused transformation
    transformed = [v ** 0.5 for v in cleaned_data if v > 0]
    avg_transformed = sum(transformed) / len(transformed) if transformed else 0
    
    # Scoring logic
    base_score = weighted_sum * 10
    category_bonus = 0
    if category_map['high'] >= 3:
        category_bonus += 25
    if category_map['low'] == 0:
        category_bonus += 15
    
    # Final computation
    final_score = int(base_score + stability_bonus + category_bonus)
    
    # Additional red herring variables
    peak_value = max(cleaned_data) if cleaned_data else 0
    decay_factor = 0.95 ** len(cleaned_data)
    adjusted_score = final_score * decay_factor  # Not used
    
    return final_score

data = [48, 52, 95, 50, 54, 46, 88, 51, 49, 120, 47, 53, 45, 55, 89]
thresholds = {'stability': 8.5}

# Key execution point
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")