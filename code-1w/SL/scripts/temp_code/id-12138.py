import math

# Simulate agricultural yield optimization under varying conditions
def preprocess_sensor_readings(data):
    """Apply smoothing and outlier removal (distractor)"""
    smoothed = [x + 0.1 for x in data if x > 0]
    return [x * 0.95 for x in smoothed]

# Irrelevant function - simulates drone flight path (dead code)
def calculate_flight_efficiency(coordinates):
    total = 0
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        total += math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return total * 0.78

drone_route = [(0,0), (10,5), (20,10), (30,0)]
efficiency_score = calculate_flight_efficiency(drone_route)  # Red herring

# Soil pH adjustment logic (partially relevant)
base_ph_shift = 0.3
temperature_factor = lambda temp: 1.0 + (temp - 25) * 0.02 if temp > 20 else 0.9

# Environmental stress index calculator (misleading intermediate)
def compute_stress_index(values):
    mean_val = sum(values) / len(values)
    deviations = [(v - mean_val)**2 for v in values]
    variance = sum(deviations) / len(deviations)
    return math.sqrt(variance) * 10

# Core crop yield model
max_capacity = 9876.54
decay_rate = 0.01

# Actual yield prediction kernel
def simulate_growth_cycle(days, base_yield, stress_tol):
    yield_progress = []
    current = base_yield
    for day in range(1, days+1):
        stress_mod = 1 - (compute_stress_index([day % 7, day % 5]) / 100)
        temp_mod = temperature_factor(22 + (day % 30) * 0.5)
        current *= (1 + decay_rate * stress_mod * temp_mod)
        if day % 10 == 0:
            current -= 0.5  # Watering penalty
        yield_progress.append(current)
    return yield_progress

# Data inputs
climate_data = [23, 25, 27, 26, 30, 32, 31, 29, 28, 27]  # Daily temps (°C)
soil_conditions = [6.2, 6.4, 6.3, 6.5, 6.1, 6.0, 6.2, 6.3, 6.4, 6.2]  # pH levels
sensor_noise = [-0.1, 0.2, -0.3, 0.1, 0.0, 0.2, -0.2, 0.1, 0.3, -0.1]

# Process raw sensor data (distractor chain)
noisy_ph = [ph + noise for ph, noise in zip(soil_conditions, sensor_noise)]
cleaned_ph = preprocess_sensor_readings(noisy_ph)

# Phantom irrigation system log (irrelevant structure)
irrigation_log = {
    'zones': 5,
    'schedule': ['06:00', '18:00'],
    'duration_mins': [15, 12, 18, 14, 16],
    'pressure_psi': 45.6
}

total_water_flow = 0
for dur in irrigation_log['duration_mins']:
    total_water_flow += dur * irrigation_log['pressure_psi'] * 0.01

# Hidden calculation: effective growing degree days
def calc_gdd(temps, base=10):
    return sum(max(0, t - base) for t in temps)

gdd = calc_gdd(climate_data)
scaling_factor = gdd / 200.0  # Normalize to expected season length

# Main optimization algorithm
initial_estimate = max_capacity * 0.65
interim_results = []

for i in range(len(climate_data)):
    adj_factor = scaling_factor * (1 + (cleaned_ph[i % len(cleaned_ph)] - 6.2) * 0.1)
    adjusted = initial_estimate * adj_factor
n    interim_results.append(adjusted)

# Final integration using growth simulation
raw_projection = simulate_growth_cycle(100, 5000, 0.85)
projection_peak = max(raw_projection)
average_ph = sum(soil_conditions) / len(soil_conditions)

# Key computation with distractors
buffer_adjustment = (average_ph - 6.2) * 100
legacy_offset = math.sin(math.pi / 6) * 500  # Obsolete calibration (red herring)

target_baseline = projection_peak * (scaling_factor + 0.1)
penalty_mask = [1 for x in climate_data if x > 30]
extreme_days_penalty = len(penalty_mask) * 200

# Final yield optimization
final_yield = target_baseline - extreme_days_penalty + buffer_adjustment

# Output result
Result: {final_yield}