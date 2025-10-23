#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> sensor_readings = {15, -8, 22, -3, 17, 0, -12};
    int checksum = 0;
    int weight = 1;
    
    for (size_t i = 0; i < sensor_readings.size(); ++i) {
        int reading = sensor_readings[i];
        int transformed = (reading % 2 == 0) ? (reading / 2) : (reading * 3 + 1);
        
        if (transformed > 0) {
            checksum += (i % 2 == 0) ? (transformed * weight) : (transformed / weight);
        } else {
            checksum -= (i % 3 == 0) ? (weight * 2) : (std::abs(transformed) + weight);
        }
        
        weight = (weight < 4) ? (weight + 1) : 1;
    }
    
    std::cout << "Result: " << checksum << std::endl;
    return 0;
}