def monitor_power_levels():
    base_load = 174
    peak_load = 268
    safety_margin = 19

    # Calculate dynamic threshold using conditional expression
    load_forecast = base_load * 1.3 if peak_load > 250 else base_load * 1.1

    # Apply bitwise adjustment for grid stability (simulates hardware feedback)
    stability_hint = (peak_load ^ 0x0F) & 0x07

    # Final threshold combines arithmetic and bit logic
    energy_threshold = int(load_forecast + safety_margin) | stability_hint

    return energy_threshold

# Execute function and print result
target_result = monitor_power_levels()
print(f"Result: {target_result}")