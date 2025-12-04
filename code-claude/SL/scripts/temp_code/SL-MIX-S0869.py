import itertools

def analyze_password_patterns(passwords):
    # Calculate pattern strength based on character distribution
    char_counts = {}
    for password in passwords:
        for char in password:
            char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find most and least common characters
    most_common = max(char_counts.items(), key=lambda x: x[1])[0]
    least_common = min(char_counts.items(), key=lambda x: x[1])[0]
    
    # Calculate a baseline security score (not used in final calculation)
    baseline_score = sum(ord(c) for c in most_common + least_common)
    
    return most_common, least_common, baseline_score

# Password dataset
passwords = ["p@ssw0rd", "qwerty123", "secure!99", "admin123", "letmein"]

# Extract unique characters for analysis
unique_chars = set(''.join(passwords))
char_combinations = list(itertools.combinations(unique_chars, 2))

# Analyze password security
most_common, least_common, unused_score = analyze_password_patterns(passwords)

# Calculate entropy factors
entropy_base = ord(most_common) ^ ord(least_common)
bit_strength = len(unique_chars) * 2

# Apply security multipliers
result_factors = []
for i in range(3):
    # Conditional calculation based on character properties
    if i % 2 == 0:
        factor = entropy_base + bit_strength
    else:
        factor = entropy_base - bit_strength
    result_factors.append(factor)

# Generate alternative factors (distraction calculation)
alternative_factors = [ord(c) % 32 for c in unique_chars if c.isalnum()]
alternative_sum = sum(alternative_factors)

# Calculate final strength value
result_sum = sum(result_factors) + len(char_combinations)

# Normalize to byte range
encryption_strength = result_sum & 0xFF

# Apply additional security checks (distraction calculation)
if entropy_base > 50:
    security_rating = "high"
elif entropy_base > 30:
    security_rating = "medium"
else:
    security_rating = "low"

print(f"Result: {encryption_strength}")