from collections import defaultdict

def calculate_performance(base, data):
    stats = defaultdict(float)
    adjustments = []

    for idx, value in enumerate(data):
        deviation = abs(value - base)
        if deviation > 5:
            stats['outliers'] += 1
        stats['total_deviation'] += deviation
        adjustments.append(deviation * 0.8)

    avg_adjustment = sum(adjustments) / len(adjustments) if adjustments else 0
    performance = 100 - stats['total_deviation'] * 0.5 - stats['outliers'] * 2
    return round(performance, 2)

# Irrelevant helper (mild distraction)
def normalize_string(s):
    return s.strip().lower().replace(' ', '_')

baseline = 20
readings = [18, 22, 15, 27, 19, 21]

# Key computation step
temperature_offset = 3  # unused variable (minor distraction)
final_score = calculate_performance(baseline, readings)

print(f"Result: {final_score}")