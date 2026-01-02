from collections import defaultdict, Counter

# Simulated user interaction data across multiple app usage levels
raw_events = [
    ('level1', 'click', 'A'), ('level1', 'scroll', 'B'), ('level1', 'click', 'A'),
    ('level2', 'hover', 'C'), ('level2', 'click', 'D'), ('level2', 'click', 'D'),
    ('level3', 'click', 'A'), ('level3', 'scroll', 'E'), ('level3', 'hover', 'C'),
    ('level4', 'click', 'F'), ('level4', 'click', 'F'), ('level4', 'hover', 'C')
]

# Irrelevant mapping: color codes with no impact on logic
COLOR_MAP = {'A': '#FF0000', 'B': '#00FF00', 'C': '#0000FF', 'D': '#FFFF00', 'E': '#FF00FF', 'F': '#00FFFF'}

# Misleading preprocessing: transforms data but isn't used in final calculation
decoys = []
for lvl, act, tag in raw_events:
    if act == 'hover':
        decoys.append(f'{lvl}_{tag}_ho')
    elif act == 'scroll':
        decoys.append(f'{lvl}_{tag}_sc')

# Dead code path: never accessed
ignored_cache = {}
def update_cache(key, val):
    ignored_cache[key] = val  # Function exists but is never called

# Distractor variable: looks important but unused
baseline_metrics = [0.5, 0.7, 0.6, 0.8, 0.9]

# Real processing begins: extract level-specific actions
levels = defaultdict(list)
for level, action, tag in raw_events:
    levels[level].append((action, tag))

# Compute action frequency per level (used later)
analytics = {}
for level, actions in levels.items():
    freq = Counter([act for act, _ in actions])
    total_actions = len(actions)
    unique_tags = len(set(tag for _, tag in actions))
    
    # Decoy intermediate: complex but unused metric
    entropy = 0.0
    for count in freq.values():
        p = count / total_actions
        entropy -= p * p  # Not real entropy, just a red herring
    
    # Relevant metrics
    click_ratio = freq.get('click', 0) / total_actions if total_actions > 0 else 0
    scroll_count = freq.get('scroll', 0)
    
    analytics[level] = {
        'click_ratio': click_ratio,
        'scroll_count': scroll_count,
        'total': total_actions,
        'tags': unique_tags
    }

# Unused function: looks like it processes something important
def analyze_engagement(metrics):
    score = 0
    for m in metrics:
        if m > 0.5:
            score += 1
    return score * 10

# Another distractor: bitwise manipulation with no effect
obfuscation_key = 237
masked_values = [tag ^ obfuscation_key for tag in range(65, 71)]  # A-F in ASCII

# Core algorithm: computes performance score based on specific rules
penalty_floor = -2
counterbalance = 0

# Conditional branches with mixed relevance
for lv in ['level1', 'level2', 'level3', 'level4']:
    data = analytics.get(lv, {})
    if data.get('click_ratio', 0) >= 0.5:
        counterbalance += 1
    if data.get('scroll_count', 0) == 0 and 'level' in lv:
        counterbalance -= 1

# Key function that determines final result
def aggregate_performance(level_data, analysis):
    base = 0
    bonus = 0
    level_names = sorted(level_data.keys())
    
    # Use slicing to extract middle levels
    focus_levels = level_names[1:-1]  # level2 and level3 only
    
    for idx, lvl in enumerate(level_names):
        meta = analysis[lvl]
        
        # Relevant scoring logic
        base += meta['total']
        if meta['click_ratio'] == 1.0:  # Only level4 satisfies this
            bonus += meta['tags']
        
        # Red herring branch: modifies unused variable
        if meta['scroll_count'] > 0:
            baseline_metrics[0] = 999  # No effect on output
    
    # Final computation
    adjustment = len(focus_levels) * 2
    return (base * (bonus + 1)) - adjustment + counterbalance

# Execute main logic
final_score = aggregate_performance(levels, analytics)

# Print result as required
Target result: {final_score}