from functools import reduce
from itertools import combinations

def calculate_inspection_score(failures):
    return reduce(lambda x, y: x ^ (y << 1), failures, 0)

def compute_quality_score(inspection_results):
    base_score = sum(inspection_results) * 3
    adjustment = 0
    for combo in combinations(inspection_results, 2):
        if combo[0] & combo[1]:
            adjustment += 1
    return base_score - adjustment

class WidgetStateMachine:
    def __init__(self):
        self.state = 'START'
        self.mechanical_passed = True
        self.electrical_passed = True
        self.software_passed = True
    
    def process_inspection(self, inspection_type, result):
        if self.state == 'START' and inspection_type == 'mechanical':
            self.mechanical_passed = result
            self.state = 'MECHANICAL_DONE'
        elif self.state == 'MECHANICAL_DONE' and inspection_type == 'electrical':
            self.electrical_passed = result
            self.state = 'ELECTRICAL_DONE'
        elif self.state == 'ELECTRICAL_DONE' and inspection_type == 'software':
            self.software_passed = result
            self.state = 'COMPLETE'
    
    def get_failure_flags(self):
        flags = []
        if not self.mechanical_passed:
            flags.append(1)
        if not self.electrical_passed:
            flags.append(2)
        if not self.software_passed:
            flags.append(4)
        return flags

# Process batch of widgets
widget_batch = [WidgetStateMachine() for _ in range(12)]

# Simulate inspection results
inspection_data = [
    [('mechanical', True), ('electrical', True), ('software', False)],
    [('mechanical', False), ('electrical', True), ('software', True)],
    [('mechanical', True), ('electrical', False), ('software', True)],
    [('mechanical', True), ('electrical', True), ('software', True)],
    [('mechanical', False), ('electrical', False), ('software', False)],
    [('mechanical', True), ('electrical', True), ('software', False)],
    [('mechanical', False), ('electrical', True), ('software', False)],
    [('mechanical', True), ('electrical', False), ('software', False)],
    [('mechanical', False), ('electrical', False), ('software', True)],
    [('mechanical', True), ('electrical', True), ('software', True)],
    [('mechanical', False), ('electrical', True), ('software', True)],
    [('mechanical', True), ('electrical', False), ('software', True)]
]

# Apply inspection data to widgets
for i, widget in enumerate(widget_batch):
    for inspection_type, result in inspection_data[i]:
        widget.process_inspection(inspection_type, result)

# Calculate scores
failure_profiles = [widget.get_failure_flags() for widget in widget_batch]
inspection_scores = [calculate_inspection_score(profile) for profile in failure_profiles]
final_quality_score = compute_quality_score(inspection_scores)

print(f"Result: {final_quality_score}")