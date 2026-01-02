def calculate_humidity_score(readings):
    total_humidity_index = 0
    for i, (temp, hum) in enumerate(zip(readings['temperatures'], readings['humidity_levels'])):
        adjustment = 1.5 if temp > 25 else 0.8
        score = hum * adjustment
        total_humidity_index += score if score > 10 else 10
    return total_humidity_index

readings = {
    'temperatures': [22, 26, 30, 19],
    'humidity_levels': [12, 15, 8, 20]
}

# Irrelevant auxiliary variable (minimal distraction)
dummy_flag = len(readings['temperatures']) > 3

total_humidity_index = calculate_humidity_score(readings)
print(f"Result: {total_humidity_index}")