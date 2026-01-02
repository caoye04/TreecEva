from collections import defaultdict, Counter

# Simulate sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 25.0, 22.7, 20.3, 24.9, 26.1, 23.8, 21.5]
humidity_readings = [45, 48, 55, 43, 50, 60, 47, 44, 52, 58]
co2_levels = [410, 415, 430, 405, 420, 440, 412, 408, 425, 435]

# Irrelevant auxiliary data (distractor)
sound_decibels = [32, 35, 30, 33, 36, 29, 31, 34, 33, 30]
lux_levels = [500, 480, 510, 490, 505, 495, 515, 485, 520, 475]

# Process relevant environmental metrics
def process_temperature(temps):
    temp_stats = defaultdict(float)
    temp_stats['avg'] = sum(temps) / len(temps)
    temp_stats['deviations'] = [abs(t - temp_stats['avg']) for t in temps]
    temp_stats['stability_index'] = 100 - (sum(temp_stats['deviations']) / len(temps))
    return temp_stats

def analyze_humidity(humidities):
    count_by_level = Counter()
    for h in humidities:
        if h < 50:
            count_by_level['low'] += 1
        elif h < 60:
            count_by_level['moderate'] += 1
        else:
            count_by_level['high'] += 1
    return count_by_level

# Misleading function that computes unrelated metric (dead code path)
def compute_noise_pollution(sound_data):
    weighted_avg = sum(s * 1.2 for s in sound_data if s > 32)
    return weighted_avg // len(sound_data)

# Main processing pipeline
temp_analysis = process_temperature(temperature_readings)
humidity_distribution = analyze_humidity(humidity_readings)

# Simulated air quality score based on CO2 (primary contributor)
base_co2_score = sum(450 - c for c in co2_levels if c < 450)
adjusted_co2_score = base_co2_score * 0.8

# Auxiliary stability contribution
stability_bonus = temp_analysis['stability_index'] * 0.5

# Dummy transformation (irrelevant but looks important)
decibel_summary = {"total": sum(lux_levels), "peak": max(lux_levels)}

# Actual score calculation depends only on adjusted_co2_score and stability_bonus
final_score = 0
final_score += adjusted_co2_score
final_score += stability_bonus

# Critical execution point
final_score = int(final_score)

# Output result
print(f"Result: {final_score}")