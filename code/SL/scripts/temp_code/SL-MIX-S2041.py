import math
from functools import reduce

def log_frequency_transform(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return {char: math.log(count) for char, count in freq.items()}

def state_machine_processor(freq_map):
    states = {'initial': 1.0, 'processing': 0.7, 'final': 0.4}
    current_state = 'initial'
    weighted_scores = []
    
    for char, log_freq in sorted(freq_map.items()):
        if current_state == 'initial':
            weight = states['initial'] * math.exp(log_freq)
            current_state = 'processing'
        elif current_state == 'processing':
            weight = states['processing'] * math.pow(log_freq, 2)
            if log_freq > 1:
                current_state = 'final'
        else:  # final state
            weight = states['final'] * math.sqrt(log_freq)
        weighted_scores.append(weight)
    
    return reduce(lambda x, y: x + y, weighted_scores, 0)

class TextPipeline:
    def __init__(self):
        self.processed_text = ""
        self.char_frequencies = {}
    
    def transform_text(self, input_text):
        # String transformation: reverse and duplicate vowels
        vowels = 'aeiou'
        transformed = ''
        for char in input_text:
            if char.lower() in vowels:
                transformed += char * 2
            else:
                transformed += char
        self.processed_text = transformed[::-1]  # Reverse
        return self.processed_text

# Execution pipeline
pipeline = TextPipeline()
original_input = "abracadabra"
transformed_text = pipeline.transform_text(original_input)
frequency_map = log_frequency_transform(transformed_text)
final_weighted_score = state_machine_processor(frequency_map)

print(f"Result: {final_weighted_score}")