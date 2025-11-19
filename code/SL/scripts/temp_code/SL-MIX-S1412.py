import re
from collections import defaultdict, Counter

def calculate_phoneme_weights(phoneme_data):
    # Initialize weight tracking
    weight_map = defaultdict(int)
    
    # Process each phoneme entry
    for entry in phoneme_data:
        # Extract phoneme and context using regex
        match = re.match(r'([a-z]+)_([0-9]+)', entry)
        if match:
            phoneme, position = match.groups()
            # Calculate base weight using string hash
            base_weight = hash(phoneme) % 1000
            # Apply position modifier
            pos_modifier = int(position) * 7
            # Store weighted value
            weight_map[phoneme] += base_weight + pos_modifier
    
    # Sort phonemes by accumulated weight
    sorted_phonemes = sorted(weight_map.items(), key=lambda x: x[1], reverse=True)
    
    # Calculate final score using top 3 phonemes
    top_three_scores = [score for _, score in sorted_phonemes[:3]]
    final_score = sum(top_three_scores) >> 2  # Right shift by 2 (equivalent to dividing by 4)
    
    return final_score

# Sample dataset representing phoneme occurrences
phoneme_dataset = [
    "ba_1", "ka_2", "da_1", "ba_3", 
    "ka_1", "ta_2", "da_2", "ga_1",
    "na_3", "ma_2", "pa_1", "la_2"
]

# Execute analysis
final_score = calculate_phoneme_weights(phoneme_dataset)
print(f"Result: {final_score}")