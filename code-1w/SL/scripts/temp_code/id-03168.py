import math

# Irrelevant astronomical constants (distractor)
AU_IN_KM = 149597870.7
LIGHT_YEAR_YEARS = 365.25 * 24 * 3600

def solar_flux(angle):
    # Unused function - red herring
    return AU_IN_KM / (angle + 1) if angle > 0 else 0

def generate_noise(length, seed=42):
    # Dead code path - not used in main logic
    result = []
    for i in range(length):
        seed = (seed * 937) % 10007
        result.append((seed % 100) / 100.0)
    return result

def calculate_entropy(sequence):
    # Misleading mathematical computation with no impact
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 3)

# Simulated climate data over 12 months (temperature, rainfall)
climate_data = [
    (22.5, 80), (23.1, 75), (24.3, 90), (26.0, 110),
    (28.2, 130), (29.5, 140), (30.1, 150), (29.8, 145),
    (28.0, 130), (26.2, 110), (24.0, 95), (22.8, 85)
]

# Soil nutrient profiles across 4 zones (N, P, K levels)
soil_profiles = [
    [0.8, 0.6, 0.7], [0.9, 0.5, 0.8], [0.7, 0.7, 0.6], [0.6, 0.8, 0.9]
]

# Phantom transformation matrix (unused)
transform_matrix = [[(i + j) % 3 for j in range(4)] for i in range(4)]

# Auxiliary function to compute water stress index (used)
def compute_water_stress(rainfall_list):
    avg_rain = sum(r for _, r in rainfall_list) / len(rainfall_list)
    threshold = 100
    if avg_rain < threshold:
        return 1 - (avg_rain / threshold)
    return 0.0

# Helper: nutrient balance score (used)
def nutrient_balance(zone):
    n, p, k = zone
    return (n + p + k) / 3 * (1 + abs(n - p) + abs(p - k))  # weighted consistency

# Complex multi-step optimization function with list comprehensions and filtering
def optimize_harvest(weather, soils):
    # Step 1: Extract high-temperature months (>27C)
    hot_months = [temp for temp, rain in weather if temp > 27]
    
    # Step 2: Compute growth potential from temperature
    temp_factor = sum(math.sin(math.radians(t - 20)) for t in hot_months) / len(hot_months) if hot_months else 0.5
    
    # Step 3: Water stress adjustment
    water_stress = compute_water_stress(weather)
    water_factor = 1 - 0.6 * water_stress
    
    # Step 4: Process soil quality using list comprehension and max balance
    soil_scores = [nutrient_balance(zone) for zone in soils]
    best_soil_score = max(soil_scores)
    avg_soil_score = sum(soil_scores) / len(soil_scores)
    
    # Step 5: Combine factors with nonlinear interaction
    base_yield = 5000 * temp_factor * water_factor * (0.3 * avg_soil_score + 0.7 * best_soil_score)
    
    # Step 6: Apply diminishing returns via logarithmic cap
    adjusted_yield = base_yield * (math.log(base_yield + 1) / (base_yield / 1000)) if base_yield > 0 else 0
    
    # Step 7: Phantom correction using unused noise (never applied)
    noise_correction = generate_noise(len(soils))  # computed but unused
    entropy_check = calculate_entropy([int(s*100)%10 for s in soil_scores])  # irrelevant metric
    
    # Step 8: Final calibration with fixed offset
    final_output = int(adjusted_yield - 250 + 50 * entropy_check)
    
    return final_output

# Critical execution point
final_yield = optimize_harvest(climate_data, soil_profiles)

# Output target result
print(f"Target result: {final_yield}")