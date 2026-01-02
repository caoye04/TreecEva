sensors = {'temp': 23.5, 'humid': 68, 'press': 1013}

raw_data = [15, 27, 36, 44, 58]
temperature = int(sensors['temp'])
efficiency = 0.85 if temperature > 20 else 1.0

# Extract subset using slicing and compute average reading
subset = raw_data[1:4]
avg_reading = sum(subset) // len(subset)

# Conditional expression for mode selection
mode = 'high' if avg_reading > 30 else 'low'

# Key computational chain
baseline = 100 - (avg_reading % 7) * 3
pressure_adjustment = sensors['press'] // baseline

final_rating = efficiency * (temperature // 10)

print(f"Result: {pressure_adjustment}")