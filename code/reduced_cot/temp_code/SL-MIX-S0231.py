from math import gcd
from functools import reduce

def compute_gcd_of_list(numbers):
    return reduce(gcd, numbers) if numbers else 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Packet processing state machine
states = {
    'INIT': 0,
    'MONITORING': 1,
    'ALERT': 2,
    'BLOCKED': 3
}

class PacketAnalyzer:
    def __init__(self):
        self.state = states['INIT']
        self.prime_ports = set()
        self.all_ports = []
        self.gcd_value = 0
        self.security_score = 0
    
    def process_packet(self, port, flags):
        # State transition logic
        if self.state == states['INIT']:
            if port > 1024:
                self.state = states['MONITORING']
        elif self.state == states['MONITORING']:
            if 'SYN' in flags and 'ACK' not in flags:
                self.state = states['ALERT']
        elif self.state == states['ALERT']:
            if port in [22, 443, 80]:
                self.state = states['BLOCKED']
        
        # Port analysis
        self.all_ports.append(port)
        if is_prime(port):
            self.prime_ports.add(port)
        
        # Update GCD
        self.gcd_value = compute_gcd_of_list(self.all_ports)
        
        # Security scoring based on state and port characteristics
        base_score = len(self.prime_ports) * 10
        if self.state == states['BLOCKED']:
            base_score -= 50
        elif self.state == states['ALERT']:
            base_score += 20
        
        # Apply GCD factor
        if self.gcd_value > 1:
            base_score *= self.gcd_value
        
        self.security_score = base_score

# Packet sequence to process
packets = [
    (8080, ['SYN']),
    (1025, ['SYN', 'ACK']),
    (80, ['SYN']),
    (17, ['FIN']),
    (51, ['SYN']),
    (22, ['SYN']),
    (102, ['RST'])
]

analyzer = PacketAnalyzer()
for port, flags in packets:
    analyzer.process_packet(port, flags)

# Final security computation
prime_port_count = len(analyzer.prime_ports)
final_gcd = analyzer.gcd_value
state_factor = 1
if analyzer.state == states['BLOCKED']:
    state_factor = -1
elif analyzer.state == states['ALERT']:
    state_factor = 2

final_security_score = analyzer.security_score + (prime_port_count * final_gcd * state_factor)
print(f"Result: {final_security_score}")