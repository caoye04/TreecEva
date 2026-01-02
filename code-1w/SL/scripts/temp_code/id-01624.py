from itertools import cycle

# Simulate 7-day crop growth cycle with daily environmental factors
daily_factors = [1.2, 0.8, 1.1, 0.95, 1.3, 0.7, 1.05]
base_yield_per_plot = 45
growth_cycle_days = 28
plots = 6

# Initialize variables
cumulative_yields = [0] * plots
day_cycle = cycle(daily_factors)

for day in range(growth_cycle_days):
    current_factor = next(day_cycle)
    for plot_idx in range(plots):
        if day < 14:
            # Growth phase: apply increasing yield
            cumulative_yields[plot_idx] += base_yield_per_plot * current_factor
        else:
            # Decay phase: reduce yield after peak
            decayed_contribution = base_yield_per_plot * current_factor * 0.6
            cumulative_yields[plot_idx] += decayed_contribution

# Calculate total harvest across all plots
total_harvest = int(sum(cumulative_yields))

# Irrelevant logging variable (minimal distraction)
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print(f"Result: {total_harvest}")