from collections import defaultdict
from functools import reduce
import operator

def calculate_packet_signature(packet_id, position):
    return (packet_id ^ position) & ((packet_id << 1) | (position >> 1))

def evaluate_security_vector(packets):
    signature_map = defaultdict(int)
    for idx, packet in enumerate(packets):
        sig = calculate_packet_signature(packet, idx)
        signature_map[sig] += 1 if sig > 0 else 0
    
    # Combinatorial analysis of signatures
    unique_sigs = list(signature_map.keys())
    combo_scores = []
    
    # Short-circuit evaluation in condition check
    for i in range(len(unique_sigs)):
        for j in range(i+1, len(unique_sigs)):
            if signature_map[unique_sigs[i]] > 0 and signature_map[unique_sigs[j]] > 0:
                combo_score = (unique_sigs[i] * unique_sigs[j]) % (signature_map[unique_sigs[i]] + signature_map[unique_sigs[j]])
                combo_scores.append(combo_score)
    
    # Divide and conquer approach to aggregate scores
    def divide_scores(scores):
        if len(scores) <= 1:
            return scores[0] if scores else 0
        mid = len(scores) // 2
        left = divide_scores(scores[:mid])
        right = divide_scores(scores[mid:])
        return left ^ right
    
    return divide_scores(combo_scores) if combo_scores else 0

# Network packet sequence analysis
network_traffic = [0x1F, 0x3A, 0x2B, 0x4C, 0x5D]
security_score = evaluate_security_vector(network_traffic)
print(f"Result: {security_score}")