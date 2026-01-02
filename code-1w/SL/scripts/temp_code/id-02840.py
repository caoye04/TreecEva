from collections import defaultdict, Counter
import math

# Simulate agricultural yield optimization with environmental data
def analyze_rainfall(patterns):
    total_rain = sum([p[1] for p in patterns if p[0] == 'rain'])
    peak_days = [p[2] for p in patterns if p[1] > 8]
    avg_intensity = total_rain / len(patterns) if patterns else 0
    return total_rain, len(peak_days), avg_intensity

def calculate_ph_balance(readings):
    balanced = [r for r in readings if 6.0 <= r <= 7.0]
    deviation = sum(abs(r - 6.5) for r in readings)
    return len(balanced), deviation

def simulate_growth_stages(days):
    stages = []
    for i in range(days):
        stage = (i % 4) + 1
        stress = (i * 0.1) % 1.0
        stages.append((i, stage, stress > 0.8))
    mature_days = sum(1 for s in stages if s[1] == 4)
    return mature_days

# Irrelevant helper - dead code path (decoy)
def predict_market_prices(trends):
    weights = [0.1, 0.3, 0.6]
    forecast = 0
    for i, trend in enumerate(trends):
        forecast += trend * weights[i % 3]
    return forecast * 1.15

# Unused transformation (distractor)
def normalize_readings(data):
    if not data:
        return []
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data if x != -1]

# Core logic disguised among distractions
def evaluate_crop_resilience(soil_list, climate_seq):
    resilience_score = 0
    ph_metrics = defaultdict(int)
    
    for idx, entry in enumerate(soil_list):
        ph_metrics['total'] += 1
        if 5.5 <= entry['ph'] <= 7.5:
            resilience_score += 2
            ph_metrics['optimal'] += 1
        else:
            resilience_score -= 1
            
        # Distractor: complex but unused calculation
        stability_factor = math.log(abs(entry['ph'] - 6.5) + 1) * (idx + 1)
        ph_metrics['drift'] += stability_factor

    # Real computation embedded here
    rainfall_data = [c for c in climate_seq if c[0] in ['rain', 'storm']]
    base_yield = len(rainfall_data) * resilience_score
    
    # Another decoy structure
    shadow_buffer = []
    for _ in range(3):
        temp = (base_yield * 0.1) ** 0.5
        shadow_buffer.append(int(temp))
    
    # Actual contribution
    if ph_metrics['optimal'] >= 3:
        base_yield *= 1.25
    
    return base_yield

# Misleading function that looks important but isn't used in final path
def compute_seasonal_index(timestamps):
    index_vals = []
    for t in timestamps:
        val = (t % 7) * math.sin(t * 0.1)
        index_vals.append(abs(val))
    return sum(index_vals) / len(index_vals) if index_vals else 0

# Key function containing red herrings and real logic
def optimize_harvest(weather, soils):
    # Irrelevant preprocessing
    filtered_weather = [w for w in weather if w[1] > 0]
    daily_cycles = [(i, w[0]) for i, w in enumerate(filtered_weather)]
    
    # Real data extraction
    rain_patterns = [(w[0], w[1], i) for i, w in enumerate(weather) if w[0] == 'rain']
    total_rain, peak_count, _ = analyze_rainfall(rain_patterns)
    
    # Decoy usage
    time_stamps = [i for i in range(len(weather))]    
    _ = compute_seasonal_index(time_stamps)  # result discarded
    
    # Real processing
    ph_readings = [s['ph'] for s in soils]
    balanced_count, deviation = calculate_ph_balance(ph_readings)
    
    # Complex distraction: tuple unpacking, slicing, unused results
    history_log = []
    for i in range(len(soils)):
        subset = soils[i:i+2]
        avg_ph = sum(s['ph'] for s in subset) / len(subset)
        status = 'stable' if avg_ph >= 6.0 else 'unstable'
        history_log.append((i, avg_ph, status))
    
    recent_trend = history_log[-3:] if len(history_log) >= 3 else history_log
    critical_phase = recent_trend[1] if len(recent_trend) > 1 else None
    
    # Shadow variable - looks like it's used but isn't
    potential_yield = 0
    for record in weather:
        if record[0] == 'sun' and record[1] > 6:
            potential_yield += int(record[1] // 2)
    
    # Main yield calculation - uses prior functions
    base_output = evaluate_crop_resilience(soils, weather)
    growth_days = simulate_growth_stages(len(weather))
    
    # Final integration with distractors
    modifiers = []
    if total_rain > 50:
        modifiers.append(1.1)
    if balanced_count >= 4:
        modifiers.append(1.15)
    if deviation < 5.0:
        modifiers.append(1.05)
    
    multiplier = 1.0
    for mod in modifiers:
        multiplier *= mod
    
    # Dead code - never executed
    if False:
        backup_calc = math.ceil(potential_yield * 0.8)
        multiplier = max(multiplier, backup_calc / 100)
    
    final_yield = int(base_output * multiplier)
    
    # Print required at end
    print(f"Target result: {final_yield}")
    return final_yield

# Input data setup
climate_data = [
    ('sun', 7, 'morning'), ('rain', 6, 'noon'), ('sun', 8, 'afternoon'),
    ('storm', 12, 'night'), ('sun', 5, 'morning'), ('rain', 9, 'noon'),
    ('sun', 9, 'afternoon'), ('cloud', 3, 'night'), ('sun', 10, 'morning'),
    ('rain', 7, 'noon')
]

soil_profiles = [
    {'id': 'A1', 'ph': 6.8, 'nutrients': [3, 7, 2]},
    {'id': 'B2', 'ph': 5.9, 'nutrients': [4, 6, 3]},
    {'id': 'C3', 'ph': 7.1, 'nutrients': [5, 5, 1]},
    {'id': 'D4', 'ph': 6.3, 'nutrients': [6, 4, 4]},
    {'id': 'E5', 'ph': 5.7, 'nutrients': [7, 3, 2]},
    {'id': 'F6', 'ph': 6.9, 'nutrients': [8, 2, 3]}
]

# Execution point
final_yield = optimize_harvest(climate_data, soil_profiles)