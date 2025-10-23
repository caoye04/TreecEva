#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <functional>
#include <memory>
#include <bitset>

constexpr int encodeBase7(int value) {
    return (value * 3 + 5) % 7;
}

int main() {
    std::vector<int> sensorReadings = {12, 45, 67, 89, 23, 56};
    int telemetryChecksum = 0;
    int index = 0;
    
    auto processReading = [&telemetryChecksum](int rawValue) -> int {
        int encoded = encodeBase7(rawValue);
        int masked = encoded & 0x3; // Keep only 2 bits
        telemetryChecksum += masked;
        return masked;
    };
    
    std::unique_ptr<std::vector<int>> processedData = std::make_unique<std::vector<int>>();
    
    for (const auto& reading : sensorReadings) {
        if (index >= 4) break;
        
        int result = processReading(reading);
        processedData->push_back(result);
        
        switch (result) {
            case 0:
                telemetryChecksum += 10;
                break;
            case 1:
                telemetryChecksum -= 3;
                break;
            case 2:
                telemetryChecksum *= 2;
                break;
            default:
                if (result > 2) {
                    telemetryChecksum += 5;
                }
                return 0; // Early exit simulation (won't execute here)
        }
        index++;
    }
    
    // Final adjustment
    if (telemetryChecksum % 2 == 0) {
        telemetryChecksum /= 2;
    } else {
        telemetryChecksum = (telemetryChecksum << 1) | 1;
    }
    
    std::cout << "Result: " << telemetryChecksum << std::endl;
    return 0;
}