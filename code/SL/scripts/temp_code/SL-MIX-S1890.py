import base64
import re

def decode_payload(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

def calculate_threat_score(payload):
    score = 0
    # Regex patterns for threat indicators
    if re.search(r'\b(malware|virus)\b', payload, re.IGNORECASE):
        score += 10
    if re.search(r'\b(phishing|scam)\b', payload, re.IGNORECASE):
        score += 5
    if re.search(r'\b(exploit|backdoor)\b', payload, re.IGNORECASE):
        score += 15
    return score

# Encoded network packets
packets = [
    "SGVsbG8gd29ybGQ=",
    "TUd3d0tBUXhOamd3TUF3S0RRd01BZ3dMRnd3TERBdytNYXdLRFF3TUFRd0pBd3dKQkF3S0J3d0tCZ3dMQmd3TEJnd0xCZ3dMQmd3TEJndytKYlF3S0Jnd0xCZ3dMQmd3TEJnd0xCZ3dMQmd3TEJnd0xCZ3crSmJRd0tCZ3dMQmd3TEJnd0xCZ3dMQmd3TEJnd0xCZ3dMQmd3K0phd3dKQnd3SkJnd0pCZ3dKQmd3SkJnd0pCZ3dKQmd3SkJndytKYXc9",
    "UEsDBAoAAAAAALZVHFYAAAAA... (truncated for brevity)",
    "R2V0IGluZm9ybWF0aW9uIGFib3V0IG1hbHdhcmUgcHJvcGVydGllcyBhbmQgZXhwbG9pdHM=",
    "Q2hlY2sgaW52YWxpZCBhY2Nlc3MgdG9rZW5zIGFuZCBwaGlzaGluZyBhdHRlbXB0cw=="
]

# Finite State Machine states
states = {'IDLE': 0, 'PROCESSING': 1, 'ANALYZING': 2}
current_state = states['IDLE']
threat_score = 0
processed_packets = []

for i, packet in enumerate(packets):
    if current_state == states['IDLE']:
        current_state = states['PROCESSING']
    
    if current_state == states['PROCESSING']:
        try:
            decoded_payload = decode_payload(packet)
            processed_packets.append(decoded_payload)
            current_state = states['ANALYZING']
        except Exception as e:
            # Skip malformed packets
            continue
    
    if current_state == states['ANALYZING']:
        # Calculate threat score only for successfully decoded packets
        if processed_packets:
            latest_payload = processed_packets[-1]
            threat_score += calculate_threat_score(latest_payload)
        current_state = states['IDLE']

# Additional security check using set operations
known_malicious_patterns = frozenset(['malware', 'virus', 'exploit'])
suspicious_payloads = [p for p in processed_packets if any(word in p.lower() for word in known_malicious_patterns)]
threat_score += len(suspicious_payloads) * 2

print(f"Result: {threat_score}")