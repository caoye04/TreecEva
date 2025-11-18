import re
from collections import defaultdict

packet_headers = [
    "GET /admin/login HTTP/1.1|User-Agent: Mozilla|X-Forwarded-For: 192.168.1.100",
    "POST /api/v1/users HTTP/1.1|Content-Type: application/json|Authorization: Bearer abc123",
    "GET /public/index.html HTTP/1.1|User-Agent: Chrome|Referer: https://external.com",
    "DELETE /api/v1/sessions HTTP/1.1|Authorization: Basic xyz789|X-Custom-Header: suspicious_value",
    "PUT /api/v1/settings HTTP/1.1|Content-Length: 0|X-Forwarded-For: 10.0.0.1"
]

threat_patterns = [
    r"DELETE.*sessions",
    r"Authorization: Basic",
    r"X-Forwarded-For: 192\.168\.1\.100",
    r"X-Custom-Header: suspicious_value"
]

pattern_weights = {
    threat_patterns[0]: 3.5,
    threat_patterns[1]: 2.0,
    threat_patterns[2]: 4.0,
    threat_patterns[3]: 5.5
}

packet_scores = defaultdict(float)

for header in packet_headers:
    for pattern in threat_patterns:
        if re.search(pattern, header):
            packet_id = hash(header) % 1000
            packet_scores[packet_id] += pattern_weights[pattern]

aggregate_threat_score = 0.0
for score in packet_scores.values():
    if score > 5.0:
        aggregate_threat_score += score * 1.5
    else:
        aggregate_threat_score += score

print(f"Result: {aggregate_threat_score}")