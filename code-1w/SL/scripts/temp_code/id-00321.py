def analyze_text(s):
    return {c: s.count(c) for c in set(s) if c.isalpha()}

# Irrelevant helper function (dead utility)
def normalize_case(text):
    return text.lower().replace(' ', '_')

# Misleading data initialization
temp_log = [0] * 15
backup_buffer = list(range(8, 20))
offset_correction = sum([i * 0.5 for i in range(4)])  # Unused distraction

# Core problem variables
raw_input = "DataScienceAndMachineLearning"
char_freq = analyze_text(raw_input)

# Distractor: complex but unused transformation chain
transform_chain = lambda x: x.upper()[::-1].replace('A', 'X')
processed_shadow = transform_chain(raw_input)

# Actual relevant data structures
metrics = [
    len(raw_input),
    len(char_freq),
    sum(1 for c in raw_input if c in 'aeiouAEIOU'),
    raw_input.count('e')
]

# Unused metric red herring
rare_count = sum(1 for k, v in char_freq.items() if v == 1)

weights = [0.4, 0.3, 0.2, 0.1]  # Importance coefficients

# Another dead path: slicing with no effect
tail_slice = raw_input[10:15:2]
dummy_set = set(tail_slice).union({'X', 'Y'}).difference({'a'})

# Key computation hidden among distractions
def evaluate_performance(m, w):
    adjusted = [m[i] * w[i] for i in range(len(m))]
    penalty = 0
    if m[1] > 20:  # Never true
        penalty = 5
    elif m[0] > 25:  # Also false
        penalty = 3
    return sum(adjusted) - penalty

# Secondary distractor: bit manipulation with no impact
event_flag = 0b10101
shifted_mask = (event_flag << 3) & 0b1111000
flag_check = shifted_mask | 0b1100

# State tracking with irrelevant accumulation
counter_log = []
for i in range(1, 6):
    counter_log.append(i ** 2 + offset_correction)

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Final output
print(f"Result: {final_score}")