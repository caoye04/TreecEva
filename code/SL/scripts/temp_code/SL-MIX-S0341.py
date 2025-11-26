def apply_discounts(base_total, membership):
    tier_multipliers = {'bronze': 0.95, 'silver': 0.90, 'gold': 0.85}
    base_discount = tier_multipliers.get(membership, 1.0)
    adjusted_total = base_total * base_discount
    
    # Check for bulk discount eligibility
    if base_total > 500:
        bulk_reduction = adjusted_total * 0.05
        adjusted_total -= bulk_reduction
    
    total_discount = base_total - adjusted_total
    return total_discount

cart_total = 650
membership_level = 'silver'
final_pricing = apply_discounts(cart_total, membership_level)
print(f"Result: {final_pricing}")