def optimize_route(route_data):
    # Optimize shipping routes based on distance and cargo type
    optimized = {}
    for city, details in route_data.items():
        distance = details['distance']
        traffic = details.get('traffic_index', 1.0)
        # Apply optimization formula
        optimized[city] = distance * (2 - traffic/10)
    return optimized

def calculate_tax(value, country_code):
    # Calculate import taxes based on country code
    tax_rates = {
        'US': 0.08,
        'EU': 0.21,
        'CN': 0.17,
        'JP': 0.10
    }
    # Default tax rate for unknown countries
    return value * tax_rates.get(country_code, 0.15)

def analyze_cargo_composition(cargo_items):
    # Analyze cargo composition for quality assessment
    total_quality = 0
    quality_factors = {'A': 3, 'B': 2, 'C': 1, 'D': 0.5}
    
    for item, details in cargo_items.items():
        grade = details.get('grade', 'C')
        weight = details.get('weight', 1)
        total_quality += quality_factors.get(grade, 0) * weight
    
    return total_quality / max(1, len(cargo_items))

def calculate_final_cargo_value(manifest, routes):
    # Extract primary cargo values
    primary_cargo = manifest['primary_cargo']
    base_value = primary_cargo['base_value']
    
    # This calculation is misleading and not used in final result
    misleading_value = 0
    for i, item in enumerate(manifest.get('secondary_cargo', [])):
        factor = 1.5 if i % 2 == 0 else 0.8
        misleading_value += item.get('value', 0) * factor
    
    # Calculate route efficiency
    route_efficiency = 1.0
    active_routes = [r for r in routes if r.get('active', False)]
    if active_routes:
        distances = [r['distance'] for r in active_routes]
        # Misleading calculation that won't be used
        unused_metric = sum(distances) / len(distances) * 0.75
        
        # The actual calculation we'll use
        priority_routes = set([r['id'] for r in routes if r.get('priority', False)])
        normal_routes = set([r['id'] for r in routes]) - priority_routes
        
        # Route efficiency calculation using set operations
        efficiency_factor = len(priority_routes) * 0.15 + len(normal_routes) * 0.05
        route_efficiency = max(0.8, min(1.5, 1 + efficiency_factor))
    
    # Apply various adjustments (some relevant, some not)
    seasonal_adjustments = {
        'winter': 0.9,
        'summer': 1.1,
        'spring': 1.0,
        'fall': 0.95
    }
    
    # This is a distraction - not used in final calculation
    for season, adjustment in seasonal_adjustments.items():
        if manifest.get('season') == season:
            distraction_value = base_value * adjustment
            break
    else:
        distraction_value = base_value
    
    # Calculate insurance costs - this is relevant
    insurance_rate = 0.05
    if manifest.get('hazardous', False):
        insurance_rate = 0.12
    elif manifest.get('fragile', False):
        insurance_rate = 0.08
    
    insurance_cost = base_value * insurance_rate
    
    # Extract cargo quality factor - this is relevant
    cargo_details = primary_cargo.get('details', {})
    quality_items = {k: v for k, v in cargo_details.items() if k in ['A1', 'B2', 'C3']}
    
    # Irrelevant calculation to distract
    for item_name, specs in cargo_details.items():
        if 'premium' in specs.get('tags', []):
            premium_bonus = specs.get('value', 0) * 0.25
    
    # Relevant calculation - using slicing
    route_codes = [r.get('code', '000') for r in routes]
    risk_factor = 0
    if route_codes:
        # Use the first 2 digits of each code to calculate a risk factor
        risk_digits = [int(code[:2]) if code[:2].isdigit() else 50 for code in route_codes]
        risk_factor = sum(risk_digits) / len(risk_digits) / 100
    
    # Final calculation with relevant factors
    quality_modifier = 1.0
    if quality_items:
        quality_values = [details.get('quality', 5) for details in quality_items.values()]
        quality_modifier = sum(quality_values) / len(quality_values) / 5
    
    # The actual final calculation
    final_value = base_value * route_efficiency * (1 - insurance_rate) * (1 + quality_modifier) * (1 - risk_factor)
    
    # Round to 2 decimal places for currency value
    return round(final_value, 2)

# Main program
manifest = {
    'primary_cargo': {
        'id': 'C-1289',
        'base_value': 45000,
        'details': {
            'A1': {'quality': 8, 'tags': ['premium']},
            'B2': {'quality': 7, 'tags': ['standard']},
            'C3': {'quality': 6, 'tags': ['economy']}
        }
    },
    'secondary_cargo': [
        {'id': 'SC-001', 'value': 5000},
        {'id': 'SC-002', 'value': 3500},
        {'id': 'SC-003', 'value': 2800}
    ],
    'fragile': True,
    'season': 'winter'
}

routes = [
    {'id': 1, 'code': '723', 'distance': 1500, 'active': True, 'priority': True},
    {'id': 2, 'code': '845', 'distance': 2100, 'active': True, 'priority': False},
    {'id': 3, 'code': '512', 'distance': 980, 'active': False, 'priority': False},
    {'id': 4, 'code': '390', 'distance': 1700, 'active': True, 'priority': True}
]

# Calculate alternative values (distractions)
distractor_routes = optimize_route({'NYC': {'distance': 1200, 'traffic_index': 8}, 
                                 'LAX': {'distance': 2800, 'traffic_index': 6}})
distractor_tax = calculate_tax(manifest['primary_cargo']['base_value'], 'EU')
distractor_quality = analyze_cargo_composition({'item1': {'grade': 'A', 'weight': 2}, 
                                            'item2': {'grade': 'B', 'weight': 3}})

# The key calculation we're interested in
cargo_value = calculate_final_cargo_value(manifest, routes)

print(f"Route optimization: {distractor_routes}")
print(f"Tax calculation: {distractor_tax}")
print(f"Quality analysis: {distractor_quality}")
print(f"Final cargo value: {cargo_value}")