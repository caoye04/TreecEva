def analyze_growth_cycle(data):
    total_cycles = len(data)
    peak_count = 0
    avg_duration = sum([cycle['duration'] for cycle in data]) / total_cycles
    
    # Distractor: irrelevant growth metrics
    phantom_metric = 0
    for cycle in data:
        if cycle['temperature'] > 25:
            phantom_metric += cycle['humidity'] * 0.3
    
    for cycle in data:
        if cycle['yield'] > 90:
            peak_count += 1
    
    return peak_count, avg_duration


def normalize_region_name(name):
    name = name.strip().lower()
    name = name.replace('-', '_').replace(' ', '_')
    if name.endswith('_region'):
        name = name[:-7]
    return ''.join([c for c in name if c.isalnum() or c == '_'])


def calculate_harvest_efficiency(raw_data):
    # Extract and clean region name (string method usage)
    region_name = normalize_region_name(raw_data['region'])
    
    # Harvest metrics
    crops = raw_data['crops']
    base_yield = 0
    adjustment_factor = 1.0
    
    # Summation and conditional logic with nesting
    high_value_crops = [c for c in crops if c['market_price'] > 15]
    
    for crop in crops:
        # Irrelevant computation (distractor)
        fake_score = (crop['growth_rate'] + crop['resilience']) * 0.1
        
        if crop['type'] == 'staple':
            base_yield += crop['baseline_yield']
            if crop['pest_resistance']:
                adjustment_factor *= 1.08

    # Complex condition with logical operations
    if len(high_value_crops) >= 3 and adjustment_factor > 1.05:
        adjustment_factor *= 0.95  # Slight overproduction penalty

    # Secondary distractor: unused accumulation
    total_risk = 0
    for crop in crops:
        risk = 0
        if 'fungus' in crop.get('history', '').lower():
            risk += 20
        if 'drought' in crop.get('history', '').lower():
            risk += 15
        total_risk += risk  # Not used later

    # Final efficiency calculation
    efficiency_score = base_yield * adjustment_factor
    
    # Conditional expression (ternary)
    final_yield = efficiency_score if efficiency_score > 50 else 50.0
    
    return final_yield

# Simulated input data
region_data = {
    'region': ' Northern Plains Region ',
    'crops': [
        {
            'type': 'staple',
            'baseline_yield': 25,
            'growth_rate': 4.2,
            'resilience': 6,
            'pest_resistance': True,
            'market_price': 12,
            'history': 'Previous drought in 2020'
        },
        {
            'type': 'staple',
            'baseline_yield': 30,
            'growth_rate': 3.8,
            'resilience': 7,
            'pest_resistance': True,
            'market_price': 10,
            'history': ''
        },
        {
            'type': 'cash',
            'baseline_yield': 10,
            'market_price': 20,
            'history': 'Fungus outbreak contained'
        },
        {
            'type': 'staple',
            'baseline_yield': 20,
            'growth_rate': 4.0,
            'resilience': 5,
            'pest_resistance': False,
            'market_price': 18,
            'history': 'No issues'
        }
    ],
    'metadata': {
        'analyst': 'DR-7719',
        'version': '2.3'
    }
}

# Execute analysis (irrelevant to final result)
peak_phases, avg_len = analyze_growth_cycle([
    {'duration': 120, 'temperature': 28, 'humidity': 60, 'yield': 95},
    {'duration': 110, 'temperature': 26, 'humidity': 65, 'yield': 88},
    {'duration': 130, 'temperature': 30, 'humidity': 55, 'yield': 92}
])

# Key statement
final_yield = calculate_harvest_efficiency(region_data)
print(f"Result: {final_yield}")