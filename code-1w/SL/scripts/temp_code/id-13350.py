def analyze_pattern(sequence):
    count = {}
    for item in sequence:
        count[item] = count.get(item, 0) + 1
    return count

# Simulated sensor data with noise
temperature_readings = [23.1, 24.5, 24.5, 25.0, 23.1, 26.3, 25.0, 24.5]
distance_cache = {i: temp ** 0.5 for i, temp in enumerate(temperature_readings)}

# Misleading intermediate processing (not used later)
reversed_readings = temperature_readings[::-1]
rolling_avg = sum(temperature_readings[1:4]) / 3

# Character frequency analysis (distractor)
log_entry = "sys_update_231 sys_init_245 sys_init_245"
char_freq = {}
for ch in log_entry:
    if ch.isalpha():
        char_freq[ch] = char_freq.get(ch, 0) + 1

# Core data structure with relevant information
data_log = {
    'events': ['start', 'update', 'update', 'sync', 'start'],
    'metrics': [88, 92, 76, 85, 90],
    'flags': [True, False, True, True, False]
}

# Weight configuration (some are red herrings)
weights = {
    'base': 0.5,
    'bonus': 0.3,
    'penalty': 0.2,
    'hidden_factor': 1.1  # unused distractor
}

# Auxiliary function that appears important but only partially used
def compute_risk_level(events):
    risk = 0
    for event in events:
        if event == 'sync':
            risk += 10
        elif event == 'error':
            risk += 50
    return risk * 0.1

# Main scoring logic
def calculate_final_score(log, w):
    score = 0
    event_count = analyze_pattern(log['events'])
    
    # Scoring from metrics with conditional weighting
    for i, val in enumerate(log['metrics']):
        if log['flags'][i]:
            score += val * w['base']
        else:
            score += val * (w['base'] - w['penalty'])
    
    # Bonus for multiple 'update' events
    if event_count.get('update', 0) >= 2:
        score += 15 * w['bonus']
    
    # Irrelevant transformation (dead computation)
    temp_dict = {k: v*2 for k, v in event_count.items()}
    
    # Final adjustment based on event types
    if 'sync' in log['events'] and 'start' in log['events']:
        score += 10
        
    return int(score)

# Execution point of interest
final_score = calculate_final_score(data_log, weights)
print(f"Target result: {final_score}")