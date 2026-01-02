from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    'ERROR:disk_full', 'INFO:cpu_ok', 'WARN:mem_high',
    'ERROR:disk_full', 'INFO:network_stable', 'WARN:mem_high',
    'ERROR:disk_full', 'INFO:cpu_ok', 'INFO:gpu_active'
]

# Irrelevant helper function (decoy)
def analyze_sentiment(logs):
    sentiment_score = 0
    for log in logs:
        if 'ERROR' in log:
            sentiment_score -= 2
        elif 'WARN' in log:
            sentiment_score -= 1
        else:
            sentiment_score += 1
    return sentiment_score  # Never used in final calculation

# Another red herring: unused statistical transform
def rolling_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        averages.append(round(avg, 2))
    return averages

# Misleading intermediate structure (looks important but isn't used)
class DiagnosticCache:
    def __init__(self):
        self.entries = {}
        self.hit_count = 0

    def add(self, key, value):
        self.entries[key] = value

    def get(self, key):
        if key in self.entries:
            self.hit_count += 1
            return self.entries[key]
        return None

cache = DiagnosticCache()
cache.add('baseline', 42)

# Real processing begins here
log_data = defaultdict(int)
for entry in telemetry_stream:
    level = entry.split(':')[0]
    log_data[level] += 1

# Extract frequencies
error_count = log_data['ERROR']
warn_count = log_data['WARN']
info_count = log_data['INFO']

# Fake transformation path (dead end)
if error_count > warn_count:
    threshold = 0.5
else:
    threshold = 0.8

# Complex but irrelevant string manipulation
decomposed = []
for item in telemetry_stream:
    parts = item.split(':')
    action = ''.join([p[0].upper() for p in parts])
    decomposed.append(action)
fingerprint = ''.join(decomposed)[::3]  # Looks cryptic but unused

# System state with multiple fields (only some matter)
system_state = {
    'uptime': 12746,
    'cores_active': 8,
    'disk_usage_pct': 95,
    'concurrent_users': 23,
    'temperature_c': 67
}

# Bit manipulation decoy
fingerprint_hash = 0
for c in fingerprint:
    fingerprint_hash ^= ord(c)
fingerprint_hash = fingerprint_hash & 0xFFFF  # Mask to 16 bits, unused

# Core logic hidden among distractions
def evaluate_stability(state, errors):
    base_score = 100
    if state['disk_usage_pct'] > 90:
        base_score -= 40
    if state['temperature_c'] > 65:
        base_score -= 20
    if errors > 2:
        base_score -= 30
    return base_score

def calculate_entropy(counts):
    total = sum(counts)
    entropy = 0.0
    for count in counts:
        if count > 0:
            prob = count / total
            entropy -= prob * math.log(prob)
    return round(entropy, 4)

# Secondary metric (appears important)
entropy_metric = calculate_entropy([error_count, warn_count, info_count])

# Main processing function that actually determines result
def process_metrics(metrics, state):
    # This early return is a distractor - condition is never met
    if metrics.get('CRITICAL', 0) > 0:
        return -1
    
    # Real computation buried in middle
    raw_score = evaluate_stability(state, metrics['ERROR'])
    
    # Fake normalization layer
    normalized = raw_score / 100.0
    scaled = int(normalized * 100)
    
    # Additional distraction: string-based weight
    weights = {'high': 3, 'medium': 2, 'low': 1}
    priority = 'high' if metrics['ERROR'] >= 3 else 'medium'
    weighted_score = scaled * weights[priority]
    
    # Final adjustment based on actual logic
    adjustment = 1
    if state['cores_active'] >= 8 and entropy_metric > 1.0:
        adjustment = 2
    
    # The real answer is computed here, but obscured by context
    result = (weighted_score // adjustment) + 17
    
    # Dead code branch (never reached due to logic)
    if result < 0:
        backup_cache = DiagnosticCache()
        backup_cache.add('recovery', 999)
        result = 999
    
    return result

# Key execution point
final_diagnostic = process_metrics(log_data, system_state)

# Output result as required
print(f"Result: {final_diagnostic}")