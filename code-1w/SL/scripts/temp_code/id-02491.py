from collections import Counter
class FlowMeter:
    def __init__(self, readings):
        self.readings = readings

    def total(self):
        return sum(self.readings)

# Simulated sensor data for water flow (in liters per minute)
inflow_readings = [12, 15, 10, 18, 20, 14]
outflow_readings = [9, 16, 11, 13, 17, 12]

# Use Counter to validate reading frequencies (additional analysis)
inflow_counter = Counter(inflow_readings)
outflow_counter = Counter(outflow_readings)

# Primary computation: net flow over the period
total_inflow = sum(inflow_readings)
total_outflow = sum(outflow_readings)
net_flow = total_inflow - total_outflow

# Final calculation based on Counter objects
net_flow = inflow_counter.total() - outflow_counter.total()
print(f"Result: {net_flow}")