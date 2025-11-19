zones_data = [
    {'season_coeff': 1.2, 'geo_mod': 0.8},
    {'season_coeff': 0.9, 'geo_mod': 1.1},
    {'season_coeff': 1.5, 'geo_mod': 0.7}
]

adjustments = []
for zone in zones_data:
    adj = zone['season_coeff'] * zone['geo_mod']
    adjustments.append(adj)

total_adjustment = 0
for adj_val in adjustments:
    if adj_val > 1.0:
        total_adjustment += adj_val
    else:
        total_adjustment -= adj_val

print(f"Result: {total_adjustment}")