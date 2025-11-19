import re
from collections import namedtuple

# Define a recording structure
Recording = namedtuple('Recording', ['id', 'audio_data'])

# Sample batch of recordings with encoded species calls
batch_recordings = [
    Recording(1, "sparrow-chirp robin-song sparrow-chirp"),
    Recording(2, "eagle-screech sparrow-chirp hawk-scream"),
    Recording(3, "robin-song eagle-screech sparrow-chirp")
]

# Species call patterns
species_patterns = {
    'sparrow': r'sparrow-chirp',
    'robin': r'robin-song',
    'eagle': r'eagle-screech',
    'hawk': r'hawk-scream'
}

# Initialize set for distinct species
identified_species = set()

# Process each recording
for recording in batch_recordings:
    for species, pattern in species_patterns.items():
        if re.search(pattern, recording.audio_data):
            identified_species.add(species)

# Calculate biodiversity index
biodiversity_index = len(identified_species)

print(f"Result: {biodiversity_index}")