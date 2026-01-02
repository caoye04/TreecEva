from collections import defaultdict

# Simulate harmonic frequency analysis in music theory
def build_frequency_map(base_notes):
    freq_map = defaultdict(float)
    for note in base_notes:
        if note % 3 == 0:
            freq_map[note] += 0.75
        elif note % 2 == 0:
            freq_map[note] += 0.5
        else:
            freq_map[note] += 0.25
    return freq_map

def is_consonant(harmonic_value):
    if harmonic_value < 0.5:
        return False
    return True

def analyze_chords(freq_map):
    total = 0.0
    for value in freq_map.values():
        if is_consonant(value):
            total += value * 2
        else:
            total += value
    return total

# Initial musical note sequence (MIDI note numbers)
base_note_sequence = [60, 62, 64, 65, 67, 69, 71, 72]

# Step 1: Build frequency map based on note properties
frequency_map = build_frequency_map(base_note_sequence)

# Step 2: Analyze harmonic consonance and compute total harmony
# Key execution point
final_harmony = analyze_chords(frequency_map)

total_harmony = final_harmony

print(f"Result: {total_harmony}")