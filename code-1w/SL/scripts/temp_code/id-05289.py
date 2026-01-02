import math

# Simulated agricultural data processing with noise filtering and yield prediction
def collect_samples():
    raw_readings = [3, 7, 11, 14, 18, 22, 25, 29, 33, 37, 41, 44, 48, 52]
    return raw_readings[::3]  # Every 3rd reading is calibrated

def filter_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    threshold = 1.5 * std_dev
    filtered = [x for x in data if abs(x - mean_val) <= threshold]
    
    # Irrelevant transformation (distractor)
    temp_analysis = [math.sin(x / 10) for x in data]
    summary_score = sum(temp_analysis) * 0.1
    
    return filtered

def generate_synthetic_controls(base):
    # Dead function - never used, red herring
    synthetic = [b * 1.1 + 2 for b in base]
    return synthetic[:len(base)]

def shift_ph_levels(data, offset=0.3):
    # Misleading environmental adjustment (not affecting final result)
    adjusted = [round(d - offset * 2.1, 2) for d in data]
    return adjusted

def compute_z_scores(values):
    # Unused statistical analysis (dead code path)
    m = sum(values) / len(values)
    s = (sum((v - m)**2 for v in values) / len(values)) ** 0.5
    z_scores = [(v - m) / s for v in values]
    return z_scores

def rolling_window_avg(seq, size=2):
    # Decoy smoothing function
    avgs = []
    for i in range(len(seq) - size + 1):
        avgs.append(sum(seq[i:i+size]) / size)
    return avgs

def classify_growth_rate(val):
    # Partially used logic - only one case matters
    if val > 40:
        return 'high'
    elif val > 30:
        return 'medium'
    else:
        return 'low'

def extract_key_metrics(samples):
    metrics = {}
    
    # Real computation begins
    doubled = [x * 2 for x in samples]
    shifted = doubled[1:] + [doubled[0]]  # Rotate
    
    # Slice-based feature extraction (relevant)
    segment_a = shifted[:3]
    segment_b = shifted[3:]
    
    # Key intermediate (only sum_b is used later)
    sum_a = sum(segment_a)
    sum_b = sum(segment_b)
    
    # Distractor aggregation
    product_a = 1
    for x in segment_a:
        product_a *= x % 17
    
    metrics['base_total'] = sum_b
    metrics['noise_floor'] = product_a  # Unused
    metrics['peak'] = max(shifted)  # Unused
    
    return metrics

def process_environments(raw):
    calibrated = filter_outliers(raw)
    
    # Environmental interference simulation (irrelevant)
    ph_shifted = shift_ph_levels(calibrated)
    
    # Actual relevant path
    enhanced = [val + 5 for val in calibrated if val % 2 == 1]  # Only odd values boosted
    
    # Extra transformation that looks important but isn't used
    normalized = [round(e / sum(enhanced), 3) for e in enhanced]
    
    return enhanced

def harvest_results(data_dict):
    base = data_dict['base_total']
    bonus = data_dict.get('bonus_factor', 0)
    
    # Final calculation
    yield_raw = base * 17
    
    # Conditional boost (never triggers due to data)
    if data_dict.get('growth_class') == 'optimal':
        yield_raw *= 1.5
    
    # Final cap
    final_yield = int(yield_raw % 10000)
    
    return final_yield

# --- Main Execution ---
if __name__ == "__main__":
    # Step 1: Collect raw sample data
    initial_readings = collect_samples()  # [3, 14, 25, 37]
    
    # Step 2: Process environment data (with distractions)
    env_data = process_environments(initial_readings)  # [3, 25] -> [8, 30]
    
    # Step 3: Extract key features from rotated data
    processed_data = extract_key_metrics(env_data)  # base_total = 30
    
    # Step 4: Add classification (partial usage)
    primary_value = env_data[-1]
    cls = classify_growth_rate(primary_value)
    processed_data['growth_class'] = cls  # 'medium'
    
    # Step 5: Compute unused statistics (distractors)
    z_vals = compute_z_scores(env_data)
    rolling_avgs = rolling_window_avg(env_data, 2)
    controls = generate_synthetic_controls(env_data)
    
    # Step 6: Final yield calculation (ANSWER PATH)
    final_yield = harvest_results(processed_data)
    
    # Output target result
    print(f"Result: {final_yield}")