import re
from collections import defaultdict, Counter
import heapq

def calculate_base_score(log_entry):
    score = 0
    if re.search(r'\b(SELECT|DROP|UNION)\b', log_entry):
        score += 10
    if 'admin' in log_entry.lower():
        score += 5
    return score

def process_logs(log_entries):
    threat_scores = defaultdict(int)
    keyword_counter = Counter()
    
    for entry in log_entries:
        base = calculate_base_score(entry)
        words = re.findall(r'\w+', entry.lower())
        keyword_counter.update(words)
        ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', entry)
        if ip_match:
            ip = ip_match.group()
            threat_scores[ip] += base
    
    top_keywords = [word for word, count in keyword_counter.most_common(5)]
    suspicious_ips = [ip for ip, score in threat_scores.items() if score > 10]
    
    # Calculate weighted score
    weighted_score = 0
    for ip in suspicious_ips:
        weighted_score += threat_scores[ip] * len([kw for kw in top_keywords if kw in ip])
    
    return threat_scores, top_keywords, suspicious_ips, weighted_score

def main():
    logs = [
        "192.168.1.10 attempted admin login with SELECT * from users",
        "10.0.0.5 DROP TABLE detected in request",
        "Normal traffic from 172.16.0.3",
        "192.168.1.10 UNION attack with admin privileges",
        "Regular data transfer to 10.0.0.5"
    ]
    
    scores, keywords, sus_ips, weight = process_logs(logs)
    
    # Heuristic adjustment using heap
    heap = []
    for ip in sus_ips:
        heapq.heappush(heap, (-scores[ip], ip))  # Max heap
    
    adjusted_score = 0
    while heap:
        neg_score, ip = heapq.heappop(heap)
        adjusted_score += -neg_score * len(ip.split('.'))
    
    # Final calculation
    final_threat_level = adjusted_score + weight + len(keywords)
    print(f"Result: {final_threat_level}")

if __name__ == "__main__":
    main()