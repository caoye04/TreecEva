import re

def calculate_threat_score(packet_headers):
    base_patterns = {
        'sql_injection': r"(?i)(union|select|insert|update|delete).*?\b(from|into|where|set)\b",
        'xss_attempt': r"<script.*?>.*?</script>",
        'path_traversal': r"(\.\./)+",
        'cmd_exec': r"(;|&&|\|\||`)"
    }
    
    pattern_scores = {pattern: idx * 5 for idx, pattern in enumerate(base_patterns.keys(), 1)}
    detected_patterns = set()
    
    for header in packet_headers:
        for name, pattern in base_patterns.items():
            if re.search(pattern, header):
                detected_patterns.add(name)
    
    threat_level = sum(pattern_scores[p] for p in detected_patterns)
    return threat_level

# Simulated packet headers with various payloads
network_traffic = [
    "GET /page?id=1 HTTP/1.1",
    "User-Agent: Mozilla/5.0 <script>alert('XSS')</script>",
    "Cookie: session=../../../etc/passwd",
    "Referer: http://example.com; rm -rf /",
    "Accept: */* UNION SELECT username, password FROM users"
]

# Matrix representing previous threat assessments (historical scores)
previous_assessments = [
    [15, 20, 25],
    [10, 30, 35],
    [5,  40, 45]
]

# Calculate current threat score from packet analysis
new_threat_score = calculate_threat_score(network_traffic)

# Dictionary comprehension to adjust historical scores based on new findings
adjusted_scores = {f'packet_{i}': score + new_threat_score 
                  for i, row in enumerate(previous_assessments) 
                  for score in row}

# Merge with a default baseline assessment
baseline = {'default': 10}
dictionary_merge = {**baseline, **adjusted_scores}

# Final threat level combines new findings with adjusted historical data
threat_level = new_threat_score + sum(dictionary_merge.values())

print(f'Result: {threat_level}')