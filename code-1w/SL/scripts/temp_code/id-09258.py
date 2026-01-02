def calculate_entropy(freq_map):
    import math
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * math.log2(probability)
    return entropy

# Analyze character frequency in a data packet
packet_data = "aabbcddddeeeeeffggggghhhhhii"

# Count character frequencies using dictionary comprehension and enumerate
char_freq = {char: 0 for char in set(packet_data)}
for index, char in enumerate(packet_data):
    char_freq[char] += 1

# Unrelated diagnostic counter (minor distraction)
diagnostic_flag = len([c for c in char_freq.keys() if c in 'aeiou'])

# Compute entropy based on frequency distribution
frequency_map = char_freq

# Key computational step
total_entropy = calculate_entropy(frequency_map)

# Output result as required
print(f"Result: {total_entropy}")