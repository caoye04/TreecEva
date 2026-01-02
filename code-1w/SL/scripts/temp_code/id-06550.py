from itertools import cycle

# Simulate a power grid load monitor over a week with fluctuating demand
def compute_peak_load():
    daily_pattern = [50, 70, 95, 120, 300, 280, 200, 150]  # Hourly base load pattern (kW)
    weather_factor = [1.0, 1.1, 1.3, 1.5, 1.2, 0.9, 0.8, 1.0]  # Heatwave effect on AC usage
    maintenance_mode = False
    emergency_backup = False
    peak_capacity = 0
    total_energy = 0.0
    fluctuation_log = []
    hour_of_week = 0
    
    # Simulate hourly readings for one week
    for day in range(7):
        for hour_idx, base_load in enumerate(daily_pattern):
            hour_of_week += 1
            
            # Apply weather-dependent scaling
            adjusted_load = base_load * weather_factor[hour_idx % len(weather_factor)]
            
            # Simulate random fluctuations (but deterministically)
            noise = (hour_of_week * 17) % 11 - 5  # Oscillates between -5 and 5
            current_load = int(adjusted_load + noise)
            
            # Artificial constraint: avoid overload during maintenance
            if maintenance_mode:
                if current_load > 250:
                    current_load = 250
            
            # Track peak capacity
            if current_load > peak_capacity:
                peak_capacity = current_load
            
            # Irrelevant logging for system diagnostics
            energy_used = current_load / 1000.0  # kWh
            total_energy += energy_used
            fluctuation_log.append(noise)
            
            # Dummy check for emergency backup activation (never triggers)
            if current_load > 500 and not emergency_backup:
                emergency_backup = True

            # Additional distraction: simulate sensor recalibration every 24 hours
            if hour_of_week % 24 == 0:
                recalibration_offset = sum(fluctuation_log[-8:]) // 8
                _ = recalibration_offset  # Used only for fake diagnostics

    # Post-processing: adjust for transmission loss (does not affect peak)
    transmission_loss_rate = 0.02
    final_energy_delivered = total_energy * (1 - transmission_loss_rate)
    efficiency_ratio = final_energy_delivered / total_energy if total_energy > 0 else 0

    # Output the required result
    print(f"Result: {peak_capacity}")

compute_peak_load()