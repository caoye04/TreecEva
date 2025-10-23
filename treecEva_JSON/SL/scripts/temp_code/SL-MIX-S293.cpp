#define _USE_MATH_DEFINES
#include <iostream>
#include <optional>

class ThermalZone {
public:
    double raw_temp;
    int zone_id;
    
    ThermalZone(double temp, int id) : raw_temp(temp), zone_id(id) {}
    
    // Operator overloading for averaging
    ThermalZone operator+(const ThermalZone& other) const {
        return ThermalZone(raw_temp + other.raw_temp, zone_id);
    }
    
    ThermalZone operator/(double divisor) const {
        return ThermalZone(raw_temp / divisor, zone_id);
    }
};

std::optional<double> calibrate(int zone_id, double reading) {
    double calibrated;
    switch(zone_id) {
        case 1:
            calibrated = reading * 1.05;
            break;
        case 2:
            calibrated = reading * 0.98;
            break;
        case 3:
            calibrated = reading * 1.02;
            break;
        default:
            return std::nullopt;
    }
    return calibrated;
}

int main() {
    ThermalZone zone1(25.4, 1);
    ThermalZone zone2(27.8, 2);
    ThermalZone zone3(26.1, 3);
    
    auto calibrated1 = calibrate(zone1.zone_id, zone1.raw_temp);
    auto calibrated2 = calibrate(zone2.zone_id, zone2.raw_temp);
    auto calibrated3 = calibrate(zone3.zone_id, zone3.raw_temp);
    
    if (calibrated1 && calibrated2 && calibrated3) {
        // Divide and conquer approach to compute average
        double sum12 = (*calibrated1 + *calibrated2).raw_temp;
        double avg12 = sum12 / 2.0;
        double total_sum = avg12 * 2 + *calibrated3;
        double final_avg = total_sum / 3.0;
        
        std::cout << "Result: " << final_avg << std::endl;
    }
    
    return 0;
}