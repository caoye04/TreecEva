from collections import defaultdict
from statistics import mean
from contextlib import contextmanager

@contextmanager
def risk_calculator():
    state = {'score': 0}
    try:
        yield state
    finally:
        state['score'] *= 2

event_log = [
    ('192.168.1.10', 'failed_login', 3),
    ('10.0.0.5', 'malicious_payload', 5),
    ('192.168.1.10', 'port_scan', 2),
    ('172.16.0.3', 'failed_login', 3),
    ('10.0.0.5', 'data_exfiltration', 7)
]

ip_profiles = defaultdict(list)
suspicious_ips = frozenset(['10.0.0.5', '192.168.1.10'])
weight_map = {
    'failed_login': 2,
    'port_scan': 3,
    'malicious_payload': 5,
    'data_exfiltration': 8
}

for ip, event_type, count in event_log:
    if ip in suspicious_ips:
        weighted_score = weight_map[event_type] * count
        ip_profiles[ip].append(weighted_score)

profile_stats = {
    ip: {'mean': mean(scores), 'total': sum(scores)}
    for ip, scores in ip_profiles.items()
}

with risk_calculator() as calc_state:
    for ip, stats in profile_stats.items():
        if stats['total'] > 10:
            calc_state['score'] += stats['mean']
    intermediate_score = calc_state['score']

penalty_factors = {ip: len(scores) for ip, scores in ip_profiles.items()}
final_risk_score = intermediate_score - sum(penalty_factors.values())
print(f'Result: {final_risk_score}')