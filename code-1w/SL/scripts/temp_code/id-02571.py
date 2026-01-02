from collections import defaultdict, Counter
import math

# Simulated agricultural dataset with multiple crop types and growth phases
def load_fake_crop_dataset():
    data = [
        ('wheat', 'phase1', 120), ('wheat', 'phase2', 135), ('wheat', 'phase3', 140),
        ('corn', 'phase1', 95), ('corn', 'phase2', 110), ('corn', 'phase3', 105),
        ('rice', 'phase1', 100), ('rice', 'phase2', 115), ('rice', 'phase3', 125),
        ('barley', 'phase1', 80), ('barley', 'phase2', 85), ('barley', 'phase3', 90)
    ]
    return data

# Misleading auxiliary function – never used in main logic
def compute_thermal_index(temps):
    acc = 0
    for t in temps:
        if t > 25:
            acc += (t - 25) * 1.5
        else:
            acc -= (25 - t) * 0.5
    return acc / len(temps) if temps else 0

# Another red herring: complex soil pH adjustment model (unused)
class SoilPHModel:
    def __init__(self):
        self.base = 7.0
    
    def adjust(self, organic_content, rainfall):
        delta = organic_content * 0.03 - rainfall * 0.02
        return self.base + delta

# Distractor list of environmental factors (partially used, mostly noise)
environmental_factors = {
    'temperature_avg': [22, 24, 26, 25, 23],
    'humidity': [60, 65, 70, 68, 62],
    'sunlight_hours': [8, 8.5, 9, 8.7, 8.2],
    'wind_speed': [12, 14, 10, 13, 11]
}

# Fake preprocessing that looks important but only used once
processed_env = {k: sum(v) / len(v) for k, v in environmental_factors.items()}
adjusted_ph = 6.8  # Hardcoded override - invalidates SoilPHModel

# Core data aggregation with defaultdict (relevant)
def aggregate_by_crop(data):
    result = defaultdict(list)
    for crop, phase, yield_val in data:
        result[crop].append(yield_val)
    return result

# Secondary transformation using enumerate and zip (key concept)
def align_growth_stages(crop_yields):
    aligned = {}
    for crop, yields in crop_yields.items():
        if len(yields) >= 3:
            # Use enumerate to track index and zip to pair with stage weights
            stage_weights = [0.3, 0.5, 0.7]
            weighted_sum = 0
            total_weight = 0
            for idx, (yield_val, weight) in enumerate(zip(yields[:3], stage_weights)):
                if idx == 1:
                    yield_val *= 1.05  # mid-phase boost
                weighted_sum += yield_val * weight
                total_weight += weight
            aligned[crop] = weighted_sum / total_weight
        else:
            aligned[crop] = sum(yields) / len(yields)
    return aligned

# Complex filtering with set operations (distractor-heavy)
def filter_outliers(yield_dict):
    all_values = list(yield_dict.values())
    mean = sum(all_values) / len(all_values)
    std_dev = (sum((x - mean)**2 for x in all_values) / len(all_values))**0.5
    
    # Define outlier bounds
    lower = mean - 1.5 * std_dev
    upper = mean + 1.5 * std_dev
    
    # Create sets for no real purpose (distraction)
    valid_set = {k for k, v in yield_dict.items() if lower <= v <= upper}
    outlier_set = set(yield_dict.keys()) - valid_set
    temp_copy = dict(yield_dict)
    
    # Remove outliers (but this version doesn't actually change anything - dead path)
    for key in outlier_set:
        if 'w' in key:  # Never true in current data
            del temp_copy[key]
    
    return yield_dict  # Original unchanged

# Main calculation with conditional complexity
def calculate_optimal_yield(data, cycles):
    # Real pipeline starts here
    grouped = aggregate_by_crop(data)
    normalized = align_growth_stages(grouped)
    
    # Apply cycle-based decay factor (relevant)
    decayed = {}
    for crop, val in normalized.items():
        decay_factor = 1
        for i in range(cycles):
            decay_factor *= 0.97 + (i * 0.005)  # Diminishing returns
        decayed[crop] = val * decay_factor
    
    # Final fusion metric: harmonic mean (resistant to outliers)
    values = list(decayed.values())
    if not values:
        return 0
    reciprocal_sum = sum(1/v for v in values if v != 0)
    harmonic_mean = len(values) / reciprocal_sum
    
    # Artificial precision truncation (relevant final step)
    return round(harmonic_mean * 1.08, 4)  # Market adjustment factor

# Unused statistical summary (distractor)
def generate_crop_report(data):
    crop_names = [item[0] for item in data]
    counter = Counter(crop_names)
    report = {}
    for name, count in counter.items():
        report[name] = {'count': count, 'efficiency': round(count * 0.76, 2)}
    return report

# Irrelevant bit manipulation routine (red herring)
def encode_crop_id(name):
    encoded = 0
    for char in name:
        encoded ^= ord(char)
        encoded = (encoded << 1) | (encoded >> 7)
        encoded &= 0xFF
    return encoded

# Global constants with misleading names
total_phase_count = 12  # Unused
max_canopy_cover = 0.88  # Unused
baseline_evapotranspiration = 3.4  # Unused

# Simulated growth cycles (input parameter)
growth_cycles = 6

# Load and preprocess real data
raw_data = load_fake_crop_dataset()

# Execute fake preprocessing (has side effect of looking necessary)
fake_summary_stats = []
for env_key, vals in environmental_factors.items():
    fake_summary_stats.append(max(vals) - min(vals))

# Begin core computation
harvest_data = raw_data

# Key statement
final_yield = calculate_optimal_yield(harvest_data, growth_cycles)

print(f"Result: {final_yield}")