def analyze_text(pattern, data):
    count = 0
    for char in data:
        if char.lower() in pattern:
            count += 1
    return count

extra_data = 'abcdefghijk'
dummy_sum = sum([i for i in range(4) if i % 2 == 0])

baseline = {'threshold': 5, 'weight': 0.8}
raw_input = "Xylophone melody echoes beautifully"

# Process character frequency based on vowels
vowel_set = 'aeiou'
vowel_count = analyze_text(vowel_set, raw_input)
consonant_count = len(raw_input) - vowel_count - raw_input.count(' ')

# Dummy processing with string methods
trimmed = raw_input.strip().replace(' ', '').upper()
reversed_part = trimmed[::-1]
mid_section = trimmed[2:7]

# Secondary distraction: counting specific letter patterns
letter_z_score = 0
for c in raw_input.lower():
    if c > 'm':
        letter_z_score += 1

# Real metric computation begins
metrics = {
    'length': len(trimmed),
    'vowels': vowel_count,
    'balance': consonant_count - vowel_count,
    'entropy': (vowel_count + 1) / (consonant_count + 1)
}

# Misleading recursive function (unused)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n - 2)

# Another red herring: complex loop with no impact
temp_result = 0
for i in range(3):
    for j in range(2):
        temp_result += i * j
        if temp_result > 10:
            break

# Core logic nested in helper function
def evaluate_performance(data, config):
    score = 0
    if data['length'] > config['threshold']:
        score += data['vowels'] * config['weight']
    if data['balance'] >= 0:
        score += 5
    # Final adjustment using entropy and string length ratio
    adjustment = (data['entropy'] * data['length']) / 10
    score += adjustment
    return int(score)

final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")