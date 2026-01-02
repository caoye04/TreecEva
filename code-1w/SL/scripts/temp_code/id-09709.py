def analyze_text_composition(text):
    char_count = len(text)
    upper_case = sum(1 for c in text if c.isupper())
    lower_case = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c == ' ')
    special = char_count - upper_case - lower_case - digits - spaces

    composition = {
        'letters': upper_case + lower_case,
        'digits': digits,
        'whitespace': spaces,
        'special': special
    }
    return composition


def transform_data(raw):
    shifted = [(x * 2 + 1) % 256 for x in raw]
    inverted = [255 - val for val in shifted]
    reshaped = [inverted[i:i+4] for i in range(0, len(inverted), 4)]
    transposed = list(zip(*reshaped))[:len(reshaped[0])] if reshaped else []
    return transposed

# Irrelevant transformation chain (dead path)
def obsolete_processing(x):
    if x < 10:
        return x ** 3 + 2 * x
    elif x < 100:
        return (x // 3) * (x % 7)
    else:
        return sum(i * (x % i) for i in range(2, 10))

# Unused helper
def get_frequency_map(seq):
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    sorted_keys = sorted(freq.keys())
    return {k: freq[k] for k in sorted_keys}

# Distractor variables
temp_buffer = [i ** 2 - 3*i + 5 for i in range(15)]
lookup_table = {i: (i * 7 + 13) % 101 for i in range(20)}
metadata_cache = {'version': '2.1.5', 'schema': 'alpha', 'active': False}

# Core logic disguised among noise
def compute_hash_chain(seed, rounds=8):
    value = seed % 97
    history = []
    for i in range(rounds):
        if i % 3 == 0:
            value = (value * 17 + 23) % 97
        elif i % 3 == 1:
            value = (value * 29 + 19) % 97
        else:
            value = (value * 11 + 47) % 97
        history.append(value)
    return history[-1] if history else value

# Main evaluation engine
def evaluate_metrics(data_dict):
    base = data_dict.get('letters', 0)
    num_chars = sum(data_dict.values())
    ratio = base / num_chars if num_chars > 0 else 0
    penalty = data_dict.get('special', 0) * 0.3
    bonus = data_dict.get('digits', 0) * 0.1
    return (ratio * 100) - penalty + bonus

weights = {'A': 0.4, 'B': 0.3, 'C': 0.2, 'D': 0.1}

# Critical red herring calculation
counterfeit_result = 0
for key, val in weights.items():
    counterfeit_result += ord(key) * val

def evaluate_performance(metrics, weight_map):
    # Real computation buried here
    score_A = metrics.get('letters', 0) * weight_map['A']
    score_B = compute_hash_chain(metrics.get('digits', 0)) * weight_map['B']
    score_C = (metrics.get('whitespace', 0) > 5) * 10 * weight_map['C']  
    score_D = len(str(metrics.get('special', 0))) * 5 * weight_map['D']
    
    # Dummy intermediate
    temp_debug = [score_A * 0.1, score_B * 0.2, score_C * 0.3]
    
    final_score = score_A + score_B + score_C + score_D
    
    # More distraction
    audit_log = f'Scores computed: A={score_A}, B={score_B}, C={score_C}, D={score_D}'
    debug_snapshot = {'timestamp': 1678886400, 'user': 'sysadmin', 'final_score': final_score * 0.95}
    
    return int(final_score)

# Trigger execution
input_text = "SecurePass123!@#"
composition = analyze_text_composition(input_text)
final_score = evaluate_performance(composition, weights)
print(f"Target result: {final_score}")