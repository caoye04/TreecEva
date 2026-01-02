from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic logic
def collect_sensor_data():
    raw_readings = [
        (101, 23.4, 'temp'), (102, 45.1, 'pressure'), (103, 23.4, 'temp'),
        (104, 18.9, 'humidity'), (105, 45.1, 'pressure'), (106, 77.2, 'temp'),
        (107, 18.9, 'humidity'), (108, 91.3, 'temp'), (109, 45.1, 'pressure')
    ]
    return raw_readings

def filter_anomalies(readings):
    # Irrelevant filtering (not used in final path)
    valid = []
    for sid, val, typ in readings:
        if val > 0:
            valid.append((sid, val, typ))
    return valid

def categorize_by_type(readings):
    categorized = defaultdict(list)
    for sensor_id, value, s_type in readings:
        categorized[s_type].append(value)
    return categorized

def compute_averages(cat_data):
    averages = {}
    for typ, vals in cat_data.items():
        averages[typ] = sum(vals) / len(vals)
    return averages

def detect_outliers(vals, tolerance=1.5):
    # Simple outlier detection using IQR
    sorted_vals = sorted(vals)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - tolerance * iqr, q3 + tolerance * iqr
    return [v for v in vals if v < lower or v > upper]

def transform_values(data_dict, scalar=0.8):
    # Applies scaling to all values (distractor)
    transformed = {}
    for k, v_list in data_dict.items():
        transformed[k] = [x * scalar for x in v_list]
    return transformed

def generate_signature(values):
    # Creates a hash-like signature (red herring)
    sig = 0
    for v in values:
        sig ^= int(v * 100) % 97
    return sig

def build_correlation_matrix(types_list):
    # Builds dummy correlation map (dead code path)
    matrix = defaultdict(dict)
    for t1 in types_list:
        for t2 in types_list:
            if t1 != t2:
                matrix[t1][t2] = round(math.sin(hash(t1+t2) % 10), 3)
    return matrix

def count_frequencies(data):
    # Counts frequency of rounded values (partially relevant)
    freqs = Counter()
    for val_list in data.values():
        for v in val_list:
            freqs[round(v)] += 1
    return freqs

def calculate_entropy(freq_counter):
    total = sum(freq_counter.values())
    entropy = 0.0
    for count in freq_counter.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def derive_threshold_map(avg_dict, freq_counter):
    # Creates adaptive thresholds based on averages and frequencies
    thresh_map = {}
    for typ, avg in avg_dict.items():
        adjustment = 5.0 if freq_counter.get(round(avg), 0) > 1 else 2.5
        thresh_map[typ] = avg + adjustment
    return thresh_map

def identify_extremes(data):
    # Finds min/max per type (distractor)
    extremes = {}
    for typ, vals in data.items():
        extremes[typ] = (min(vals), max(vals))
    return extremes

def analyze_readings(processed, thresholds):
    # Core diagnostic logic
    diagnostics = []
    for typ, vals in processed.items():
        above_thresh = [v for v in vals if v > thresholds[typ]]
        diagnostics.append(len(above_thresh))
    # Final computation: product of counts, adjusted by entropy factor
    base_score = 1
    for d in diagnostics:
        base_score *= (d + 1)  # Avoid zeroing
    entropy_component = calculate_entropy(Counter([len(diagnostics), len(thresholds)]))
    final_score = base_score * (1 + entropy_component)
    return int(final_score)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    readings = collect_sensor_data()
    
    # Step 2: Categorize data by type (relevant)
    categorized = categorize_by_type(readings)
    
    # Step 3: Compute average per type (relevant)
    averages = compute_averages(categorized)
    
    # --- Distractor Section ---
    anomalies = detect_outliers([v for vals in categorized.values() for v in vals])
    transformed_data = transform_values(categorized, scalar=0.8)
    sig_temp = generate_signature(transformed_data['temp'])
    sig_press = generate_signature(transformed_data['pressure'])
    correlation = build_correlation_matrix(list(categorized.keys()))
    extremes = identify_extremes(categorized)
    # --------------------------
    
    # Step 4: Count frequencies for entropy calculation (semi-relevant)
    frequencies = count_frequencies(categorized)
    
    # Step 5: Derive dynamic thresholds (relevant)
    threshold_map = derive_threshold_map(averages, frequencies)
    
    # Step 6: Analyze readings against thresholds (critical)
    final_diagnostic = analyze_readings(categorized, threshold_map)
    
    # Print result
    print(f"Result: {final_diagnostic}")