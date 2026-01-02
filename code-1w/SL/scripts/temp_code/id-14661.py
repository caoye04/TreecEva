def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence if c.lower() in 'aeiou')
    char_sum = sum(ord(c) for c in sequence)
    reversed_seq = sequence[::-1]
    palindrome_check = sequence == reversed_seq
    return char_sum, palindrome_check

raw_input = 'algorithm'
data_length = len(raw_input)
processed_data = raw_input.upper() + 'X' * (5 - (data_length % 5))

# Irrelevant transformation chain
temp_buffer = [ord(c) * 2 for c in processed_data]
shifted_values = [v >> 1 for v in temp_buffer if v > 100]
stat_summary = sum(shifted_values) // len(shifted_values) if shifted_values else 0

# Distractor variables
dummy_flag = False
intermediate_hash = 0
for i, c in enumerate(processed_data):
    intermediate_hash += ord(c) * (i + 1)
    if i % 3 == 0 and not dummy_flag:
        dummy_flag = True

# Core logic disguised among noise
def calculate_final_score(text):
    score = 0
    for i in range(len(text)):
        if text[i].isalpha():
            score += ord(text[i]) - ord('A') + 1
    
    # Apply modifiers based on structural properties
    length_bonus = len(text) % 7
    checksum = sum(1 for c in text if c in 'AEIOU')
    
    # Real computation path
    base = score * length_bonus
    if 'X' in text:
        base -= text.count('X') * 5
    return base + checksum

# Execution point of interest
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")