from collections import Counter

def process_temperatures(readings, limit):
    # Filter temperatures above threshold
    high_temps = [t for t in readings if t > limit]
    
    # Count occurrences of each temperature
    temp_counts = Counter(high_temps)
    
    # Compute aggregate score using bitwise and arithmetic ops
    score = 0
    for temp, count in temp_counts.items():
        score += (temp ^ count) + (temp >> 1)
    
    # Irrelevant auxiliary variable (minimal distraction)
    avg_temp = sum(readings) / len(readings) if readings else 0
    
    return score

# Input data
temps = [20, 25, 30, 25, 35, 30, 25, 40]
threshold = 28

result = process_temperatures(temps, threshold)
print(f"Result: {result}")