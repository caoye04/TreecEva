import re
from functools import reduce

def calculate_threat_score(log_entries):
    threat_indicators = frozenset(['malware', 'phishing', 'DDoS', 'intrusion'])
    base_scores = {'malware': 10, 'phishing': 7, 'DDoS': 15, 'intrusion': 12}
    
    # Extract threat types using regex and filter valid ones
    extracted_types = list(filter(lambda x: x in threat_indicators, 
                                 [re.search(r'threat=([a-zA-Z]+)', entry).group(1) for entry in log_entries if re.search(r'threat=([a-zA-Z]+)', entry)]))
    
    # Calculate initial score using map and sum
    initial_score = sum(map(lambda t: base_scores[t], extracted_types))
    
    # Apply modifier based on frequency using set operations
    unique_types = set(extracted_types)
    modifier = len(threat_indicators.intersection(unique_types)) * 2
    
    # Ternary operator to adjust score based on modifier
    adjusted_score = initial_score + modifier if modifier > 0 else initial_score
    
    # Final calculation with reduce
    final_threat_score = reduce(lambda acc, x: acc + (x * 2 if x > 10 else x), [base_scores[t] for t in unique_types], 0)
    
    return final_threat_score

log_data = [
    "event_id=1001,threat=malware,severity=high",
    "event_id=1002,threat=phishing,severity=medium",
    "event_id=1003,threat=DDoS,severity=critical",
    "event_id=1004,threat=malware,severity=high",
    "event_id=1005,threat=intrusion,severity=high"
]

final_threat_score = calculate_threat_score(log_data)
print(f"Result: {final_threat_score}")