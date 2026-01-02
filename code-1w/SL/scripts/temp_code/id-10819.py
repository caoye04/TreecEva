from collections import defaultdict, Counter

# Simulate agricultural yield optimization with noise and distractions
def preprocess_soil(ph_levels):
    normalized = []
    for val in ph_levels:
        if val < 6.0:
            normalized.append((6.0 - val) * 10)
        elif val > 7.5:
            normalized.append((val - 7.5) * 8)
        else:
            normalized.append(0)
    return [max(0, 10 - x) for x in normalized]

def analyze_rainfall(pattern):
    total = 0
    for i, amount in enumerate(pattern):
        if i % 3 == 0:
            total += amount * 0.7
        elif i % 5 == 0:
            total -= amount * 0.2
    return total // 1 + len(pattern)  # integer division

def calculate_resilience_index(data):
    index = 0
    for i in range(len(data)):
        if data[i] > 70:
            index += 1
            break
    for j in range(i + 1, len(data)):
        index += (data[j] // 10) & 3  # bitwise AND
    return index

def mock_calibration(sequence):
    # Irrelevant calibration function (dead code path)
    result = 0
    for x in sequence:
        result ^= int(x * 1.5)  # XOR operation
    return result

def assess_nutrient_score(profiles):
    score = 0
    for p in profiles:
        score += sum(p.values()) * 0.3
    return round(score, 4)

def optimize_harvest(weather, soils):
    # Core logic disguised among distractors
    baseline = 0
    peak_window = weather[1:6]  # slicing
    
    # Distractor: nutrient scoring (not used in final calculation)
    fake_nutrients = assess_nutrient_score(soils)
    dummy_var = mock_calibration([1.1, 2.2, 3.3])
    
    # Real computation begins
    processed = preprocess_soil([s['ph'] for s in soils])
    rain_effect = analyze_rainfall(weather)
    
    # Use of enumerate and zip
    adjustments = []
    for idx, (w, p) in enumerate(zip(weather, processed)):
        adjustment = (w - 50) * (p + 1) / (idx + 1)
        adjustments.append(adjustment)
    
    base_yield = sum(adjustments) * 12.5
    
    # Secondary correction using resilience
    stress_data = [abs(w - 75) for w in weather]
    resilience = calculate_resilience_index(stress_data)
    
    # Final formula
    final = (base_yield + rain_effect) - (resilience * 4.2)
    
    # Red herring: unused transformation
    transformed = [x.upper() for x in ['a', 'b', 'c']]  # case conversion, irrelevant
    temp_dict = defaultdict(int)
    for k in 'xyz':
        temp_dict[k] += 1
    
    return int(final)  # deterministic integer result

# Input data
climate_data = [68, 72, 75, 66, 80, 85, 70, 60]
soil_profiles = [
    {'ph': 5.8, 'n': 20, 'k': 15},
    {'ph': 6.1, 'n': 18, 'k': 17},
    {'ph': 7.6, 'n': 25, 'k': 10},
    {'ph': 6.3, 'n': 22, 'k': 19},
    {'ph': 5.5, 'n': 15, 'k': 14},
    {'ph': 7.2, 'n': 20, 'k': 18},
    {'ph': 8.0, 'n': 30, 'k': 12},
    {'ph': 6.8, 'n': 19, 'k': 16}
]

# Dead code paths
unused_list = [x**2 for x in range(10)]
counter_noise = Counter('irrelevant')

# Key execution point
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Result: {final_yield}")