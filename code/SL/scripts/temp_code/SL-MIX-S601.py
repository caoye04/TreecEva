import re
from collections import defaultdict

def calculate_packet_suspicion(header_data):
    base_score = 0
    if re.search(r'\\b(192\\.168|10\\.|172\\.(1[6-9]|2[0-9]|3[01]))\\.', header_data['src_ip']):
        base_score += 5
    if header_data['protocol'] == 'TCP' and int(header_data['dst_port']) > 1024:
        base_score += 3
    if len(header_data['payload']) > 1000:
        base_score += 7
    if 'XSS' in header_data['payload'] or '<script>' in header_data['payload'].lower():
        base_score += 15
    return base_score

packet_headers = [
    {'src_ip': '192.168.1.100', 'dst_port': '8080', 'protocol': 'TCP', 'payload': 'GET / HTTP/1.1'},
    {'src_ip': '203.0.113.5', 'dst_port': '22', 'protocol': 'TCP', 'payload': 'SSH-2.0-OpenSSH'},
    {'src_ip': '10.0.0.25', 'dst_port': '3306', 'protocol': 'TCP', 'payload': 'SELECT * FROM users WHERE id=1'},
    {'src_ip': '172.16.0.45', 'dst_port': '80', 'protocol': 'HTTP', 'payload': '<script>alert("XSS")</script>'},
    {'src_ip': '8.8.8.8', 'dst_port': '53', 'protocol': 'UDP', 'payload': 'DNS query'},
    {'src_ip': '192.168.10.20', 'dst_port': '4444', 'protocol': 'TCP', 'payload': 'a' * 1500}
]

suspicion_scores = defaultdict(int)
for header in packet_headers:
    score = calculate_packet_suspicion(header)
    suspicion_scores[header['src_ip']] += score

high_risk_ips = {ip for ip, score in suspicion_scores.items() if score >= 10}
final_suspicion_score = sum(suspicion_scores[ip] for ip in high_risk_ips)

print(f"Result: {final_suspicion_score}")