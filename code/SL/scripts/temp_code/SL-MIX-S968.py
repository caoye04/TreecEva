from dataclasses import dataclass
from collections import namedtuple
import statistics

temperature_record = namedtuple('TemperatureRecord', ['day', 'min_temp', 'max_temp'])

@dataclass
class StabilityAnalyzer:
    records: list
    
    def calculate_variance_index(self):
        temp_ranges = [rec.max_temp - rec.min_temp for rec in self.records]
        return statistics.variance(temp_ranges)
    
    def calculate_mean_range(self):
        temp_ranges = [rec.max_temp - rec.min_temp for rec in self.records]
        return statistics.mean(temp_ranges)

# Temperature data for a 5-day period
climate_data = [
    temperature_record(1, 12.5, 24.3),
    temperature_record(2, 14.2, 26.1),
    temperature_record(3, 16.8, 28.9),
    temperature_record(4, 13.7, 22.4),
    temperature_record(5, 15.3, 27.2)
]

analyzer = StabilityAnalyzer(climate_data)
variance_score = analyzer.calculate_variance_index()
mean_temp_range = analyzer.calculate_mean_range()

# Weather stability classification logic
stability_category = None
if variance_score < 2.0:
    stability_category = 'STABLE'
elif variance_score < 4.0:
    stability_category = 'MODERATE'
elif variance_score < 6.0:
    stability_category = 'UNSTABLE'
else:
    stability_category = 'VOLATILE'

# Calculate final stability index based on category
base_modifier = 0
match stability_category:
    case 'STABLE':
        base_modifier = 10
    case 'MODERATE':
        base_modifier = 5
    case 'UNSTABLE':
        base_modifier = -5
    case 'VOLATILE':
        base_modifier = -15
    case _:
        base_modifier = 0

final_stability_index = int(mean_temp_range * base_modifier)
print(f"Result: {final_stability_index}")