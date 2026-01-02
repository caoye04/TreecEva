def main():
    # Simulate a three-phase electrical system with harmonic distortion
    phase_a = [120 * (i % 60) for i in range(1, 6)]
    phase_b = [120 * ((i + 20) % 60) for i in range(1, 6)]
    phase_c = [120 * ((i + 40) % 60) for i in range(1, 6)]

    phases = list(zip(phase_a, phase_b, phase_c))

    # Irrelevant diagnostic flag (minor distraction)
    system_diagnostic_mode = False

    # Calculate RMS-adjusted power per phase using lambda
    rms_factor = lambda x: round((sum(v**2 for v in x) / len(x)) ** 0.5, 2)

    # Extract individual phase waveforms
    a_vals, b_vals, c_vals = zip(*phases)

    # Compute RMS for each phase
    rms_a = rms_factor(a_vals)
    rms_b = rms_factor(b_vals)
    rms_c = rms_factor(c_vals)

    # Harmonic distortion correction factor (modular arithmetic)
    hcf = (len(phase_a) + 7) % 5  # introduces small nonlinearity

    def calculate_total_power(phase_data):
        base_power = sum(rms_a, rms_b, rms_c)
        # Apply harmonic correction based on cycle count
        corrected_power = base_power * (1 + hcf * 0.02)
        return int(corrected_power)  # Discretized total power

    total_phase_power = calculate_total_power(phases)

    # Extraneous debug print (not affecting result)
    if system_diagnostic_mode:
        print("Debug:", rms_a, rms_b, rms_c)

    print(f"Result: {total_phase_power}")

if __name__ == "__main__":
    main()