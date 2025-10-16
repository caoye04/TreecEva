#define _USE_MATH_DEFINES
#include <iostream>
#include <string>

constexpr int scale_factor = 100;

template<typename T>
constexpr T convert_to_celsius(T raw_value) {
    return (raw_value - 32 * scale_factor) * 5 / 9;
}

template<>
constexpr int convert_to_celsius<int>(int raw_value) {
    return (raw_value * 5 - 32 * scale_factor * 5) / 9;
}

constexpr int adjust_calibration(int base_temp) {
    return base_temp + 2 * scale_factor;
}

int main() {
    const std::string unit_label = "C";
    int sensor_reading = 78 * scale_factor;  // 78 degrees Fahrenheit scaled
    int celsius_base = convert_to_celsius(sensor_reading);
    int calibrated_temp = adjust_calibration(celsius_base);
    int final_temperature = calibrated_temp / scale_factor;
    
    std::cout << "Result: " << final_temperature << std::endl;
    return 0;
}