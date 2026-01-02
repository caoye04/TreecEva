from collections import Counter

# System health monitoring simulation
data_packets = [1, 1, 0, 1, 1, 0, 0, 1]
error_flags = [bool(x) for x in data_packets]
packet_counter = Counter(error_flags)

# Compute transmission metrics
success_count = packet_counter[True]
failure_count = packet_counter[False]
transmission_rate = success_count / len(data_packets) if data_packets else 0

# User activity and engagement baseline
active_users = 247
baseline = 200
engagement_log = [4.2, 3.8, 4.5, 4.0, 3.9, 4.3]
engagement_score = sum(engagement_log) / len(engagement_log)
min_engagement = 4.0

# Critical logic statement
threshold_flag = (active_users > baseline) and (engagement_score >= min_engagement)

# Irrelevant telemetry
system_uptime = 98.7
diagnostic_mode = False

Result: threshold_flag