def analyze_pattern(sequence):
    count = 0
    for char in sequence:
        if char.isdigit():
            count += int(char) % 3
    return count

sequence = 'x7y2z9p4q'

# Irrelevant transformation chain
transformed = ''.join([c.upper() if c.isalpha() else c for c in sequence[::-1]])
shadow_value = sum([ord(c) for c in transformed if c.isalpha()]) // len(transformed)

base_load = len(sequence) * 2
stress_factor = analyze_pattern(sequence)

# Distractor: complex-looking but unused calculation
auxiliary_metric = (shadow_value * base_load) >> 2
temp_offset = 0
for i in range(3):
    temp_offset += (stress_factor + i) ** 2

# Real logic embedded with noise
adjustments = [i * stress_factor for i in range(1, 4)]
net_correction = sum(adjustments) // base_load

if net_correction > 5:
    scaling = 1.5
else:
    scaling = 2.0  # This will be used

interim = (base_load + stress_factor) * scaling
final_load = int(interim - (net_correction * 1.5))

# Dead code path (never reached due to logic)
if False:
    final_load *= 2
    final_load += shadow_value

# Print required result
Result: final_load