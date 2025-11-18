from functools import reduce

def analyze_packet_headers():
    # Baseline ports commonly used in attacks
    baseline_ports = frozenset([21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995])
    
    # Observed port activity from network traffic
    observed_sessions = [
        [8080, 8443, 21],
        [1337, 80, 22],
        [53, 5353, 123],
        [4444, 8080, 80],
        [25, 465, 587]
    ]
    
    # Convert to sets for set operations
    observed_sets = list(map(set, observed_sessions))
    
    # Find intersection of each session with baseline ports
    flagged_sessions = [
        session & baseline_ports for session in observed_sets
    ]
    
    # Count total flagged ports across all sessions
    total_flagged = sum(len(session) for session in flagged_sessions)
    
    # Apply nested loop transformation for entropy-like scoring
    score_matrix = []
    for i in range(len(observed_sets)):
        row = []
        for j in range(len(observed_sets)):
            common_elements = observed_sets[i] & observed_sets[j]
            # Ternary operator to avoid zero values
            weight = len(common_elements) if len(common_elements) > 0 else 1
            row.append(weight)
        score_matrix.append(row)
    
    # Reduce the matrix to a single suspiciousness score
    aggregate_weights = [
        reduce(lambda x, y: x * y, row, 1) for row in score_matrix
    ]
    
    # Final score calculation
    suspicious_score = (
        total_flagged * max(aggregate_weights)
        if max(aggregate_weights) > 1
        else total_flagged + sum(aggregate_weights)
    )
    
    return suspicious_score

# Execute the analysis
final_score = analyze_packet_headers()
print(f"Target result: {final_score}")