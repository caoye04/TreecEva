import math

def tokenize_config(config_str):
    tokens = []
    i = 0
    while i < len(config_str):
        if config_str[i].isspace():
            i += 1
            continue
        elif config_str[i] == '"':
            j = i + 1
            while j < len(config_str) and config_str[j] != '"':
                j += 1
            tokens.append(('STRING', config_str[i+1:j]))
            i = j + 1
        elif config_str[i].isalpha():
            j = i
            while j < len(config_str) and config_str[j].isalnum():
                j += 1
            word = config_str[i:j]
            if word in {'enable', 'disable', 'set'}:
                tokens.append(('KEYWORD', word))
            else:
                tokens.append(('IDENTIFIER', word))
            i = j
        else:
            tokens.append(('SYMBOL', config_str[i]))
            i += 1
    return tokens

def process_tokens(tokens):
    keyword_count = {}
    string_literals = set()
    state_flags = {'enable_flag': False, 'disable_seen': False}
    
    for token_type, value in tokens:
        if token_type == 'KEYWORD':
            keyword_count[value] = keyword_count.get(value, 0) + 1
            if value == 'enable':
                state_flags['enable_flag'] = True
            elif value == 'disable':
                state_flags['disable_seen'] = True
        elif token_type == 'STRING':
            string_literals.add(value)
    
    # Short-circuit evaluation with complex condition
    if state_flags['enable_flag'] and not state_flags['disable_seen'] or len(string_literals) > 2:
        modifier = 0x5C3F
    else:
        modifier = 0x2A1E
    
    # Dictionary comprehension and merging
    base_weights = {k: len(k)*v for k, v in keyword_count.items()}
    extra_weights = {k: ord(k[0]) for k in string_literals}
    merged_weights = {**base_weights, **extra_weights}
    
    # Calculate final state using set operations
    keyword_set = frozenset(keyword_count.keys())
    control_keywords = frozenset({'enable', 'disable'})
    intersection = keyword_set & control_keywords
    
    final_state = (len(intersection) << 16) | (sum(merged_weights.values()) & 0xFFFF)
    final_state ^= modifier
    
    return final_state

config_text = 'enable feature1 "value1" disable "value2" set parameter "value3"'
tokens = tokenize_config(config_text)
final_state = process_tokens(tokens)
print(f"Result: {final_state}")