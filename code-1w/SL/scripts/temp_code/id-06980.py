def analyze_trend(data, threshold):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append('up')
        elif data[i] < data[i-1]:
            trend.append('down')
        else:
            trend.append('same')
    direction_count = {'up': trend.count('up'), 'down': trend.count('down'), 'same': trend.count('same')}
    return direction_count['up'] - direction_count['down']

baseline = [30, 32, 35, 34, 36, 38, 37]
deflection = [1.2, 1.5, 1.3, 1.8, 1.6]
readings = [33, 36, 39, 35, 40, 42, 38, 41]

# Irrelevant transformation chain
temp_str = ''.join([chr(97 + (x % 26)) for x in baseline])
encoded = temp_str.upper().replace('A', 'X').strip('X')
length_check = len(encoded) * 2 if 'X' not in encoded else len(encoded)

# Dummy counters with partial use
counter_a = 0
counter_b = 0
for val in deflection:
    if val > 1.4:
        counter_a += 1
    else:
        counter_b += 1

# Misleading intermediate calculation
adjustment_factor = sum(deflection) / (counter_a or 1)
scaled_values = [round(x * adjustment_factor, 2) for x in baseline]

# Actual logic begins
net_trend = analyze_trend(readings, threshold=35)

# Simulate performance scoring
def calculate_performance(base, current):
    base_avg = sum(base) / len(base)
    current_avg = sum(current) / len(current)
    deviation = abs(current_avg - base_avg)
    
    # Use string method to simulate mode classification
    status_tag = "STABLE" if deviation < 5 else "FLUCTUATING"
    modifier = 1.2 if status_tag.lower().startswith('s') else 0.8
    
    # Secondary check using trend
    trend_boost = 5 if net_trend > 0 else -3
    
    # Distractor: unused nested logic
    if base_avg > 30:
        if current_avg > 40:
            for _ in range(2):
                pass  # Dead loop placeholder

    raw_score = (current_avg - base_avg) * modifier + trend_boost
    return int(raw_score)

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")