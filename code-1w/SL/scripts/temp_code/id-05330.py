from itertools import groupby

def calculate_entropy(freq_list):
    total = sum(freq_list)
    entropy = 0.0
    for freq in freq_list:
        if freq > 0:
            probability = freq / total
            entropy -= probability * __import__('math').log2(probability)
    return entropy

def main():
    raw_sequence = 'aabbbbcccddee'
    frequency_data = [len(list(group)) for _, group in groupby(sorted(raw_sequence))]
    
    # Irrelevant auxiliary variable (minimal distraction - intervention level 5)
    temp_result = [x * 2 for x in frequency_data if x < 3]
    
    total_entropy = calculate_entropy(frequency_data)
    print(f"Result: {total_entropy}")

main()