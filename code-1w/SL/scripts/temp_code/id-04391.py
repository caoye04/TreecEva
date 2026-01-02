import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9, 24.8, 23.0]
humidity_readings = [45, 50, 52, 60, 58, 65, 70, 55, 48, 53]
pressure_readings = [1013, 1015, 1010, 1008, 1012, 1016, 1018, 1011, 1009, 1014]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G3', 'H6', 'I5', 'J0']
user_preferences = {'units': 'metric', 'alerts': True, 'interval': 5}

# Misleading transformation chain (dead path)
def transform_legacy(codes):
    return [c[::-1] for c in codes if c[0] in 'BCDFGH']

def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

# Unused helper (distractor)
def calculate_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    return -sum((count/total) * log(count/total) for count in freq.values())

# Complex filtering with red herring conditions
def filter_outliers(readings, low_thresh=20.0, high_thresh=25.0):
    anomalies = []
    clean = []
    for i, val in enumerate(readings):
        if val < low_thresh or val > high_thresh:
            anomalies.append((i, val))
        else:
            clean.append(val)
    # Return only clean values (anomalies list unused - misleading)
    return clean

# Decoy function that looks important but is never called
def generate_diagnostic_report(data_list):
    stats = {}
    for i, data in enumerate(data_list):
        stats[f'sensor_{i}'] = {
            'mean': sum(data)/len(data),
            'peak': max(data),
            'stability': calculate_entropy([round(x) for x in data])
        }
    return stats

# Bit manipulation masquerading as encoding (irrelevant)
current_mode = 0b101010
encoded_header = current_mode ^ 0b111111

# Real processing begins here — heavily obscured
normalized_temp = normalize(temperature_readings)
filtered_data = filter_outliers(temperature_readings, low_thresh=21.0, high_thresh=24.5)

# Create complex threshold map with irrelevant expansions
base_thresholds = {'critical': 24.0, 'warning': 22.5}
expanded_keys = ['_'.join(pair) for pair in itertools.product(['upper'], base_thresholds.keys())]
threshold_map = {k: base_thresholds[k.split('_')[1]] + 0.5 for k in expanded_keys}

# Core logic buried in abstraction
def evaluate_stability(value, thresholds):
    if value > thresholds['upper_critical']:
        return 3
    elif value > thresholds['upper_warning']:
        return 2
    else:
        return 1

# Main processing function with early returns and distractors
def process_readings(data, th_map):
    cumulative_score = 0
    penalty_factor = 1.0
    
    # Fake data transformation (unused result)
    reversed_data = [round(x * 1.01, 2) for x in data[::-1]]
    
    for reading in data:
        # Multiple nested conditions with misleading branches
        if reading < 20.0:
            cumulative_score += 1
            continue
        elif 20.0 <= reading < 22.0:
            cumulative_score += 2
        else:
            category = evaluate_stability(reading, th_map)
            if category == 3:
                cumulative_score += 5
                break  # Early termination red herring
            elif category == 2:
                cumulative_score += 3
            else:
                cumulative_score += 4
        
        # Dead logic branch due to placement
        if penalty_factor > 2.0:  # Never true
            cumulative_score -= 1
    
    # Final adjustment using bit trick (actually simple)
    adjustment = (len(data) ^ 7) & 3  # Evaluates to 2
    final_score = cumulative_score + adjustment
    
    # Critical line: this is where the answer is determined
    final_diagnostic = int(final_score * 1000) // len(data) if data else 0
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Target result: {final_diagnostic}")