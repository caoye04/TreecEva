plots = [101, 102, 103, 104, 105]
plant_status = ['mature', 'sprout', 'mature', 'seedling', 'mature']
yield_per_plot = {'mature': 12.5, 'sprout': 3.0, 'seedling': 0.5}

# Irrelevant tracking variable (minimal distraction)
count_check = len([p for p in plant_status if p == 'mature'])

total_yield = 0.0
for i, (plot, status) in enumerate(zip(plots, plant_status)):
    if status in yield_per_plot:
        total_yield += yield_per_plot[status] * (i + 1)

Result: {total_yield}