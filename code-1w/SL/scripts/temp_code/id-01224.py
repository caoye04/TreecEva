def calculate_energy_flux(readings):
    scaled_readings = [x * 0.75 for x in readings]
    positive_contributions = [val for val in scaled_readings if val > 5]
    negative_contributions = [val for val in scaled_readings if val < 0]
    net_flux = sum(positive_contributions) - sum(negative_contributions)
    return net_flux

sensor_data = [12, -3, 8, -6, 15, 4, -2]
result = calculate_energy_flux(sensor_data)
print(f"Result: {result}")