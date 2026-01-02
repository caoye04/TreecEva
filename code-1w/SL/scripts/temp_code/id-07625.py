import itertools

def analyze_wind_pattern(data):
    # Irrelevant function - dead code path
    return sum(x ** 2 for x in data if x > 5)

def generate_seasonal_cycle(length):
    # Distractor: generates unused seasonal weights
    return [(i % 4 + 1) ** 1.5 for i in range(length)]

def filter_noisy_readings(readings):
    # Misleading preprocessing - not actually used in final logic
    cleaned = []
    for val in readings:
        if abs(val - 25.0) < 10:
            cleaned.append(val * 0.9)
        else:
            cleaned.append(25.0)
    return cleaned

def recursive_drought_score(seq, index):
    # Unused recursive red herring
    if index == 0:
        return seq[0]
    prev = recursive_drought_score(seq, index - 1)
    return prev + (seq[index] * 0.5 if seq[index] < 30 else -10)

def calculate_harvest_efficiency(climate_data, start_idx):
    # Core relevant logic begins
    base_threshold = 28.5
    elevation_factor = 0.88
    temp_series = [x[0] for x in climate_data]
    rainfall_series = [x[1] for x in climate_data]
    
    # Bit manipulation decoy
    magic_seed = 0
    for t in temp_series[:5]:
        magic_seed ^= int(t) & 7
    
    # Irrelevant combinatorics with itertools
    permutations_count = 0
    for _ in itertools.permutations([1, 2, 3], 3):
        permutations_count += 1  # Always 6, but distracts
    
    # Simulated sensor calibration (dead code)
    calibration_offset = 0
    for i, temp in enumerate(temp_series):
        if i % 7 == 0:
            calibration_offset += (temp % 3) * 0.1
    
    # Actual key computation chain
    accumulated_heat = 0
    stress_days = 0
    peak_rain_impact = 0
    
    for i in range(len(climate_data)):
        temp, rain = climate_data[i]
        
        # Relevant conditional logic
        if temp > base_threshold:
            accumulated_heat += (temp - base_threshold) * 1.2
        
        if rain < 5:
            stress_days += 1
        elif rain > 50:
            peak_rain_impact += rain * 0.3
        
    # Complex interdependent calculation
    baseline_yield = 850.0
    heat_penalty = accumulated_heat * 1.8
    stress_penalty = stress_days * 7.5
    bonus = peak_rain_impact * 0.4
    
    # Destructuring distraction (unused)
    _, _, *other_temps = temp_series
    summary_stats = {"avg_temp": sum(temp_series) / len(temp_series), "total_rain": sum(rainfall_series)}
    outlier_check = [t for t in temp_series if abs(t - 25) > 15]
    
    # Final efficiency formula
    raw_yield = baseline_yield - heat_penalty - stress_penalty + bonus
    elevation_adjusted = raw_yield * elevation_factor
    
    # Key assignment - answer depends on this
    final_yield = max(elevation_adjusted, 50)  # Floor at 50
    
    # More red herrings
    synthetic_index = 0
    for combo in itertools.combinations([2, 4, 6], 2):
        synthetic_index += combo[0] * combo[1]
    
    return final_yield

# Unused data structure
sensor_metadata = {
    'location': 'Zone-G',
    'calibration_date': '2023-06-15',
    'units': ['Celsius', 'mm/hour']
}

# Main input data (simulated 10-day climate log)
climate_data = [
    (30.2, 12), (29.1, 8), (31.5, 4), (27.3, 60), (33.0, 3),
    (30.8, 2), (26.9, 70), (32.4, 1), (28.7, 55), (29.5, 6)
]

# Dead function call
seasonal_weights = generate_seasonal_cycle(10)

# Trigger main logic
final_yield = calculate_harvest_efficiency(climate_data, 0)
print(f"Target result: {final_yield}")