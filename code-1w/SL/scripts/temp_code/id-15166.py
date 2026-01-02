def preprocess_sector(sector):
    if not sector['active']:
        return 0
    base = sector['size'] * sector['density']
    adjustment = (sector['growth'] - sector['decay']) ** 2 if sector['growth'] > sector['decay'] else 0
    return base + adjustment

# Irrelevant helper function (decoy)
def calculate_efficiency(elements):
    total_weight = sum([x.get('mass', 0) for x in elements])
    efficiency = total_weight / len(elements) if elements else 0
    return efficiency * 1.5  # unused result

# Misleading data structure
system_metrics = {
    'calibration': [0.89, 0.91, 0.87],
    'tolerance': 0.05,
    'flags': ['valid', 'verified'],
    'score_cache': []  # unused
}

# Unused transformation map
decoys = {
    'alpha': lambda x: x ** 3 % 7,
    'beta': lambda x: (x + 5) // 2,
    'gamma': lambda x: x * 0.1
}

# Real computation begins
region_codes = ['R1', 'R2', 'R3']
sector_data = {
    'R1': [
        {'active': True, 'size': 120, 'density': 8, 'growth': 6, 'decay': 4},
        {'active': False, 'size': 80, 'density': 10, 'growth': 3, 'decay': 7},
        {'active': True, 'size': 60, 'density': 15, 'growth': 9, 'decay': 5}
    ],
    'R2': [
        {'active': True, 'size': 200, 'density': 5, 'growth': 4, 'decay': 2},
        {'active': True, 'size': 90, 'density': 12, 'growth': 7, 'decay': 6}
    ],
    'R3': [
        {'active': False, 'size': 130, 'density': 9, 'growth': 5, 'decay': 3},
        {'active': True, 'size': 110, 'density': 7, 'growth': 8, 'decay': 4}
    ]
}

threshold_map = {'R1': 1000, 'R2': 1200, 'R3': 900}

# Dead code path
for code in region_codes:
    temp_val = system_metrics['tolerance'] * 100
    if temp_val > 5:
        system_metrics['score_cache'].append(temp_val)  # never used

# Another distraction
aggregate = 0
for key, funcs in decoys.items():
    aggregate += funcs(4)  # Computed but irrelevant

# Core logic with conditional expressions and nesting
def calculate_harvest(data, thresholds):
    total_output = 0
    for region_id, sectors in data.items():
        regional_sum = sum(preprocess_sector(sec) for sec in sectors)
        
        # Conditional expression with distractor variables
        adjusted = regional_sum * 1.1 if regional_sum >= thresholds[region_id] else regional_sum * 0.9
        
        # Nested conditionals with red herring checks
        compliance_flag = 1
        if region_id == 'R1':
            compliance_flag = 1 if regional_sum > 800 else 0.8
        elif region_id == 'R2':
            compliance_flag = 1 if adjusted > 1100 else 0.7
        else:
            compliance_flag = 0.9  # default
        
        contribution = adjusted * compliance_flag
        
        # Distractor: modifying unused metric
        if contribution > 1000:
            system_metrics['flags'].append(f'high_{region_id}')
        
        total_output += contribution
    
    # Final adjustment using conditional expression
    bonus_applied = total_output > 3000
    final_total = total_output * 1.05 if bonus_applied else total_output
    
    # Irrelevant rounding on unused path
    rounded = round(final_total, -1)
    
    return final_total

# Execution point of interest
regional_data = sector_data
final_yield = calculate_harvest(regional_data, threshold_map)

print(f"Result: {final_yield}")