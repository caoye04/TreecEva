def analyze_temperature_trends(raw_readings):
    daily_averages = {}
    temp_sum = 0
    count = 0
    outlier_threshold = 50
    adjusted_values = []

    for reading in raw_readings:
        if reading < outlier_threshold:
            temp_sum += reading
            count += 1
            adjusted_values.append(reading + 2)

    daily_averages['avg'] = temp_sum / count if count > 0 else 0

    scaled_adjusted = [val * 1.1 for val in adjusted_values]
    return scaled_adjusted, daily_averages


def transform_codes(char_codes):
    encoded = []
    buffer = []
    for code in char_codes:
        if code.isalpha():
            buffer.append(ord(code.upper()) - ord('A') + 1)
    transformed = [num * 2 for num in buffer]
    return transformed


def compute_modular_weights(values, modulus=7):
    weights = []
    total_weight = 0
    for i, val in enumerate(values):
        weight = (val % modulus) * (i + 1)
        weights.append(weight)
        total_weight += weight
    return total_weight


def calculate_final_score(data_packet):
    base_score = data_packet.get('base', 0)
    modifier = data_packet.get('mod', 1)
    penalty = data_packet.get('penalty', 0)
    bonus_list = data_packet.get('bonuses', [])

    intermediate = base_score * modifier
    bonus_total = sum(b for b in bonus_list if b > 5)  
    final_score = (intermediate - penalty) + bonus_total
    return final_score

# Simulated sensor data and metadata
sensor_readings = [23, 45, 67, 12, 34, 56, 89, 10, 22]
category_codes = ['X', 'Y', 'Z', 'A', 'B']

# Step 1: Process temperature data
adjusted_data, stats = analyze_temperature_trends(sensor_readings)
smoothing_factor = 0.9
filtered_data = [x * smoothing_factor for x in adjusted_data]

# Step 2: Irrelevant transformation on codes
digit_sequence = transform_codes(category_codes)
sum_digits = sum(digit_sequence)
placeholder_calc = sum_digits * 2 - 5

# Step 3: Compute modular contribution
mod_result = compute_modular_weights(adjusted_data, modulus=7)

# Step 4: Prepare data packet for scoring
processed_data = {
    'base': int(stats['avg']),
    'mod': len(digit_sequence) % 4 + 1,
    'penalty': mod_result // 10,
    'bonuses': [8, 3, 12, 5, 7]
}

# Key execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")