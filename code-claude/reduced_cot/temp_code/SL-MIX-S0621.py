def analyze_signal(signal_strength, noise_threshold=15):
    """Analyze signal strength with noise filtering."""
    filtered_signal = [s for s in signal_strength if s > noise_threshold]
    if len(filtered_signal) > 0:
        return sum(filtered_signal) // len(filtered_signal)
    return 0

def calculate_position(text, pattern):
    """Find the position of a pattern in text with adjustments."""
    # Track character frequencies for potential use
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Calculate potential adjustments based on character distribution
    vowels = sum([char_freq.get(v, 0) for v in 'aeiou'])
    consonants = sum([char_freq.get(c, 0) for c in 'bcdfghjklmnpqrstvwxyz'])
    
    # Misleading calculations that aren't used in the final result
    adjustment_factor = (vowels - consonants) if vowels > consonants else 0
    special_chars = len(text) - vowels - consonants
    entropy_measure = len(char_freq) * special_chars
    
    # Find pattern position
    position = text.find(pattern)
    if position == -1:
        # Calculate alternative position based on pattern characteristics
        alt_position = 0
        for char in pattern:
            alt_position += char_freq.get(char, 0)
        return alt_position % len(text) if len(text) > 0 else 0
    
    # More misleading calculations
    signal_data = [ord(c) % 10 for c in text[:10]]
    noise_level = analyze_signal(signal_data)
    
    # Calculate bitwise operations on ASCII values (distraction)
    bit_sum = 0
    for i in range(min(5, len(text))):
        bit_sum |= (1 << (ord(text[i]) % 7))
    
    # Unused complex slice operation
    reversed_slice = text[position:position+10][::-1]
    slice_value = sum([ord(c) for c in reversed_slice]) if reversed_slice else 0
    
    # The actual logic that determines the result
    # Position is modified by pattern length and a constant
    modifier = len(pattern) * 2
    final_pos = position + modifier
    
    # Limit position to text length with wrapping
    if final_pos >= len(text):
        final_pos = final_pos % len(text)
    
    return final_pos

# Main execution
text_data = "python_programming_is_fascinating_and_powerful"
target_pattern = "is"

# Distraction variables and calculations
processing_mode = "advanced"
offset_values = [3, 7, 11, 13, 17]
base_multiplier = 2

# More distractions with list comprehensions
char_values = [ord(c) for c in text_data if c not in "aeiou_"]
even_values = [v for v in char_values if v % 2 == 0]
odd_values = [v for v in char_values if v % 2 == 1]

# Unused complex calculation
if processing_mode == "simple":
    complexity_score = sum(offset_values) // len(offset_values)
else:
    complexity_score = sum([v * base_multiplier for v in offset_values])

# Dead code path
if text_data.startswith("java"):
    alternative_position = text_data.count("a") * 5
    secondary_factor = sum([ord(c) for c in target_pattern])
    position_offset = alternative_position + secondary_factor
else:
    # This branch is taken but most calculations aren't used
    alternative_position = text_data.count("p") * 3
    secondary_factor = len([c for c in text_data if c == target_pattern[0]])
    position_offset = alternative_position - secondary_factor

# More distraction with early returns in an unused function
def optimize_position(pos, text_length, factors):
    if pos < 0:
        return 0
    if pos >= text_length:
        return text_length - 1
    
    for factor in factors:
        if pos % factor == 0:
            return pos // factor
    return pos

# The key calculation that determines the answer
final_position = calculate_position(text_data, target_pattern)

# More distractions after the key calculation
adjusted_position = final_position
if len(even_values) > len(odd_values):
    adjusted_position += 5
else:
    adjusted_position -= 2

print(f"Result: {final_position}")