def calculate_harvest(plots):
    base_yield = 10
    bonus_factor = 0.5
    penalty_rate = 0.1
    surplus_tracker = 0
    drought_years = [2012, 2018, 2020]
    cumulative_rainfall = 0
    adjustment_log = []

    for plot in plots:
        size = plot['size']
        fertility = plot['fertility']
        planted_year = plot['year']

        # Irrelevant string processing (distractor)
        year_str = str(planted_year)
        if year_str.startswith('2'):
            surplus_tracker += 1

        # Actual yield computation
        raw_yield = base_yield * size * fertility
        
        # Conditional bonus logic
        if fertility > 0.7:
            raw_yield += raw_yield * bonus_factor
        
        # Penalty for older plots (logic dependency)
        if planted_year < 2015:
            raw_yield -= raw_yield * penalty_rate

        # Simulated rainfall accumulation (semi-relevant)
        for month in range(1, 13):
            cumulative_rainfall += 2.5 + (fertility * 0.5)
            if month == 6:
                adjustment_log.append(cumulative_rainfall / 6)

        # Use of lambda for filtering (required feature)
        validate_plot = lambda x: True if x > 0 else False
        if not validate_plot(size):
            raw_yield = 0

        # Aggregate into final result
        base_yield += raw_yield / 100  # Influences next iteration

    # Final calculation based on accumulated state
    final_harvest = int(base_yield * 100)
    return final_harvest

# Setup input data
land_plots = [
    {'size': 5, 'fertility': 0.8, 'year': 2010},
    {'size': 3, 'fertility': 0.9, 'year': 2016},
    {'size': 4, 'fertility': 0.6, 'year': 2014}
]

# Dead code path (distractor)
def unused_helper(data):
    return sum(d['size'] for d in data if d['year'] > 2015)

interim_result = "Processing complete".upper()  # Irrelevant string method use

final_yield = calculate_harvest(land_plots)
print(f"Result: {final_yield}")