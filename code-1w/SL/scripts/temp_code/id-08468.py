def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence.lower() if c in 'aeiou')
    total_chars = len(sequence)
    reverse_seq = sequence[::-1]
    is_palindrome = sequence.lower() == reverse_seq.lower()
    
    # Irrelevant analysis branch (dead logic path)
    if 'xyz' in sequence:
        magic_offset = 999
    else:
        magic_offset = 0
    
    normalized = count_vowels / max(total_chars, 1)
    return int(normalized * 100)


def track_metrics(data_stream):
    readings = []
    temp_buffer = []
    for item in data_stream:
        if isinstance(item, str):
            processed = len(item.strip())
            readings.append(processed)
            temp_buffer.append(processed * 2)  # Unused buffer
    average_length = sum(readings) / len(readings) if readings else 0
    return average_length

# Simulate system diagnostics
status_log = ['active', 'idle', 'active', 'standby']
activation_flags = [1 if s == 'active' else 0 for s in status_log]
active_duration = sum(activation_flags) * 15  # 15-minute intervals

# Core computation with distractions
raw_input = "ElectrostaticChargeBalance"
diagnostic_code = "ESC-7X"

charge_count = len([c for c in raw_input if c.isupper()])
efficiency_ratio = analyze_pattern(raw_input)

# Distractor: fake checksum calculation (not used)
fake_checksum = 0
for i, c in enumerate(diagnostic_code):
    fake_checksum += ord(c) * (i + 1)
fake_checksum = fake_checksum % 97

# Another red herring: recursive character counter (semi-relevant)
def count_consonants(s, index=0):
    if index >= len(s):
        return 0
    char = s[index].lower()
    is_consonant = char.isalpha() and char not in 'aeiou'
    return (1 if is_consonant else 0) + count_consonants(s, index + 1)

consonant_total = count_consonants(raw_input)

# Real logic path begins
baseline = track_metrics(['test', 'data', 'entry'])
adjustment_factor = efficiency_ratio / 100.0
interim_value = charge_count * adjustment_factor * 12.5

# Final evaluation with nested conditionals
if efficiency_ratio > 40:
    bonus_multiplier = 1.8
else:
    bonus_multiplier = 1.2

if consonant_total > 10:
    penalty = 5
else:
    penalty = 2

adjusted_interim = interim_value + (bonus_multiplier * active_duration)

# Key statement
final_score = evaluate_performance(charge_count, efficiency_ratio)

# Supporting function defined late (increases cognitive load)
def evaluate_performance(count, ratio):
    base = count * ratio
    if ratio >= 50:
        quality_bonus = 20
    elif ratio >= 30:
        quality_bonus = 10
    else:
        quality_bonus = 0
    return int(base + quality_bonus - penalty)

print(f"Result: {final_score}")