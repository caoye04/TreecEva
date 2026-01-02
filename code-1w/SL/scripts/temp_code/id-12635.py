from collections import defaultdict, Counter
import math

def analyze_access_patterns(logs):
    # Irrelevant function: analyzes access logs but not used in final computation
    freq = defaultdict(int)
    for log in logs:
        freq[log['user']] += 1
    return {k: v for k, v in freq.items() if v > 1}

def validate_checksum(data):
    # Misleading function: looks important but unused
    chk = 0
    for b in data.encode():
        chk = (chk ^ b) * 13
    return chk % 256

def evaluate_streak(values):
    # Distractor: computes streaks but irrelevant to final result
    max_streak = current = 0
    for v in values:
        if v > 0:
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 0
    return max_streak

def compute_entropy(s):
    # Unused advanced math function
    counts = Counter(s)
    total = len(s)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def filter_anomalies(dataset):
    # Dead code path: never called
    return [x for x in dataset if 10 <= x['value'] <= 100]

def process_performance(metrics, context):
    # Core logic buried among distractions
    base = metrics['attempts']
    correct = metrics['successes']
    penalty = 0
    
    # Red herring: complex string processing
    user_str = ''.join(context['username'].split('_'))
    cap_count = sum(1 for c in user_str if c.isupper())
    if cap_count > 2:
        penalty += 10
    
    # Another distraction: character frequency analysis
    char_freq = Counter(user_str)
    mode_freq = char_freq.most_common(1)[0][1] if char_freq else 0
    if mode_freq > 2:
        penalty += 5
    
    # Bit manipulation decoy
    bit_flag = 0b1010
    temp_mask = (base ^ 0xF) & 0b1111
    if temp_mask & bit_flag:
        penalty -= 3  # Misleading adjustment
    
    # Real logic begins here — hidden in middle
    accuracy = correct / base if base else 0
    timeout_factor = len(context['history']) // 5
    dynamic_weight = 1 + (timeout_factor * 0.1)
    
    # Conditional branch with early exit red herring
    if accuracy == 1.0:
        special_bonus = 50
        return int((accuracy * 100 + special_bonus) * dynamic_weight)
    
    # Main calculation
    raw_score = accuracy * 100
    time_penalty = context.get('latency', 0) // 100
    adjusted = raw_score - time_penalty - penalty
    
    # List comprehension with filtering
    recent = [h for h in context['history'] if h['status'] == 'completed']
    if len(recent) >= 3:
        adjusted += 7
    
    # Final transformation using logarithm
    if adjusted > 0:
        final = math.log(adjusted + 10) * 8.5
    else:
        final = 5.0
    
    return int(final)

# Irrelevant global variables
SYSTEM_BOOT_TIME = 1678886400
ACTIVE_SESSIONS = ["admin", "guest", "backup"]
CONFIG_FLAGS = {'debug': False, 'trace': True, 'verbose': False}
TEMP_BUFFER = bytearray(256)

# Input data setup — key to actual computation
performance_metrics = {
    'attempts': 25,
    'successes': 18
}

user_context = {
    'username': 'Alpha_User_Test',
    'latency': 230,
    'history': [
        {'status': 'failed'},
        {'status': 'completed'},
        {'status': 'completed'},
        {'status': 'completed'},
        {'status': 'skipped'}
    ]
}

# Unused variables — red herrings
baseline_ref = 92.5
convergence_epoch = 7
retry_counter = 0
error_states = set()
checkpoint_data = [0] * 12

# Actual execution point of interest
final_score = process_performance(performance_metrics, user_context)

# Print required output
print(f"Result: {final_score}")