def analyze_temperatures(temp_list):
    avg_temp = sum(temp_list) / len(temp_list)
    above_avg_count = 0
    for temp in temp_list:
        if temp > avg_temp:
            above_avg_count += 1
    return avg_temp, above_avg_count


def encode_sequence(seq):
    encoded = []
    for i, char in enumerate(seq):
        encoded.append(ord(char) ^ (i + 1))
    return encoded


def calculate_final_score(data):
    base_score = 0
    bonus = 0
    penalty = 0

    # Extract temperature and sequence from data
    temps = data['temperatures']
    seq = data['sequence']

    # Real computation path: analyze temperatures
    avg, high_count = analyze_temperatures(temps)
    base_score += avg * 10

    # Distraction: string manipulation that doesn't affect final score
    reversed_seq = ''.join(reversed(seq))
    normalized = reversed_seq.lower().strip()
    words = normalized.split(' ')
    word_count = len(words)

    # Another distraction: encoding sequence (not used in final score)
    encoded_chars = encode_sequence(seq)
    total_encoded = sum(encoded_chars)

    # Real logic continues: use high_count for bonus
    if high_count > 3:
        bonus += 25
    else:
        bonus += 10

    # Bitwise operation relevant to final score
    adjustment_factor = len(seq) & 7  # Use bitwise AND
    base_score += adjustment_factor

    # Distractor: unused loop with zip and enumerate
    cumulative = 0
    for idx, (a, b) in enumerate(zip(temps, temps[1:])):
        diff = abs(a - b)
        cumulative += diff * (idx + 1)

    # Final score calculation
    final_score = base_score + bonus - penalty  # penalty remains 0
    return final_score

# Setup input data
raw_sequence = "XyZ@AbC!"
data_input = {
    'temperatures': [23, 18, 31, 27, 29, 16],
    'sequence': raw_sequence
}

# Preprocessing step with distractors
processed_chars = []
for c in raw_sequence:
    if c.isalpha():
        processed_chars.append(c.lower())
status_map = {i: chr(97 + i) for i in range(len(processed_chars))}

# Actual processing begins here
intermediate_result = analyze_temperatures(data_input['temperatures'])
processed_data = data_input.copy()

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")