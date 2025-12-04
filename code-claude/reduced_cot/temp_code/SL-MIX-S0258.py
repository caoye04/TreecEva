def calculate_bit_impact(bits):
    # Calculate impact based on bit patterns
    impact = 0
    for i, bit in enumerate(bits):
        if bit and i % 2 == 0:
            impact += (1 << i)
        elif bit and i % 3 == 0:
            impact += (i * 2)
    return impact

def analyze_sequence(data):
    # Analyze sequence patterns
    total = sum(data)
    variance = 0
    for x in data:
        variance += (x - total/len(data)) ** 2
    return total, variance / len(data)

def calculate_priority(metrics):
    # Core priority calculation function
    if not metrics:
        return 0
    
    # Extract relevant features
    activity_scores = metrics[::2]
    importance_values = metrics[1::2]
    
    # Calculate base priority
    base = sum(a * i for a, i in zip(activity_scores, importance_values))
    
    # Apply scaling factor
    scaling = max(importance_values) / 10 if importance_values else 1
    
    # Final priority calculation
    return int(base * scaling)

# Sensor data collection
raw_data = [5, 12, 8, 3, 9, 15, 6, 11, 7, 14]
decay_factors = [0.9, 0.85, 0.95, 0.8, 0.75]

# Process environmental factors
environmental_coefficients = [1.2, 0.8, 1.5, 0.6, 1.1]
terrain_difficulty = [3, 5, 2, 4, 1]

# Unused weather conditions
weather_impact = {'sunny': 1.0, 'cloudy': 0.8, 'rainy': 0.6, 'stormy': 0.4}
current_weather = 'cloudy'

# Bit flags for system status (distractor)
status_bits = [True, False, True, True, False, True, False, False]
bit_impact = calculate_bit_impact(status_bits)

# Data processing
processed_data = []
for i, value in enumerate(raw_data):
    if i < len(decay_factors):
        decay = decay_factors[i]
    else:
        decay = 0.7  # Default decay
    
    # Apply environmental adjustment
    env_idx = i % len(environmental_coefficients)
    env_factor = environmental_coefficients[env_idx]
    
    # Calculate processed value
    processed = value * decay * env_factor
    processed_data.append(round(processed, 2))

# Calculate sequence metrics (distractor)
total_sequence, variance = analyze_sequence(raw_data)

# Filter metrics based on terrain difficulty
filtered_metrics = []
for i, (value, terrain) in enumerate(zip(processed_data, terrain_difficulty * 2)):
    # Apply terrain filtering
    if terrain > 2:
        filtered_metrics.append(value)
        
        # Add importance factor (every second element)
        if len(filtered_metrics) % 2 == 1:
            # This creates alternating pattern of values and importance
            terrain_factor = min(terrain, 4)  # Cap at 4
            filtered_metrics.append(terrain_factor)

# Distractor calculation
potential_threshold = sum(terrain_difficulty) / len(terrain_difficulty)
if variance > 10 and bit_impact > 20:
    system_mode = "high_alert"
    alert_level = 3
else:
    system_mode = "normal"
    alert_level = 1

# The key calculation
priority_score = calculate_priority(filtered_metrics)

# Distractor final calculations
adjusted_score = priority_score + (alert_level * 5)
final_impact = (bit_impact / 10) + (variance / 5)

print(f"Processed data: {processed_data}")
print(f"Filtered metrics: {filtered_metrics}")
print(f"System mode: {system_mode}, Alert level: {alert_level}")
print(f"Result: {priority_score}")