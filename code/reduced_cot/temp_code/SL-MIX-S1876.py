from collections import deque
from statistics import mean, variance

def calculate_packet_risk(packet_hash, threat_signatures):
    distances = [abs(packet_hash - sig) for sig in threat_signatures]
    return mean(distances) if distances else 0

def update_security_posture(current_score, risk_values):
    if not risk_values:
        return current_score
    avg_risk = mean(risk_values)
    var_risk = variance(risk_values) if len(risk_values) > 1 else 0
    return (current_score * 0.7) + (avg_risk * 0.2) + (var_risk * 0.1)

# Network monitoring session
packet_hashes = [hash(f'packet_{i}') % 10000 for i in range(10)]
threat_signatures = [1234, 5678, 9012, 3456, 7890]
suspicious_markers = deque([1, 0, 1, 1, 0, 0, 1, 0, 1, 1])
processed_packets_stack = []

security_scores = []
for i, pkt_hash in enumerate(packet_hashes):
    risk = calculate_packet_risk(pkt_hash, threat_signatures)
    is_suspicious = suspicious_markers.popleft()
    if is_suspicious:
        security_scores.append(risk)
    processed_packets_stack.append((pkt_hash, risk, is_suspicious))

final_security_score = update_security_posture(50.0, security_scores)
print(f'Result: {int(final_security_score)}')