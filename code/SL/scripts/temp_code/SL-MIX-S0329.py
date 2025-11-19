from collections import defaultdict
import math

def process_signal_strength(readings):
    adjusted_readings = []
    for db_level in readings:
        if db_level > 0 and math.log(db_level) >= 1.0:
            adjusted_readings.append(math.log(db_level) * 10)
        else:
            adjusted_readings.append(0.0)
    return adjusted_readings

signal_data = [0.5, 2.7, 10.0, 0.0, 15.3, -2.1]
filtered_signals = process_signal_strength(signal_data)
species_count = defaultdict(int)

bio_activity_score = 0.0
for idx, sig in enumerate(filtered_signals):
    species_id = idx % 3
    if sig > 0.0 and (species_id == 0 or species_count[species_id] <= 2):
        species_count[species_id] += 1
        bio_activity_score += sig * (1.5 if species_id == 0 else 1.2)
    elif sig == 0.0:
        continue

print(f"Result: {round(bio_activity_score, 2)}")