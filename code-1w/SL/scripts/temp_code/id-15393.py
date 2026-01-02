import itertools

def analyze_temperature_trends(temps):
    # Irrelevant helper: computes moving average but not used in final result
    def moving_average(data, window=3):
        return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]
    
    # Distractor computation
    smoothed = moving_average(temps, 2) if len(temps) > 1 else temps
    max_temp = max(temps)
    min_temp = min(temps)
    temp_range = max_temp - min_temp

    # Relevant transformation: classify each temperature
    classifications = []
    for t in temps:
        if t < 0:
            classifications.append('freezing')
        elif t < 15:
            classifications.append('cold')
        elif t < 25:
            classifications.append('moderate')
        else:
            classifications.append('warm')
    
    # Count transitions between categories (actual relevant logic)
    transitions = 0
    for i in range(len(classifications) - 1):
        if classifications[i] != classifications[i+1]:
            transitions += 1

    # Dead code path - never executed due to input constraints
    if False and len(smoothed) > 100:
        transitions = int(sum(smoothed) / 10)

    return transitions


def calculate_humidity_weight(humidity_list):
    # Unused function - red herring
    avg = sum(humidity_list) / len(humidity_list)
    return 0.5 if avg > 60 else 0.3


def calculate_final_score(data):
    # Extract temperatures
    temps = [entry['temp'] for entry in data]
    
    # Slicing operation: only use last 7 days
    recent_temps = temps[-7:]
    
    # Use itertools to group consecutive identical trend types
    trend_groups = [list(g) for k, g in itertools.groupby(recent_temps)]
    group_lengths = [len(g) for g in trend_groups]
    
    # Lambda function to score based on stability
    stability_score = sum(map(lambda x: x ** 2, filter(lambda x: x >= 2, group_lengths)))
    
    # Main signal: temperature trend transitions
    raw_transitions = analyze_temperature_trends(recent_temps)
    
    # Secondary metric: number of warm days
    warm_days = sum(1 for t in recent_temps if t >= 25)
    
    # Final score calculation
    base_score = raw_transitions * 3
    bonus = warm_days * 2
    penalty = len(group_lengths) * 1  # More splits = less stable
    
    # Distractor variables
    hypothetical_max = 100 * len(recent_temps)  # unused
    normalization_factor = 1.0  # could be used, but isn't
    
    final_score = base_score + bonus - penalty + stability_score
    
    return final_score

# Simulated weather data over 14 days
weather_data = [
    {'day': 1, 'temp': -5, 'humidity': 80},
    {'day': 2, 'temp': -3, 'humidity': 78},
    {'day': 3, 'temp': 2,  'humidity': 75},
    {'day': 4, 'temp': 10, 'humidity': 70},
    {'day': 5, 'temp': 14, 'humidity': 65},
    {'day': 6, 'temp': 18, 'humidity': 60},
    {'day': 7, 'temp': 22, 'humidity': 55},
    {'day': 8, 'temp': 26, 'humidity': 50},
    {'day': 9, 'temp': 28, 'humidity': 52},
    {'day': 10, 'temp': 24, 'humidity': 58},
    {'day': 11, 'temp': 12, 'humidity': 65},
    {'day': 12, 'temp': 8,  'humidity': 70},
    {'day': 13, 'temp': 5,  'humidity': 72},
    {'day': 14, 'temp': 20, 'humidity': 45}
]

# Process data: extract subset
processed_data = weather_data[4:]

# Critical execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")