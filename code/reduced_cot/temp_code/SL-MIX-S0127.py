from collections import Counter

# Network connection monitoring simulation
connection_logs = ['active', 'active', 'failed', 'active', 'idle', 'active', 'failed']
status_counts = Counter(connection_logs)
active_connections = status_counts['active']
failed_attempts = status_counts['failed']
multiplier = 3
connection_bonus = 5  # Not used in final calculation
final_count = active_connections * multiplier - failed_attempts
print(f"Target result: {final_count}")