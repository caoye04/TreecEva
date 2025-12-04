from collections import Counter

# Function to calculate character weights in DNA sequences
def analyze_dna(sequence):
    # Count the occurrences of each nucleotide
    nucleotide_counts = Counter(sequence)
    
    # Define weights for nucleotides
    weights = {'A': 2, 'C': -1, 'G': 3, 'T': -2}
    
    # Calculate total weight
    total = sum(nucleotide_counts[n] * weights[n] for n in 'ACGT')
    return total, nucleotide_counts

# DNA samples from different regions
dna_samples = [
    'ACGTACGT',  # Sample 1
    'AAACCCGGT', # Sample 2
    'TGCATGCA'   # Sample 3
]

# Process all samples
sample_weights = []
all_counts = []

for i, sample in enumerate(dna_samples):
    weight, counts = analyze_dna(sample)
    sample_weights.append(weight)
    all_counts.append(counts)
    # Debug information
    print(f"Sample {i+1} weight: {weight}")

# Calculate some statistics that aren't directly used
average_weight = sum(sample_weights) / len(sample_weights)
max_weight = max(sample_weights)
min_weight = min(sample_weights)

# Extract a specific region from the second sample
subsequence = dna_samples[1][2:7]  # Extract 'ACCCG'

# Calculate character weights for the subsequence
character_weight = []
for char in subsequence:
    if char in 'AC':
        character_weight.append(ord(char) % 5)  # A=1, C=2
    else:
        character_weight.append(ord(char) % 7)  # G=6, T=3

# The answer is the sum of character weights
result = sum(character_weight)
print(f"Result: {result}")
