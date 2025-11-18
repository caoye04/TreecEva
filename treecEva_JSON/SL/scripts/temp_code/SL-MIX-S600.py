from functools import reduce

def get_octave_shift(note):
    switcher = {
        'C': -1,
        'D': 0,
        'E': 1,
        'F': 1,
        'G': 2,
        'A': 3,
        'B': 4
    }
    return switcher.get(note[0], 0)

def process_note_freq(freq_val, note_name):
    base_transform = freq_val * 2 if 'sharp' in note_name else freq_val // 2
    octave_mod = get_octave_shift(note_name)
    return base_transform + octave_mod

initial_frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]  # Middle C to B notes
note_labels = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

# Apply harmonic enrichment using list comprehension and generator expression
harmonic_enrichments = [f * 1.5 for f in initial_frequencies]
frequency_map = dict(zip(note_labels, harmonic_enrichments))

# Apply transformations using functional programming
transformed_signal = reduce(process_note_freq, note_labels, 440.0)

# Create processed tones mapping with dictionary comprehension
enrichment_factors = {note: 1.0 + (i * 0.1) for i, note in enumerate(note_labels)}
base_signals = {k: frequency_map[k] * enrichment_factors[k] for k in frequency_map}

# Merge with additional processing layer
processing_layer = {note: val * (1 + get_octave_shift(note) * 0.05) for note, val in base_signals.items()}
final_mix = {**base_signals, **processing_layer}

# Calculate final processed tone
processed_tone = sum(final_mix.values()) % 1000

print(f"Result: {int(processed_tone)}")