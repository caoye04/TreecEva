def analyze_feedback(records, weights):
    weighted_total = 0
    normalization_factor = len(weights) * sum([r['rating'] for r in records])
    for i, record in enumerate(records):
        if record['valid']:
            weighted_total += record['rating'] * weights[i % len(weights)]
    return weighted_total / (normalization_factor + 1e-8)

# Irrelevant helper - distractor function
def calculate_tenure(years_list):
    avg_tenure = sum(years_list) / len(years_list)
    adjusted = avg_tenure * 1.5 if avg_tenure > 5 else avg_tenure * 0.8
    return int(adjusted)

# Unused data structure - red herring
team_hierarchy = {
    'leaders': ['Alice', 'Bob'],
    'engineers': ['Charlie', 'Diana', 'Eve'],
    'interns': ['Frank']
}

# Misleading intermediate computation
decoy_aggregate = 0
for x in range(1, 100):
    if x % 7 == 0:
        decoy_aggregate += x ** 2

debug_trace = []
status_flags = {k: False for k in ['init', 'validate', 'transform', 'finalize']}

# Core logic disguised among noise
benchmark_criteria = [3, 1, 4, 1, 5]
baseline_shift = 0.25

assessment_log = [
    {'rating': 8, 'valid': True,  'domain': 'design'},
    {'rating': 6, 'valid': True,  'domain': 'testing'},
    {'rating': 4, 'valid': False, 'domain': 'deployment'},  # invalid entry
    {'rating': 9, 'valid': True,  'domain': 'architecture'},
    {'rating': 7, 'valid': True,  'domain': 'integration'},
    {'rating': 5, 'valid': False, 'domain': 'docs'}       # invalid entry
]

# Simulated pre-processing with side effects that don't affect result
temp_ratings = []
for item in assessment_log:
    temp_ratings.append(item['rating'] * 1.1 if item['valid'] else 0)

filtered_set = set(temp_ratings)
filtered_set.discard(0)

# Real computation buried here
outlier_threshold = 8.0
high_performers = set()
for entry in assessment_log:
    if entry['valid'] and entry['rating'] >= outlier_threshold:
        high_performers.add(entry['domain'])

# Secondary irrelevant calculation
consistency_check = True
for i in range(len(assessment_log) - 1):
    if assessment_log[i]['rating'] < assessment_log[i+1]['rating']:
        consistency_check = False

# Key function with multiple concerns and distractions
def evaluate_performance(log_entries, criteria):
    base_score = 0
    bonus_applied = False
    scaling_factor = 1.0
    
    # Simulate complex weighting logic
    for idx, entry in enumerate(log_entries):
        if not entry['valid']:
            continue
        weight = criteria[idx % len(criteria)]
        contribution = entry['rating'] * weight
        
        # Conditional scaling based on hidden rule
        if entry['rating'] >= 8 and idx % 2 == 0:
            contribution *= 1.2
            bonus_applied = True
        
        base_score += contribution
    
    # Hidden dependency on set size
    domain_coverage = len(set(e['domain'] for e in log_entries if e['valid']))
    coverage_bonus = 5 if domain_coverage >= 4 else 0
    
    # Critical distraction: unused path
    if bonus_applied and domain_coverage > 10:
        scaling_factor = 1.5  # never reached
    elif domain_coverage >= 3:
        scaling_factor = 1.1  # this one triggers

    # Final aggregation
    raw_result = base_score * scaling_factor + coverage_bonus
    
    # Apply integer division and rounding as per requirements
    final_raw = int(raw_result // 1)  # floor to integer
    
    # Noise: update debug trace
    global debug_trace
    debug_trace.append(('final_raw', final_raw))
    
    return final_raw

# Dead code path - misleading branch
def generate_report(data):
    if not data:
        return "Empty"
    summary = "Performance Report:\n"
    for d in data:
        summary += f"- {d['domain']}: {d['rating']}\n"
    return summary

# Another red herring: bit manipulation with no effect
temp_flag = 0b101010
for _ in range(3):
    temp_flag = (temp_flag << 1) | (temp_flag >> 5)
    temp_flag &= 0b111111

# Actual execution point of interest
final_score = evaluate_performance(assessment_log, benchmark_criteria)

# Print required output
print(f"Target result: {final_score}")