def main():
    # Initial stock levels for warehouse items
    stock_levels = {'axle_gear': 120, 'bracket_link': 85, 'cog_ring': 200, 'differential_housing': 45}
    
    # Pricing model using lambda functions for dynamic cost calculation
    base_rates = {'axle_gear': 12.5, 'bracket_link': 8.0, 'cog_ring': 5.75, 'differential_housing': 22.0}
    pricing_model = {item: lambda qty, rate=rate: round(qty * rate, 2) for item, rate in base_rates.items()}
    
    # Irrelevant auxiliary data (minor distraction)
    maintenance_schedule = {'axle_gear': 'Q2', 'cog_ring': 'Q4'}
    last_audit = '2023-11-05'
    
    # Core logic: compute total inventory value
    def calculate_total_stock_value(stock_dict, price_funcs):
        total = 0
        for item, quantity in stock_dict.items():
            if item in price_funcs:
                unit_value = price_funcs[item](quantity)
                total += unit_value
        return int(total)  # Final value converted to integer
    
    inventory_value = calculate_total_stock_value(stock_levels, pricing_model)
    
    # Debug flag (unused, minor interference)
    debug_mode = False
    
    print(f"Result: {inventory_value}")

if __name__ == '__main__':
    main()