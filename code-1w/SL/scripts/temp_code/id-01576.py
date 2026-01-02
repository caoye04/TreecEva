def analyze_text_pattern(s):
    # Irrelevant helper function – dead end
    return sum(1 for c in s if c.isupper())

# Irrelevant data structures
text_corpus = ['Alpha', 'BetaTest', 'GammaReport', 'DeltaForce']
unused_matrix = [[i * j for j in range(5)] for i in range(5)]
phantom_counter = 0

# Distractor variables with plausible but unused computations
baseline_shift = 3.14159
normalization_factor = len(text_corpus) * 2
dummy_offset = sum(ord(w[0]) for w in text_corpus) % 100

# Real data involved in actual computation
base_score = 87
modifiers = [-5, 3, 0, 7, -12]
penalty_threshold = 4

# Simulated environmental conditions – mostly irrelevant
env_conditions = {
    'humidity': 68,
    'temperature': 22,
    'soil_ph': 6.4,
    'light_exposure': 'partial'
}

# Unused transformation chain
transformed_data = []
for item in text_corpus:
    transformed = item.lower().replace('a', '@').title()
    transformed_data.append(transformed)

# Fake scoring model – looks important but unused
intermediate_scores = {}
for idx, word in enumerate(text_corpus):
    score = len(word) * (idx + 1)
    intermediate_scores[word] = score + dummy_offset

# Decoy function that computes something similar but not used
def calculate_fallback_yield(score, factors):
    result = score
    for f in factors:
        if f > 0:
            result += f * 1.5
        else:
            result -= abs(f) * 0.7
    return int(result)

# Actual core logic buried in distractions
def apply_modifiers(value, mod_list):
    temp = value
    adjustment_log = []
    for mod in mod_list:
        if mod == 0:
            continue
        elif mod > penalty_threshold:
            temp += mod * 0.8  # bonus scaling
        elif mod < 0:
            reduction = abs(mod) ** 0.5
            temp -= reduction
        else:
            temp -= 1
        adjustment_log.append(temp)
    
    # Character counting in a string representation as secondary logic
    log_str = ''.join([str(int(x)) for x in adjustment_log])
    extra_penalty = len([c for c in log_str if c == '7']) * 1.5  # count digit '7'
    return temp - extra_penalty

# Another red herring: uses string methods but leads nowhere
def generate_diagnostic_tag(data_list):
    tag_parts = []
    for entry in data_list:
        if len(entry) > 4:
            tag_parts.append(entry[1:3].upper())
    return ''.join(tag_parts)

diag_tag = generate_diagnostic_tag(text_corpus)

# Critical function that determines the answer
def evaluate_harvest_quality(score, adjustments):
    initial = apply_modifiers(score, adjustments)
    
    # String-based interference check
    control_flag = "pass" if initial > 70 else "fail"
    flag_chars = [c for c in control_flag]
    
    # Final adjustment based on character length of flag (trivial but hidden)
    final_value = initial - len(flag_chars)
    
    # Insertion of irrelevant string method chain
    padded_flag = control_flag.center(10, '*')
    cleaned = padded_flag.strip('*')
    
    # This print is just to mislead – not related to answer
    if cleaned == "pass":
        phantom_counter += 1  # never accessed again

    return final_value

# Execution point of interest
final_yield = evaluate_harvest_quality(base_score, modifiers)
print(f"Result: {final_yield}")