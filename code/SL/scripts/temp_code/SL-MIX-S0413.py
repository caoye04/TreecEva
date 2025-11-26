power_sources = {'solar': 120, 'wind': 85, 'hydro': 65, 'geothermal': 40}
active_sources = {k: v for k, v in power_sources.items() if v > 50}
transmission_loss = sum(power_sources.values()) * 0.08
base_load = 150
dormant_sources = [k for k, v in power_sources.items() if v <= 50]
dormant_loss = len(dormant_sources) * 5
transformer_efficiency = 0.92
intermediate_power = sum(active_sources.values()) - transmission_loss
final_energy = sum(active_sources.values()) - dormant_loss
print(f"Result: {final_energy}")