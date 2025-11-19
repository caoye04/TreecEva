import re
from functools import reduce

def calculate_threat_score(log_entries):
    threat_indicators = frozenset(['malware', 'phishing', 'ddos', 'ransomware'])
    high_risk_patterns = ['\.exe$', '\.scr$', 'cmd\.exe']
    
    base_score = 0
    suspicious_files = []
    
    for entry in log_entries:
        components = entry.split('|')
        if len(components) < 3:
            continue
            
        source_ip, destination_ip, payload = components[0], components[1], components[2]
        
        # Check for threat indicators
        indicator_match = False
        for indicator in threat_indicators:
            if indicator in payload.lower():
                indicator_match = True
                base_score += 10
                break
        
        # Early return for critical threats
        if 'ransomware' in payload.lower() and 'kernel' in payload.lower():
            return 999
        
        # Pattern matching for suspicious files
        for pattern in high_risk_patterns:
            if re.search(pattern, payload, re.IGNORECASE):
                suspicious_files.append(payload)
                base_score += 5
                break
        
        # Check for internal network scanning
        if source_ip.startswith('192.168.') and destination_ip.startswith('192.168.'):
            internal_hosts = {'192.168.1.10', '192.168.1.15', '192.168.1.20'}
            if source_ip in internal_hosts and destination_ip not in internal_hosts:
                base_score += 3
    
    # Additional processing for suspicious files
    if suspicious_files:
        unique_suspicious = list(set(suspicious_files))
        encoded_payloads = list(map(lambda x: sum(ord(c) for c in x), unique_suspicious))
        max_encoded = max(encoded_payloads) if encoded_payloads else 0
        if max_encoded > 1000:
            base_score += 15
    
    # Calculate final threat level
    threat_level = 0
    
    match base_score:
        case score if score >= 50:
            threat_level = 5
        case score if score >= 30:
            threat_level = 4
        case score if score >= 15:
            threat_level = 3
        case score if score >= 5:
            threat_level = 2
        case _:
            threat_level = 1
    
    # Adjust for multiple threat indicators
    if base_score > 20:
        threat_indicators_found = [ind for ind in threat_indicators if any(ind in entry for entry in log_entries)]
        if len(threat_indicators_found) >= 2:
            threat_level = min(threat_level + 1, 5)
    
    return threat_level

# Network traffic logs
logs = [
    "192.168.1.10|10.0.0.5|Downloaded malware.exe file",
    "192.168.1.15|192.168.1.25|Accessing kernel modules",
    "203.0.113.5|192.168.1.10|Ransomware detected in system",
    "192.168.1.20|10.0.0.8|Phishing email with malicious scr attachment",
    "10.0.0.1|192.168.1.5|Normal system update"
]

threat_level = calculate_threat_score(logs)
print(f"Result: {threat_level}")