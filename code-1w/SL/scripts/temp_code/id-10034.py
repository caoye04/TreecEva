import itertools

# Simulated system telemetry data
technical_metrics = [0.85, 0.92, 0.78, 0.96, 0.88]
user_engagement = {'sessions': 1250, 'retention': 0.73, 'crashes': 14}
config_flags = [True, False, True, True, False]

# Irrelevant preprocessing: bit manipulation red herring
decoys = []
for i in range(5):
    temp_val = (i ^ 12) & 7
    decoys.append(temp_val * 3)

# Unused transformation function
def transform_data(x):
    return [a * 1.05 for a in x if a > 0.8]

# Misleading normalization that isn't used later
normalized_tech = [round((x - 0.7) / (1.0 - 0.7), 3) for x in technical_metrics]

# Real baseline definition (used later)
baseline = {
    'min_tech': 0.8,
    'max_crashes': 15,
    'engagement_threshold': 0.7
}

# Fake scoring model with dead logic
class ScoringModel:
    def __init__(self):
        self.weight = 0.9
        self.active = False  # Never activated

    def compute(self, data):
        return sum(data) * self.weight

# Distractor: unused itertools product
cartesian_combo = list(itertools.product([1, 2], ['a', 'b']))

# Real metric processing starts here
def analyze_stability(flags):
    return sum(1 for f in flags if f)  # Count enabled flags

def extract_key_indicators(metrics, user_data):
    above_min = sum(1 for m in metrics if m >= baseline['min_tech'])
    crash_rate_ok = user_data['crashes'] <= baseline['max_crashes']
    engagement_ok = user_data['retention'] >= baseline['engagement_threshold']
    return {'strong_tech': above_min, 'low_crashes': crash_rate_ok, 'high_engagement': engagement_ok}

# Main evaluation logic (critical path)
metrics = {
    'stability': analyze_stability(config_flags),
    'indicators': extract_key_indicators(technical_metrics, user_engagement)
}

# Red herring dictionary operations
shadow_metrics = metrics.copy()
shadow_metrics['extra'] = {'level': 5, 'valid': False}
if 'debug' in shadow_metrics:
    shadow_metrics['extra']['valid'] = True

# Critical function: evaluates performance using real logic
def evaluate_performance(met, base):
    score = 100
    # Rule 1: Deduct based on missing strong technical metrics
    missing_strong = 5 - met['indicators']['strong_tech']
    score -= missing_strong * 8
    
    # Rule 2: Bonus if crash rate acceptable
    if met['indicators']['low_crashes']:
        score += 15
    
    # Rule 3: Penalty if engagement low
    if not met['indicators']['high_engagement']:
        score -= 20
    
    # Rule 4: Stability bonus
    if met['stability'] > 3:
        score += 10
    
    # Irrelevant bitwise side calculation (distractor)
    magic_flag = (met['stability'] << 2) ^ 5
    dummy_result = magic_flag & 10
    
    # Final adjustment based on obscure rule
    if met['stability'] >= 3 and met['indicators']['strong_tech'] >= 3:
        score = int(score * 1.1)
    
    return score

# Execute critical statement
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Result: {final_score}")