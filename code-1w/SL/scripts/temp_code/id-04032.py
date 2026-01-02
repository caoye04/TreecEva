from collections import defaultdict, Counter
from itertools import zip_longest

def analyze_transmissions(data_stream):
    signal_strengths = defaultdict(float)
    interference_log = []
    temp_accumulator = 0

    for i, packet in enumerate(data_stream):
        if i % 3 == 0:
            temp_accumulator += len(packet) * 0.5
        chars = [c for c in packet if c.isalpha()]
        digits = [int(d) for d in packet if d.isdigit()]
        
        # Irrelevant stats (distractors)
        avg_char_pos = sum(ord(c) for c in chars) / len(chars) if chars else 0
        interference_log.append(avg_char_pos)
        
        # Core logic: count vowel-consonant patterns
        vowels = sum(1 for c in chars if c.lower() in 'aeiou')
        consonants = len(chars) - vowels
        signal_strengths[f'vowel_ratio_cycle_{i % 4}'] += vowels / max(consonants, 1)
    
    return signal_strengths

def process_segments(raw_segments):
    segment_stats = {}
    dummy_tracker = []
    
    for idx, seg in enumerate(raw_segments):
        split_parts = seg.split('-')
        clean_parts = [p.strip().lower() for p in split_parts]
        
        # Distractor: complex but unused structure
        metadata_bundle = {
            'id': hash(tuple(clean_parts)) % 1000,
            'pattern_sig': ''.join(p[0] for p in clean_parts if p)
        }
        dummy_tracker.append(metadata_bundle)
        
        # Relevant transformation
        joined = ''.join(clean_parts)
        segment_stats[f'seg_{idx}'] = {
            'length': len(joined),
            'vowel_count': sum(1 for c in joined if c in 'aeiou'),
            'type_class': 'A' if len(joined) > 5 else 'B'
        }
    
    return segment_stats

def calculate_final_score(metrics):
    base = 0
    penalty = 0
    
    for key, val in metrics.items():
        if 'seg_' in key:
            base += val['length']
            if val['type_class'] == 'A':
                base += val['vowel_count']
            else:
                penalty += 1
    
    # Final adjustment based on logical condition
    adjustment = 1.25 if base > 20 else 0.75
    return int((base - penalty * 2) * adjustment)

# Simulated input data
transmission_input = ['X9aE3m', 'Pz2K', 'Lmno8', 'Qwerty']
signal_analysis = analyze_transmissions(transmission_input)

raw_segment_input = ['Alpha-Beta', 'Gamma', 'Delta-Epsilon-Zeta']
processed_data = process_segments(raw_segment_input)

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")