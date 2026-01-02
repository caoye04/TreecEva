def preprocess_signal(data):
    # Irrelevant preprocessing (dead path)
    normalized = [x % 256 for x in data]
    filtered = [y for y in normalized if y > 10]
    return sum(filtered) // len(filtered) if filtered else 0

# Decoy function that looks important but is unused
def evaluate_entropy(sequence):
    entropy = 0
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    for count in freq_map.values():
        prob = count / len(sequence)
        entropy -= prob * (prob ** 0.5)  # Not actual entropy
    return round(entropy, 4)

# Another red herring: complex-looking but unused transformation
class SignalAmplifier:
    def __init__(self, gain):
        self.gain = gain
        self.history = []

    def amplify(self, value):
        boosted = value * self.gain
        self.history.append(boosted)
        return boosted ** 0.5

# Real logic starts here — subtle and buried among noise
logic_core = [3, 5, 7, 11, 13, 17, 19]
activation_sequence = [1, 0, 1, 1, 0, 1, 1]

# Misleading intermediate computation
baseline_offset = sum(x ** 2 for x in logic_core if x % 3 != 0) % 1000
offset_correction = baseline_offset >> 2

# Distractor: fake checksum
checksum = 0
for i, val in enumerate(logic_core):
    checksum ^= (val + i) & 255

# Simulated sensor drift (irrelevant)
sensor_drift = 0.0
for step in range(5):
    sensor_drift += (step * 0.1) if step % 2 == 0 else 0.05

# Actual key transformation chain (interleaved with noise)
weighted_sum = 0
for idx in range(len(logic_core)):
    if activation_sequence[idx]:
        contribution = logic_core[idx]
        # Bit manipulation relevant to final result
        contribution = (contribution ^ 5) & 15  # Mask to 4 bits after XOR
        weighted_sum += contribution * (idx + 1)

# Secondary logic: conditional expression determining multiplier
multiplier = 3 if sum(activation_sequence) > 4 else 7

# Tertiary logic: modular arithmetic dependency
mod_factor = (weighted_sum + 13) % 11
if mod_factor == 0:
    mod_factor = 5

# Hidden dependency: character-based switch
flag_char = 'G'
dynamic_adjustment = ord(flag_char) % 9  # 71 % 9 = 8

# Final computation buried under distractions
intermediate_result = (weighted_sum * multiplier) % 10000
final_diagnostic = (intermediate_result + mod_factor) * dynamic_adjustment

# Fake print statements to mislead
# print(f'Diagnostic: {evaluate_entropy(activation_sequence)}')
# print(f'Preprocessed signal: {preprocess_signal(logic_core)}')

Result: final_diagnostic