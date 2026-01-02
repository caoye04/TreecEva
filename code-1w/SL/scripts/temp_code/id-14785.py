def calculate_final_score(raw_data):
    frequencies = {}
    for char in raw_data.lower():
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1
    
    weighted_sum = 0
    for key, count in frequencies.items():
        weight = (ord(key) - ord('a') + 1)
        weighted_sum += weight * count
    
    temp_value = 0
    for i in range(len(frequencies)):
        temp_value += i % 3
    
    checksum = len(raw_data) % 7
    final_score = (weighted_sum // (checksum or 1)) - temp_value
    return final_score

# Irrelevant helper (minimal distraction)
def log_process(x):
    return f'Processed: {x}'

raw_input = 'ElevateException'
data = raw_input.strip()
final_score = calculate_final_score(data)
print(f'Target result: {final_score}')