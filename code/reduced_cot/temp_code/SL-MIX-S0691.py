class NoteNode:
    def __init__(self, freq=0, next_node=None):
        self.freq = freq
        self.next = next_node

def note_transform_decorator(func):
    transforms = []
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        transforms.append(hash(func.__name__))
        return result
    wrapper.transforms = transforms
    return wrapper

@note_transform_decorator
def modulate_frequency(base_freq, factor):
    return base_freq * factor

@note_transform_decorator
def compute_harmonic_signature(freq_list):
    return sum(hash(str(f)) % 100 for f in freq_list)

# Initialize note sequence: 440 -> 523 -> 660 -> 740 -> None
note_sequence_head = NoteNode(440, NoteNode(523, NoteNode(660, NoteNode(740))))

# Apply frequency modulation using lambda
modulator = lambda x, m: modulate_frequency(x, m)
current = note_sequence_head
modulated_frequencies = []
while current:
    current.freq = modulator(current.freq, 1.2)
    modulated_frequencies.append(current.freq)
    current = current.next

# Compute harmonic signature
harmonic_sig = compute_harmonic_signature(modulated_frequencies)

# Calculate final index
final_harmonic_index = (harmonic_sig + len(modulated_frequencies)*10) % 97

print(f"Result: {final_harmonic_index}")