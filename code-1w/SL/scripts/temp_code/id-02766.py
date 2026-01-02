def analyze_readings(readings):
    filtered = [r for r in readings if r > 0]
    avg = sum(filtered) / len(filtered) if filtered else 0
    normalized = [round(r / avg, 2) for r in filtered]
    return normalized

readings = [12, -5, 23, 0, 34, -1, 18, 22]
distances = [abs(x - 15) for x in readings]  # distractor: not used later
temp_stats = {'min': min(readings), 'max': max(readings)}  # semi-relevant

processed_data = analyze_readings(readings)

# Additional processing with red herring variables
even_elements = [x for x in processed_data if x % 2 == 0]
scaling_factor = 1.5  # misleading variable, not used
offset = 10  # unused offset, adds distraction

status_flags = []
for val in processed_data:
    if val > 1.5:
        status_flags.append(1)
    elif val < 0.5:
        status_flags.append(-1)
    else:
        status_flags.append(0)

flag_sum = sum(status_flags)  # intermediate metric, not critical

# Core logic embedded within noise
def calculate_final_score(data):
    base_score = sum(data)
    penalty = 0
    for i, v in enumerate(data):
        if v > 1.8:
            penalty += 0.5
    return int(base_score - penalty)

auxiliary_weights = [0.9, 1.1, 0.8, 1.2]  # dead code path
if len(processed_data) > 10:
    weighted = [a * b for a, b in zip(processed_data, auxiliary_weights)]

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")