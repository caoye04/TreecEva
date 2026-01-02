def analyze_growth_rate(conditions):
    base = conditions[0] * 0.5
    modifier = 0
    for i in range(1, len(conditions)):
        if conditions[i] > 70:
            modifier += 1.2
        elif conditions[i] > 50:
            modifier += 0.5
        else:
            modifier -= 0.3
    return base + modifier

# Irrelevant weather scoring function (dead code path)
def calculate_weather_score(temp, humidity):
    score = 0
    if temp > 30:
        score += 10
    if humidity < 40:
        score -= 5
    return score  # Never used

# Distractor: unused crop simulation
class CropModel:
    def __init__(self, name):
        self.name = name
        self.yield_potential = 0

    def predict(self, data):
        return sum(data) / len(data) * 2

# Unused global variables (distractors)
optimal_temp_range = (18, 27)
soil_ph_levels = [6.1, 6.3, 6.7, 6.9, 7.0]
unused_interpolation_factor = 0.87

# Real processing begins here
def preprocess_sensor_array(raw_input):
    filtered = [x for x in raw_input if 20 <= x <= 100]  # List comprehension
    smoothed = filtered[1:-1]  # Slicing: remove first and last
    return [val * 1.1 for val in smoothed]

# Complex multi-step transformation with red herrings
def evaluate_stress_factors(data, threshold=60):
    stress_flags = []
    cumulative = 0
    peak_count = 0
    for idx, val in enumerate(data):
        if val < threshold:
            stress_flags.append(idx)
            cumulative += threshold - val
        if val == max(data) and idx != 0 and idx != len(data)-1:
            peak_count += 1
    
    # Decoy computation
    phantom_risk_score = len(stress_flags) * cumulative / (peak_count + 1) if peak_count else 0
    
    # Actual return value buried among distractions
    return len(stress_flags) + (cumulative * 0.1)

# Core logic with nesting and multiple concepts
def optimize_harvest(environmental_readings, cycle):
    processed = preprocess_sensor_array(environmental_readings)
    
    # Simulate multiple growth cycles (only one matters)
    trial_yields = []
    for c in range(1, 5):
        if c == cycle:
            rate = analyze_growth_rate(processed)
            stress_penalty = evaluate_stress_factors(processed)
            raw_yield = rate * 100 - stress_penalty * 5
            
            # Secondary adjustment
            adjustments = []
            for reading in processed[:len(processed)//2]:  # Slicing
                if reading > 65:
                    adjustments.append(reading * 0.05)
            net_adjustment = sum(adjustments)
            
            # Final calculation
            final_yield = raw_yield + net_adjustment
            
            # Dead code - looks important but unused
            verification_checksum = int(final_yield % 17)
            if verification_checksum > 10:
                verification_checksum //= 2
            
            trial_yields.append(final_yield)
        else:
            # Fake cycles doing complex but irrelevant work
            fake_rate = sum([x**0.5 for x in processed]) / len(processed)
            fake_penalty = len([x for x in processed if x < 40])
            trial_yields.append(fake_rate - fake_penalty)
    
    return trial_yields[-1] if trial_yields else 0

# Main execution flow
if __name__ == "__main__":
    # Real input data
    climate_data = [25, 30, 75, 85, 45, 90, 60, 40, 80, 70, 35]
    
    # Irrelevant initialization
    model_a = CropModel("Tomato")
    model_b = CropModel("Wheat")
    prediction_grid = [[0 for _ in range(5)] for _ in range(5)]
    
    # Key statement
    final_yield = optimize_harvest(climate_data, 3)
    print(f"Result: {final_yield}")