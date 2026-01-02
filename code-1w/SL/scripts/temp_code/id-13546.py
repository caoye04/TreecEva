def analyze_frequency(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Irrelevant helper function (distractor)
def validate_input(config):
    if 'mode' not in config:
        return False
    return config['mode'] == 'strict'

# Another distractor: unused data structure
temp_buffer = [0] * 256
overflow_flag = False

config_settings = {'mode': 'relaxed', 'debug': True}
validation_result = validate_input(config_settings)  # Dead computation

# Main data
raw_data = "AbRacAdaBrA!"*3
filtered_chars = ''.join(c for c in raw_data if c.isalpha())

# Frequency analysis (semi-relevant)
freq_map = analyze_frequency(filtered_chars)
dominant_letters = {k: v for k, v in freq_map.items() if v > 5}

# Flag logic with red herring conditions
flags = {
    'enable_enhance': len(dominant_letters) >= 2,
    'check_sum_valid': sum(freq_map.values()) % 4 == 0,
    'legacy_mode': False
}

# Secondary distraction: complex but unused set operation
alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
missing_letters = alphabet_set - set(freq_map.keys())
coverage_ratio = len(alphabet_set) - len(missing_letters)  # Computed but not directly used

# Core processing function
def process_metrics(data, flag_dict):
    base_value = len(data)
    adjustment = 0
    
    # String method chain (relevance: case conversion and cleaning)
    cleaned = data.upper().replace('!', '').replace('?', '')
    token_list = cleaned.split('A')
    non_empty_tokens = [t for t in token_list if t]
    
    # Use of set operation (required feature): unique first characters
    first_chars = set(t[0] for t in non_empty_tokens if t)
    adjustment += len(first_chars) * 2
    
    # Modular arithmetic and integer division
    cycle_mod = (base_value + adjustment) % 7
    if cycle_mod > 3:
        adjustment -= (cycle_mod // 2)
    
    # Conditional flag logic with interdependency
    if flag_dict['enable_enhance']:
        temp_val = 0
        for i, token in enumerate(non_empty_tokens):
            if i % 2 == 1:
                temp_val += len(token) % 3
        adjustment += temp_val
    
    # Early termination pattern
    if flag_dict['legacy_mode']:
        return base_value - adjustment  # Not triggered
    
    # Final calculation
    result = base_value - adjustment
    
    # Distracting final manipulation (not affecting result)
    backup_result = result * 2 + 100  # Unused
    overflow_check = backup_result > 300  # Unused flag
    
    return result

# Critical execution point
data = filtered_chars
final_score = process_metrics(data, flags)
print(f"Target result: {final_score}")