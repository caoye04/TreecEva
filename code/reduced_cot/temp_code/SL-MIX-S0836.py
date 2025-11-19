import itertools

def process_packets(packet_flags):
    state_machine = {
        'START': {'SYN': 'HANDSHAKE', 'DATA': 'PROCESSING'},
        'HANDSHAKE': {'ACK': 'ESTABLISHED', 'RST': 'RESET'},
        'PROCESSING': {'FIN': 'CLOSING', 'DATA': 'PROCESSING'},
        'ESTABLISHED': {'FIN': 'CLOSING', 'DATA': 'ESTABLISHED'},
        'CLOSING': {'ACK': 'CLOSED'},
        'RESET': {},
        'CLOSED': {}
    }
    
    state_scores = {'START': 0, 'HANDSHAKE': 5, 'PROCESSING': 3, 'ESTABLISHED': 10, 'CLOSING': 2, 'RESET': -10, 'CLOSED': 1}
    
    total_score = 0
    current_state = 'START'
    
    for flag_sequence in packet_flags:
        for flag in flag_sequence:
            if flag in state_machine[current_state]:
                next_state = state_machine[current_state][flag]
                total_score += state_scores[next_state]
                current_state = next_state
            else:
                total_score -= 5  # Penalty for invalid transition
                break
    
    return total_score

# Packet sequences to analyze
packet_sequences = [
    ['SYN', 'ACK', 'DATA', 'FIN', 'ACK'],
    ['SYN', 'RST'],
    ['DATA', 'DATA', 'FIN']
]

# Generate all possible orderings of processing the packet sequences
sequence_permutations = list(itertools.permutations(packet_sequences))

# Calculate scores for each permutation
permutation_scores = {}
for i, perm in enumerate(sequence_permutations):
    score = sum(process_packets([seq]) for seq in perm)
    permutation_scores[i] = score

# Find the maximum score among all permutations
max_score_key = max(permutation_scores, key=permutation_scores.get)
final_score = permutation_scores[max_score_key]

print(f"Result: {final_score}")