def analyze_growth_cycle(data, base):
    total = 0
    temp_offset = 0
    for item in data:
        if len(item) > 3:
            val = sum([ord(c) - ord('a') for c in item[:3]])
            total += val * 2
    return total

field_data = ['wheat', 'corn', 'barley', 'oats', 'rice']
threshold = 4

# Irrelevant helper function with dead logic
def validate_crop_code(code):
    if code.startswith('C') and code.isalpha():
        return False
    elif code.isdigit():
        return int(code) > 100
    return True

# Distractor variables
buffer_zone = [x.upper() for x in field_data if x.endswith('s')]
dummy_sum = sum(len(word) for word in buffer_zone)

soil_ph_levels = {'wheat': 6.5, 'corn': 6.0, 'barley': 6.8, 'oats': 6.2, 'rice': 5.5}
ph_correction_factor = 0
for crop, ph in soil_ph_levels.items():
    if ph < 6.0:
        ph_correction_factor += 0.3
    elif ph > 6.7:
        ph_correction_factor -= 0.2

# Simulate intermediate processing with red herring calculation
running_metric = 0
for i in range(len(field_data)):
    running_metric += len(field_data[i]) * (i + 1)

# Actual relevant logic hidden among distractions
base_productivity = analyze_growth_cycle(field_data, threshold)
scaled_input = base_productivity // threshold

adjustment = 0
for char in field_data[0]:
    if char in 'aeiou':
        adjustment += 1

# Key computation path
def calculate_harvest_efficiency(entries, limit):
    cumulative = 0
    penalty = 0
    for entry in entries:
        if len(entry) >= limit:
            # Use string method: count
            vowel_count = entry.count('a') + entry.count('e') + entry.count('i') + entry.count('o') + entry.count('u')
            cumulative += vowel_count * 10
        else:
            cumulative += len(entry)
    # Secondary factor: number of long-named crops
    long_names = [e for e in entries if len(e) > 4]
    bonus = len(long_names) * 3
    return cumulative + bonus - penalty

interim_check = dummy_sum * ph_correction_factor

final_yield = calculate_harvest_efficiency(field_data, threshold)

print(f"Result: {final_yield}")