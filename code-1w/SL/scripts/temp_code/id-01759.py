from collections import Counter

def tokenize_logs(logs):
    tokens = []
    for log in logs:
        parts = log.lower().split()
        tokens.extend([word for word in parts if len(word) > 2])
    return tokens

def calculate_batch_efficiency(counts, threshold=3):
    efficient_items = 0
    for count in counts.values():
        if count >= threshold:
            efficient_items += 1
    return efficient_items

def calculate_performance(log_batches):
    all_tokens = []
    for batch in log_batches:
        batch_tokens = tokenize_logs(batch)
        all_tokens.extend(batch_tokens)
    
    token_counter = Counter(all_tokens)
    high_freq_count = calculate_batch_efficiency(token_counter)
    total_unique = len(token_counter)
    
    # Irrelevant distraction: unused variable (minimal interference)
    avg_length = sum(len(t) for t in all_tokens) / len(all_tokens) if all_tokens else 0
    
    final_score = total_unique - high_freq_count
    return final_score

# Input data
batch_1 = [
    "System reboot initiated",
    "Network stable at 98%",
    "Reboot completed successfully"
]
batch_2 = [
    "Memory usage normal",
    "System reboot initiated",
    "CPU load average stable"
]
batch_3 = [
    "Disk I/O optimal",
    "Network stable at 98%",
    "Reboot completed successfully"
]

batches = [batch_1, batch_2, batch_3]
final_score = calculate_performance(batches)
print(f"Result: {final_score}")