def calculate_market_influence(revenue, competitors):
    """Calculate market influence based on revenue and competitor count"""
    base_factor = 2.5
    market_factor = revenue / (competitors + 1)
    # Additional calculation that isn't used
    potential_growth = revenue * 0.15 if competitors < 5 else revenue * 0.08
    return market_factor * base_factor

def calculate_effective_share(data_dict, company_name):
    """Calculate the effective market share for a company"""
    if company_name not in data_dict:
        return 0
    
    company_info = data_dict[company_name]
    revenue = company_info['revenue']
    competitors = company_info['competitors']
    
    # These sectors have different weighting formulas
    tech_sectors = ['software', 'hardware', 'cloud']
    retail_sectors = ['online', 'physical', 'hybrid']
    
    sector = company_info['sector']
    years = company_info['years_active']
    
    # Calculate base share
    base_share = revenue / sum(d['revenue'] for d in data_dict.values())
    
    # Apply sector modifier
    sector_modifier = 1.0
    if sector in tech_sectors:
        sector_modifier = 1.2
    elif sector in retail_sectors:
        sector_modifier = 0.9
    
    # Calculate market influence (used in final calculation)
    influence = calculate_market_influence(revenue, competitors)
    
    # This is a distractor calculation
    customer_loyalty = min(years * 0.05, 0.8)
    marketing_effectiveness = (revenue * 0.00001) + 0.5
    
    # The effective formula uses base_share, sector_modifier and influence
    # The customer_loyalty and marketing_effectiveness aren't used
    effective_share = base_share * sector_modifier + (influence / 1000)
    
    return round(effective_share * 100, 2)

# Company market data
company_data = {
    'TechCorp': {
        'revenue': 850000,
        'competitors': 4,
        'sector': 'software',
        'years_active': 12
    },
    'RetailGiant': {
        'revenue': 1200000,
        'competitors': 7,
        'sector': 'online',
        'years_active': 20
    },
    'ManufacturerX': {
        'revenue': 750000,
        'competitors': 3,
        'sector': 'hardware',
        'years_active': 15
    },
    'ServicePro': {
        'revenue': 500000,
        'competitors': 9,
        'sector': 'cloud',
        'years_active': 8
    }
}

# Calculate total industry value (distractor)
industry_value = sum(company['revenue'] for company in company_data.values())
print(f"Total industry value: {industry_value}")

# Calculate average competitors (distractor)
avg_competitors = sum(company['competitors'] for company in company_data.values()) / len(company_data)
print(f"Average competitors: {avg_competitors}")

# Calculate the market share for TechCorp
market_share = calculate_effective_share(company_data, "TechCorp")
print(f"Result: {market_share}")