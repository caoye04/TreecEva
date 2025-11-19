import math
from collections import namedtuple

# Define a structure for cryptographic analysis
CryptoKey = namedtuple('CryptoKey', ['identifier', 'content', 'base_rating'])

# Sample encryption keys with their base security ratings
encryption_keys = [
    CryptoKey('AES-256', 'xK9#mNp$2vLq@4zR', 8.2),
    CryptoKey('RSA-4096', 'Ht7&bVf*9wSd%1jK', 9.1),
    CryptoKey('ECC-P256', 'aB3$dEf^7gHi&9jL', 7.6)
]

# Character set categories
lowercase_chars = frozenset('abcdefghijklmnopqrstuvwxyz')
uppercase_chars = frozenset('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digit_chars = frozenset('0123456789')
special_chars = frozenset('!@#$%^&*()_+-=[]{}|;:,.<>?')

# Initialize accumulators
composite_entropy_measure = 0
advanced_factor_count = 0

for key in encryption_keys:
    # Determine character set diversity
    key_chars = frozenset(key.content)
    diversity_score = sum([
        bool(key_chars & lowercase_chars),
        bool(key_chars & uppercase_chars),
        bool(key_chars & digit_chars),
        bool(key_chars & special_chars)
    ])
    
    # Calculate entropy-based adjustment using logarithms
    char_space_size = len(lowercase_chars | uppercase_chars | digit_chars | special_chars)
    theoretical_max_entropy = len(key.content) * math.log2(char_space_size)
    actual_entropy = len(key.content) * math.log2(len(key_chars)) if len(key_chars) > 0 else 0
    entropy_efficiency = actual_entropy / theoretical_max_entropy if theoretical_max_entropy > 0 else 0
    
    # Apply exponential weighting to diversity
    weighted_diversity = math.pow(diversity_score, 1.5)
    
    # Compute key strength modifier
    strength_modifier = key.base_rating * entropy_efficiency * weighted_diversity
    
    # Track advanced factors (keys with high diversity and efficiency)
    if diversity_score >= 3 and entropy_efficiency > 0.75:
        advanced_factor_count += 1
    
    # Accumulate composite measure
    composite_entropy_measure += strength_modifier

# Calculate final security rating with logical conditions
if advanced_factor_count >= 2 and composite_entropy_measure > 20:
    final_security_rating = math.ceil(composite_entropy_measure * 1.25)
elif advanced_factor_count >= 1 or composite_entropy_measure > 15:
    final_security_rating = math.floor(composite_entropy_measure * 1.1)
else:
    final_security_rating = math.floor(composite_entropy_measure)

print(f"Result: {final_security_rating}")