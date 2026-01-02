def calculate_subnet_score(segment):
    length = len(segment)
    active_nodes = sum(1 for c in segment if c == '1')
    return active_nodes * (length - active_nodes)

subnets = ['11001', '101', '1111000', '0011', '10']

# Irrelevant utility function (distractor)
def format_binary_string(s):
    return '0b' + s

# Key computation path
subnet_scores = [calculate_subnet_score(subnet) for subnet in subnets]

threshold = 3
filtered_scores = [score for score in subnet_scores if score > threshold]

total_capacity = 0
for score in filtered_scores:
    total_capacity += score

# Additional irrelevant variable
max_score = max(subnet_scores) if subnet_scores else 0

Result: total_capacity