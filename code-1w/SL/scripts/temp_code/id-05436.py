def analyze_text(s):
    return {
        'upper': sum(1 for c in s if c.isupper()),
        'lower': sum(1 for c in s if c.islower()),
        'digits': sum(1 for c in s if c.isdigit()),
        'special': sum(1 for c in s if not c.isalnum())
    }

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    temp = 0
    for i in range(x):
        temp += i * (i - 1) // 2
    return temp

# Unused complex transformation
def encrypt_shift(text, shift=3):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 6)

# Distractor: unused statistical function
def calculate_z_scores(data_list):
    mean_val = sum(data_list) / len(data_list)
    variance = sum((x - mean_val) ** 2 for x in data_list) / len(data_list)
    std_dev = variance ** 0.5
    return [(x - mean_val) / std_dev for x in data_list] if std_dev != 0 else [0] * len(data_list)

def process_metrics(raw_data, settings):
    # Extract relevant fields
    text = raw_data.get('content', '')
    mode = settings.get('mode', 'standard')
    threshold = settings.get('threshold', 10)

    # Real computation begins
    stats = analyze_text(text)
    
    # Misleading intermediate calculations
    dummy_sum = 0
    for key in ['upper', 'lower', 'digits']:
        dummy_sum += stats[key] * 7  # Irrelevant multiplier
    
    size_metric = len(text) // 4  # Only partially relevant

    # Key logic hidden among distractions
    weight_map = {'upper': 2, 'lower': 1, 'digits': 5, 'special': 3}
    weighted_total = sum(stats[k] * weight_map[k] for k in stats)

    adjustment = 0
    if stats['special'] > 0 and 'priority' in settings:
        adjustment = settings['priority'] * 2
    
    # Red herring: complex but unused expression
    unused_compound = (stats['upper'] + stats['lower']) * (stats['digits'] + 1) // (stats['special'] + 1)
    
    # Conditional branch with misleading comment
    # "Normalize based on historical baseline" -- actually just adds fixed offset
    if mode == 'enhanced':
        baseline = compute_entropy([stats['upper'], stats['lower'], stats['digits']])
        adjustment += int(baseline * 10)
    else:
        adjustment -= 1  # Counteracts previous red herring

    # Final computation
    raw_score = weighted_total + adjustment
    
    # Critical execution point
    final_score = abs(raw_score - threshold * 3) + size_metric

    # More distractions below
    extra_noise = 0
    for i in range(1, 10):
        extra_noise += (i * final_score) % 9  # Unused accumulator

    return int(final_score)

# Simulated input data
config = {
    'mode': 'standard',
    'threshold': 7,
    'priority': 4
}

data = {
    'content': 'Pass4TheEx@am!',
    'timestamp': '2023-11-05',
    'type': 'assessment'
}

# Execution
final_score = process_metrics(data, config)
print(f"Result: {final_score}")