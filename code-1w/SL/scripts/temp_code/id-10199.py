def analyze_temperatures(temp_readings):
    adjusted = [t + 273.15 for t in temp_readings if t > -50]
    valid_range = {t for t in adjusted if 200 <= t <= 350}
    return sorted(valid_range)


def extract_signals(raw_signal):
    signal_clean = raw_signal.strip().replace(' ', '').lower()
    binary_seq = ''.join(['1' if c in 'aeiou' else '0' for c in signal_clean])
    return binary_seq


def decode_sequence(seq):
    chunks = [seq[i:i+8] for i in range(0, len(seq), 8)]
    numeric_values = []
    for chunk in chunks:
        if len(chunk) == 8:
            num = int(chunk, 2)
            if num % 2 == 0:
                numeric_values.append(num)
    return numeric_values


def calculate_final_score(data_list):
    base = sum(data_list)
    bonus = len(data_list) * 2
    penalty = 0
    for val in data_list:
        if val > 100:
            penalty += 5
    return base + bonus - penalty

# Simulated sensor input
sensor_log = "A3EiM9XuT2"  
raw_temperatures = [-30, -60, 0, 25, 120, -200, 50]

# Signal processing (distractor: string path)
signal_binary = extract_signals(sensor_log)
numeric_data = decode_sequence(signal_binary)

# Temperature analysis (core computation path)
processed_temps = analyze_temperatures(raw_temperatures)
converted_kelvin = [round(t, 2) for t in processed_temps]

# Irrelevant transformation (distractor)
doubled_temps = [t * 2 for t in converted_kelvin if t < 300]

# Key data for scoring
filtered_for_scoring = [int(t // 10) * 5 for t in converted_kelvin]

# Final computation
final_score = calculate_final_score(filtered_for_scoring)

# Dead code branch (distractor)
if len(numeric_data) > 10:
    final_score *= 2

print(f"Result: {final_score}")