from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        probability = count / total
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy

def process_log_data(log_stream):
    tokens = log_stream.split()
    frequency_map = Counter(tokens)
    temp_var = [x.upper() for x in tokens if len(x) > 3]  # irrelevant filtering
    unused_count = len(temp_var)
    total_entropy = calculate_entropy(frequency_map)
    return total_entropy

log_input = "error warning debug error info warning error status debug"
result = process_log_data(log_input)
total_entropy = result
print(f"Target result: {total_entropy}")