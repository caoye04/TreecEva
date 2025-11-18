from collections import defaultdict

def validate_pattern(pattern, index=0):
    if index >= len(pattern):
        return True
    if pattern[index] in 'AEIOU':
        return validate_pattern(pattern, index + 2)
    return validate_pattern(pattern, index + 1)

def process_signature(document_signature):
    state = 'START'
    char_freq = defaultdict(int)
    anomaly_score = 0
    
    for char in document_signature:
        char_freq[char] += 1
        
        if state == 'START' and char.isupper():
            state = 'CAPITAL'
        elif state == 'CAPITAL' and char.isdigit():
            state = 'NUMBER'
        elif state == 'NUMBER' and char in '!@#':
            state = 'SYMBOL'
        else:
            if state != 'START':
                anomaly_score += 1
            state = 'START'
    
    if not validate_pattern(document_signature):
        anomaly_score += 10
    
    freq_set = set(char_freq.values())
    if len(freq_set) < len(char_freq) // 2:
        anomaly_score += 5
        
    return anomaly_score

document_signature = "A1!B2@C3#D4!E5@F6#G7!H8@I9#J0!"
anomaly_score = process_signature(document_signature)
print(f"Result: {anomaly_score}")