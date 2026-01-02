from collections import defaultdict
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * math.log2(probability)
    return entropy

def main():
    # Simulate character frequency in a coded message
    message = "aabacbabdadeba"
    frequency_map = defaultdict(int)
    
    for char in message:
        frequency_map[char] += 1
    
    # Irrelevant auxiliary variable (minor distraction)
    avg_length = len(message) / len(frequency_map)
    
    total_entropy = calculate_entropy(frequency_map)
    
    # Print result as required
    print(f"Result: {total_entropy}")

main()