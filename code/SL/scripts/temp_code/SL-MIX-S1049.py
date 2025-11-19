class IntrusionNode:
    def __init__(self, ip_hash, severity):
        self.ip_hash = ip_hash
        self.severity = severity
        self.next = None

def create_intrusion_chain(attempts_data):
    if not attempts_data:
        return None
    head = IntrusionNode(attempts_data[0][0], attempts_data[0][1])
    current = head
    for ip_hash, severity in attempts_data[1:]:
        current.next = IntrusionNode(ip_hash, severity)
        current = current.next
    return head

def process_security_events(event_chain):
    # Known malicious IP hashes (frozenset for immutability)
    blacklisted_hashes = frozenset([129837412, 982374123, 120938123, 992341234])
    
    # Suspicious pattern hashes
    suspicious_hashes = {882374123, 120938123, 992341234, 123456789}
    
    # High severity threshold
    HIGH_SEVERITY = 7
    
    threat_level = 0
    current_node = event_chain
    
    while current_node:
        ip_hash = current_node.ip_hash
        severity = current_node.severity
        
        # First filter: Not in blacklist OR severity below threshold
        first_filter_pass = ip_hash not in blacklisted_hashes or severity < HIGH_SEVERITY
        
        if first_filter_pass:
            # Second filter: Either suspicious pattern OR high severity
            second_filter_pass = ip_hash in suspicious_hashes or severity >= HIGH_SEVERITY
            
            if second_filter_pass:
                # Third filter: Combined condition with bitwise operation simulation
                third_filter_pass = (ip_hash & 0xF) != 0 or (severity | 0x8) == severity
                
                if third_filter_pass:
                    threat_level += severity * 2
        
        current_node = current_node.next
    
    return threat_level

# Simulated intrusion attempts: (ip_hash, severity_score)
intrusion_attempts = [
    (129837412, 8),   # Blacklisted but high severity
    (982374123, 5),   # Blacklisted, low severity
    (882374123, 6),   # Suspicious pattern
    (120938123, 9),   # Blacklisted and suspicious, high severity
    (999999999, 3),   # Neither blacklisted nor suspicious
    (123456789, 7),   # Suspicious pattern, high severity
    (992341234, 4)    # Blacklisted and suspicious, low severity
]

# Create the intrusion chain
security_chain = create_intrusion_chain(intrusion_attempts)

# Process the events
threat_level = process_security_events(security_chain)
print(f"Result: {threat_level}")