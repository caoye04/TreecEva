from collections import defaultdict

# System logs from two different servers
server_a_logs = ['ERROR', 'INFO', 'WARNING', 'ERROR', 'DEBUG']
server_b_logs = ['WARNING', 'ERROR', 'INFO', 'FATAL', 'ERROR']

# Count frequencies using defaultdict
a_count = defaultdict(int)
b_count = defaultdict(int)

for log in server_a_logs:
    a_count[log] += 1

for log in server_b_logs:
    b_count[log] += 1

# Find unique error types per server
unique_to_a = set(server_a_logs) - set(server_b_logs)
unique_to_b = set(server_b_logs) - set(server_a_logs)

# Common error types across both servers
typical_errors = ['ERROR', 'WARNING', 'INFO']
common_elements = set(server_a_logs) & set(server_b_logs) & set(typical_errors)

# Final result
result = len(common_elements)
print(f"Target result: {result}")