from collections import Counter

# Network bandwidth allocation analysis
total_bandwidth = 1000
node_requests = [120, 85, 200, 150, 90, 180]
bandwidth_threshold = 150

# Calculate approved requests
approved_requests = [req for req in node_requests if req <= bandwidth_threshold]
discarded_requests = [req for req in node_requests if req > bandwidth_threshold]

# Distractor: Calculate frequency of requests (not used in final result)
request_frequency = Counter(node_requests)
most_common_request = request_frequency.most_common(1)[0][0]

# Allocate bandwidth with redundancy factor
redundancy_factor = 1.2
base_allocation = sum(approved_requests)
preliminary_capacity = base_allocation * redundancy_factor

# Distractor: Calculate theoretical maximum (not used)
theoretical_max = total_bandwidth * 0.8

# Apply network overhead adjustment
overhead_percentage = 0.15
overhead_adjustment = preliminary_capacity * overhead_percentage
network_capacity = preliminary_capacity - overhead_adjustment

# Final assignment
final_capacity = network_capacity
print(f"Result: {final_capacity}")