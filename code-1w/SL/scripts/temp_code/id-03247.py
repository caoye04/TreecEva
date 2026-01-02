def analyze_efficiency(data, threshold=0.75):
    """Irrelevant analysis function (red herring)."""
    if not data:
        return 0
    avg = sum(data) / len(data)
    filtered = [x for x in data if x > threshold]
    return len(filtered) / len(data)


def transform_sequence(seq):
    """Bit manipulation decoy with no impact on final result."""
    result = 0
    for i, val in enumerate(seq):
        result ^= (val << (i % 4))
    return result % 100

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 512
DEFAULT_TIMEOUT = 30
temp_calibration = [0.1, 0.3, 0.5, 0.7, 0.9]

# Real input data (hidden signal among noise)
metrics = [88, 92, 76, 85, 94, 81, 89]
benchmark = {'baseline': 82, 'weight': 0.6}

# Unused recursive function (dead code path)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Misleading intermediate calculation (decoy)
candidate_ranking = sum([x ** 0.5 for x in metrics]) * 2.718

# String-based distractor processing (irrelevant but plausible)
signal_tags = "rtt,ack,seq,dup,fin"
flag_count = len(signal_tags.split(','))
active_flags = signal_tags.upper().replace(',', '|')

# Core logic disguised among distractions
def compute_stability(values):
    """Relevant helper: computes trend stability."""
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    stable_transitions = sum(1 for d in diffs if abs(d) <= 5)
    return stable_transitions >= len(diffs) * 0.6

# Key function that contributes to final answer
def evaluate_performance(scores, config):
    base_avg = sum(scores) / len(scores)
    above_baseline = sum(1 for s in scores if s >= config['baseline'])
    
    # Conditional bonus logic (nested relevance)
    bonus = 0
    if above_baseline >= 4:
        if compute_stability(scores):
            bonus = 12
        else:
            bonus = 5
    elif base_avg >= 85:
        bonus = 7
    
    # Weighted score calculation (actual core)
    weighted = base_avg * config['weight'] + (config['baseline'] * (1 - config['weight']))
    
    # Final adjustment using string-derived fake metric (partial red herring)
    adjustment = len(active_flags.split('|')) if bonus > 10 else 0
    
    return int(weighted + bonus - adjustment)

# Trigger execution
final_score = evaluate_performance(metrics, benchmark)
print(f"Result: {final_score}")