from collections import defaultdict, Counter

# Simulated system diagnostics from a distributed cluster
diagnostic_logs = [
    'NODE_1: CPU=85%, MEM=70%, STATUS=OK',
    'NODE_2: CPU=95%, MEM=88%, STATUS=WARNING',
    'NODE_3: CPU=60%, MEM=45%, STATUS=OK',
    'NODE_4: CPU=90%, MEM=92%, STATUS=CRITICAL',
    'NODE_5: CPU=40%, MEM=30%, STATUS=OK'
]

# Irrelevant helper function – dead code path (distractor)
def legacy_parse(log):
    return {part.split('=')[0]: part.split('=')[1] for part in log.split(': ')[1].split(', ')}

# Misleading aggregation with decoy statistics
total_cpu = 0
total_mem = 0
count_nodes = 0
decoys = []
for log in diagnostic_logs:
    parts = log.split(': ')[1].split(', ')
    cpu_val = int(parts[0].split('=')[1].strip('%'))
    mem_val = int(parts[1].split('=')[1].strip('%'))
    total_cpu += cpu_val
    total_mem += mem_val
    count_nodes += 1
    decoys.append(cpu_val * mem_val)  # Red herring computation

average_cpu = total_cpu / count_nodes if count_nodes else 0
average_mem = total_mem / count_nodes if count_nodes else 0

# Unused complex data structure transformation (distractor)
node_stats = defaultdict(dict)
for i, log in enumerate(diagnostic_logs):
    node_id = f"NODE_{i+1}"
    entries = log.split(': ')[1].split(', ')
    for entry in entries:
        k, v = entry.split('=', 1)
        node_stats[node_id][k] = v

# Another irrelevant transformation using string methods (distraction)
flattened = '|'.join([log.replace(':', ';') for log in diagnostic_logs])
split_parts = flattened.split('|')
reconstructed = [part.replace(';', ':') for part in split_parts]

# Real processing begins here — parsing logs for critical evaluation
def parse_critical_metrics(logs):
    results = []
    status_rank = {'OK': 0, 'WARNING': 1, 'CRITICAL': 2}
    for log in logs:
        _, data = log.split(': ', 1)
        components = dict(item.split('=') for item in data.split(', '))
        cpu = int(components['CPU'].strip('%'))
        mem = int(components['MEM'].strip('%'))
        status = components['STATUS']
        score = cpu * 0.6 + mem * 0.4 + status_rank[status] * 10
        results.append(score)
    return results

# Decoy function that looks important but isn't used
def compute_health_vector(data):
    vec = []
    for d in data:
        tokens = d.split(' ')
        for t in tokens:
            if '%' in t:
                num = int(t.strip('%,%'))
                vec.append(num ** 2)
    return vec

# Actual key logic hidden among distractions
def evaluate_performance(logs):
    raw_scores = parse_critical_metrics(logs)
    filtered_scores = [s for s in raw_scores if s > 75]  # Only high-risk nodes
    base_penalty = sum(1 for s in raw_scores if s > 90) * 15
    adjustment_factor = len(filtered_scores) * 2.5
    aggregate = sum(raw_scores)
    
    # Complex formula involving multiple concepts
    intermediate = aggregate * 0.8 - adjustment_factor
    if len(filtered_scores) >= 2:
        intermediate -= base_penalty
    
    # Final scoring with tuple unpacking and assignment
    offset = 10
    multiplier = 1.1
    final, _ = divmod(intermediate + offset, 1)  # Ignore remainder
    final *= multiplier
    
    # Use of Counter on derived values (meets language feature requirement)
    score_counter = Counter([int(s) for s in raw_scores])
    mode_score = score_counter.most_common(1)[0][0]
    
    # Final adjustment based on mode (subtle but deterministic)
    final += mode_score * 0.1
    
    return int(final)  # Ensure integer result

# Spurious post-processing (distractor)
summary_table = {}
for log in diagnostic_logs:
    node, rest = log.split(': ', 1)
    status = rest.split('STATUS=')[1]
    summary_table[node] = status.lower()

# Additional red herring: character frequency analysis (irrelevant)
all_chars = ''.join(reconstructed)
char_freq = Counter(all_chars)
top_char = char_freq.most_common(1)[0][0]

critical_threshold = 85
exceedance_count = 0
for log in diagnostic_logs:
    cpu_val = int(log.split('CPU=')[1].split(',')[0].strip('%'))
    if cpu_val > critical_threshold:
        exceedance_count += 1

# Key execution point — this is where the real answer is computed
final_score = evaluate_performance(diagnostic_logs)

# Print required output
print(f"Result: {final_score}")