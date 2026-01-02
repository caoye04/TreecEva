def analyze_pattern(sequence):
    count_vowels = 0
    temp_sum = 0
    for char in sequence:
        if char.lower() in 'aeiou':
            count_vowels += 1
        temp_sum += ord(char)
    checksum = temp_sum % 17
    return count_vowels, checksum


def validate_entry(entry_id):
    if not entry_id.startswith('ID-'):
        return False
    body = entry_id[3:]
    if not body.isdigit():
        return False
    return int(body) % 2 == 1


def compute_diagnostics(data_stream):
    diagnostics = []
    for item in data_stream:
        if isinstance(item, str):
            length = len(item)
            upper_count = sum(1 for c in item if c.isupper())
            diagnostics.append((length, upper_count))
    return diagnostics


def adjust_score(base, factor):
    adjustment = 0
    for i in range(1, min(base, 10)):
        if base % i == 0:
            adjustment += i * 0.5
    adjusted = base - (adjustment * factor)
    
    # Irrelevant intermediate calculation (distractor)
    buffer = ''
    for j in range(int(adjusted)):
        if j % 7 == 0:
            buffer += chr(65 + (j % 26))
    buffer_hash = sum(ord(c) for c in buffer) if buffer else 0
    
    final = int(round(adjusted + (buffer_hash % 1)))
    return final

# Main execution
user_sequence = 'OptiMizAtion'
data_stream = ['Alpha', 'BETA', 'gamma', 'DELTA9']
entry_code = 'ID-12345'

# Step 1: Analyze character pattern
vowel_count, seq_checksum = analyze_pattern(user_sequence)

# Step 2: Validate ID
is_valid = validate_entry(entry_code)

# Step 3: Compute diagnostics (semi-relevant, used to derive threshold)
diag_results = compute_diagnostics(data_stream)
total_chars = sum(item[0] for item in diag_results)
threshold = total_chars // 5 if diag_results else 0

# Step 4: Calculate base score
base_score = vowel_count * 13 + seq_checksum

# Misleading computation path (dead end)
counterfeit_score = 0
for x in range(seq_checksum):
    counterfeit_score += base_score // (x + 1) if x < 4 else 0
counterfeit_score = max(counterfeit_score // 10, 50)

# Step 5: Determine penalty factor based on validation and diagnostics
penalty_factor = 0.0
if is_valid:
    penalty_factor += 0.3
if threshold > 8:
    penalty_factor += 0.2
if user_sequence.upper().endswith('N'):
    penalty_factor += 0.1

# Key statement: adjust final score
final_score = adjust_score(base_score, penalty_factor)

# Output result
print(f"Result: {final_score}")