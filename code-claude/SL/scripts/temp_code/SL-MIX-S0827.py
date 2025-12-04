import itertools

def calculate_volume(dimensions):
    """Calculate package volume based on dimensions"""
    return dimensions[0] * dimensions[1] * dimensions[2]

def calculate_density_factor(dimensions, weight):
    """Calculate density factor for shipping calculations"""
    volume = calculate_volume(dimensions)
    density = weight / volume if volume > 0 else 0
    return min(density * 0.8, 2.5)

def apply_discount(base_cost, loyalty_tier):
    """Apply loyalty discount to shipping cost"""
    discount_rates = {
        'bronze': 0.05,
        'silver': 0.10,
        'gold': 0.15,
        'platinum': 0.20
    }
    rate = discount_rates.get(loyalty_tier.lower(), 0)
    return base_cost * (1 - rate)

def find_optimal_shipping_cost(package_dimensions, shipping_zones):
    # Package information
    length, width, height = package_dimensions
    package_weight = 12.5
    
    # Tracking variables
    base_costs = []
    zone_penalties = []
    environmental_fees = []
    
    # Customer loyalty information
    loyalty_points = 2750
    customer_purchases = 28
    avg_purchase_value = 175.50
    
    # Determine loyalty tier
    if loyalty_points > 5000 and customer_purchases > 50:
        loyalty_tier = 'platinum'
    elif loyalty_points > 3000 or (customer_purchases > 25 and avg_purchase_value > 150):
        loyalty_tier = 'gold'
    elif loyalty_points > 1500:
        loyalty_tier = 'silver'
    else:
        loyalty_tier = 'bronze'
    
    # Calculate dimensions penalty
    oversized_penalty = 0
    if any(dim > 60 for dim in package_dimensions):
        oversized_penalty = sum(max(0, dim - 60) for dim in package_dimensions) * 0.5
    
    # Process each shipping zone
    for zone_id, zone_data in shipping_zones.items():
        # Base shipping calculations
        zone_distance = zone_data['distance']
        zone_multiplier = zone_data['rate_multiplier']
        
        # Calculate potential costs for different shipping methods
        for method in ['standard', 'express', 'priority']:
            if method == 'standard':
                days = 5
                method_multiplier = 1.0
            elif method == 'express':
                days = 3
                method_multiplier = 1.5
            else:  # priority
                days = 1
                method_multiplier = 2.2
            
            # Calculate base cost for this shipping option
            base_cost = (15 + (zone_distance / 100) * zone_multiplier) * method_multiplier
            base_costs.append(base_cost)
            
            # Calculate zone penalty
            if zone_id in ['Z4', 'Z5']:
                zone_penalty = base_cost * 0.15
            else:
                zone_penalty = 0
            zone_penalties.append(zone_penalty)
            
            # Calculate environmental impact fee
            if calculate_volume(package_dimensions) > 8000:  # More than 8000 cubic cm
                env_fee = 5.25
            else:
                env_fee = 2.75
            environmental_fees.append(env_fee)
    
    # Find optimal shipping option
    combined_costs = []
    for i in range(len(base_costs)):
        # We only care about standard shipping for optimal cost
        if i % 3 == 0:  # Only consider standard shipping options
            cost = base_costs[i] + zone_penalties[i] + environmental_fees[i] + oversized_penalty
            combined_costs.append(cost)
    
    # Find minimum cost among standard shipping options
    min_cost = min(combined_costs) if combined_costs else 0
    
    # Apply loyalty discount
    optimal_cost = apply_discount(min_cost, loyalty_tier)
    
    # Handling fee for all packages
    handling_fee = 3.50
    
    # This is just a tracking variable, not used in final calculation
    total_with_handling = optimal_cost + handling_fee
    
    # For debugging purposes
    print(f"Base costs: {base_costs}")
    print(f"Zone penalties: {zone_penalties}")
    print(f"Environmental fees: {environmental_fees}")
    print(f"Oversized penalty: {oversized_penalty}")
    
    return optimal_cost

# Package dimensions in cm (length, width, height)
package_dimensions = [45, 30, 20]

# Available shipping zones with their properties
shipping_zones = {
    'Z1': {'distance': 250, 'rate_multiplier': 1.0},
    'Z2': {'distance': 500, 'rate_multiplier': 1.2},
    'Z3': {'distance': 1000, 'rate_multiplier': 1.5}
}

# Calculate the optimal shipping cost
optimal_cost = find_optimal_shipping_cost(package_dimensions, shipping_zones)
print(f"Result: {optimal_cost}")