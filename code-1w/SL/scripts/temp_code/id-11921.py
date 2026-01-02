from itertools import combinations

# Simulate quantum flux stabilization in a lattice structure
def generate_flux_sequence(length, base):
    seq = [base]
    for i in range(1, length):
        if i % 3 == 0:
            seq.append(seq[-1] + (i ** 2) % 7)
        elif i % 5 == 0:
            seq.append(seq[-1] - (i % 4))
        else:
            seq.append((seq[-1] * 2) % 101)
    return seq

def detect_anomalies(seq):
    # Irrelevant function: detects but doesn't correct anomalies
    anomalies = []
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i-1]) > 50:
            anomalies.append(i)
    return anomalies

def calculate_stability(seq, limit):
    # Core logic: compute stability score based on valid subsequences
    count = 0
    total_energy = 0
    
    # Generate all possible pairs of indices (distractor: many won't meet criteria)
    for i, j in combinations(range(len(seq)), 2):
        subseq = seq[i:j+1]
        if len(subseq) >= 3:
            avg = sum(subseq) / len(subseq)
            variation = sum(1 for x in subseq if abs(x - avg) < 15)
            if variation >= len(subseq) * 0.6:
                energy = sum(x ** 2 for x in subseq) % 1000
                total_energy += energy
                count += 1
    
    # Misleading intermediate calculations
    debug_factor = len(seq) // 7
    padding_offset = (debug_factor * 13) % 23
    
    # Actual result depends only on total_energy and count
    if count == 0:
        return 0
    raw_stability = total_energy // (count + 1)
    
    # Apply modular constraint to keep result bounded
    final_score = (raw_stability * 17) % 9871
    return final_score

# Main execution flow
base_input = 13
sequence_length = 19
threshold = 15

# Generate primary data
flux_sequence = generate_flux_sequence(sequence_length, base_input)

# Perform irrelevant analysis
anomaly_positions = detect_anomalies(flux_sequence)
diagnostic_flag = len(anomaly_positions) > 0

# Introduce distractor variables
normalization_factor = sum(x % 3 for x in flux_sequence)
sample_subset = [flux_sequence[i] for i in range(0, len(flux_sequence), 4)]
shadow_copy = [x for x in flux_sequence]

# Key transformation step
final_flux = calculate_stability(flux_sequence, threshold)

# Print result as required
print(f"Result: {final_flux}")