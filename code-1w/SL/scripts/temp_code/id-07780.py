from collections import defaultdict, Counter

# Simulate agricultural yield prediction with noise and red herrings
def analyze_soil_composition(data):
    # Irrelevant analysis function (dead end)
    ph_levels = [6.5, 7.2, 8.0, 5.9]
    nutrient_score = 0
    for val in ph_levels:
        nutrient_score += (val * 1.5) % 3
    return nutrient_score

def preprocess_field_readings(raw_readings):
    # Distractor: processes irrelevant sensor data
    filtered = []
    for r in raw_readings:
        if r > 100 and r < 950:
            filtered.append(r // 4)
    return [x for x in filtered if x % 2 == 0]

def calculate_growth_potential(temp_data, moisture_data):
    # Misleading intermediate calculation
    base_potential = 0
    adjustments = []
    for t in temp_data:
        if t > 25:
            adjustments.append(t - 25)
        else:
            adjustments.append(0)
    for adj in adjustments:
        base_potential += adj * 0.3
    return base_potential + 12.5  # decoy value

def compute_resilience_factor(stress_events):
    # Unused complexity: resilience not actually used in final logic
    factor = 1.0
    event_counter = Counter(stress_events)
    for event, count in event_counter.items():
        if event == 'drought':
            factor *= (0.8 ** count)
        elif event == 'frost':
            factor *= (0.9 ** count)
    return round(factor, 4)

def calculate_harvest_efficiency(fields, cycles):
    efficiency_map = defaultdict(float)
    total_adjustment = 0.0
    
    # Real logic begins here — nested and interwoven with distractions
    for field_id, metrics in fields.items():
        base_yield = metrics['base']
        slope = metrics['slope']
        elevation = metrics['elev']
        
        # Key calculation chain (8+ steps)
        temp_boost = 0
        for cycle in cycles:
            phase = cycle['phase']
            temp = cycle['temp']
            rainfall = cycle['rain']
            
            if phase == 1:
                temp_boost += max(0, (temp - 20) * 0.4)
            elif phase == 2:
                if rainfall > 60:
                    temp_boost += 5
                else:
                    temp_boost += 2
            else:
                temp_boost += min(3, (rainfall // 20))
        
        # Critical path: efficiency depends on accumulated temp_boost
        modifier = 1.0 + (temp_boost / 100)
        
        # Elevation correction
        if elevation > 300:
            modifier *= (1 - ((elevation - 300) * 0.001))
        
        # Slope penalty
        if slope > 15:
            modifier *= 0.9
        
        # Final per-field efficiency
        efficiency_map[field_id] = base_yield * modifier
    
    # Aggregate across fields
    cumulative = 0
    for val in efficiency_map.values():
        cumulative += val
    
    # Red herring: unused transformation
    inverted = [1/v for v in efficiency_map.values() if v > 0]
    avg_inverse = sum(inverted) / len(inverted) if inverted else 0
    
    # Actual answer derived here
    total_adjustment = cumulative * 0.87  # Final scaling
    
    # Decoy variables
    phantom_yield = sum(efficiency_map.values()) * 0.1
    dummy_offset = avg_inverse * 10
    
    return int(total_adjustment)  # deterministic integer result

# Main execution block
if __name__ == '__main__':
    # Input data
    field_data = {
        'F07A': {'base': 420, 'slope': 12, 'elev': 210},
        'F08B': {'base': 380, 'slope': 18, 'elev': 340},
        'F09C': {'base': 450, 'slope': 10, 'elev': 180}
    }
    
    growth_cycles = [
        {'phase': 1, 'temp': 24, 'rain': 40},
        {'phase': 2, 'temp': 27, 'rain': 75},
        {'phase': 3, 'temp': 26, 'rain': 50},
        {'phase': 1, 'temp': 28, 'rain': 30}
    ]
    
    # Noise input: triggers distractor functions
    sensor_readings = [120, 250, 960, 880, 410, 105]
    climate_events = ['drought', 'drought', 'frost']
    temperature_log = [22, 25, 28, 30, 26]
    moisture_log = [50, 70, 65, 80]
    
    # Execute distractors (no effect on final result)
    _ = analyze_soil_composition(sensor_readings)
    _ = preprocess_field_readings(sensor_readings)
    _ = calculate_growth_potential(temperature_log, moisture_log)
    _ = compute_resilience_factor(climate_events)
    
    # Critical statement
    final_yield = calculate_harvest_efficiency(field_data, growth_cycles)
    
    # Output result
    print(f"Target result: {final_yield}")