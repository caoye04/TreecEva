#define _USE_MATH_DEFINES
#include <iostream>
#include <unordered_map>
#include <cmath>

struct Vehicle {
    int baseSpeed;
    int priorityModifier;
    
    constexpr Vehicle(int speed = 0, int mod = 0) : baseSpeed(speed), priorityModifier(mod) {}
    
    constexpr int calculateBasePriority() const {
        return baseSpeed * priorityModifier;
    }
};

constexpr Vehicle operator+(const Vehicle& v1, const Vehicle& v2) {
    return Vehicle(v1.baseSpeed + v2.baseSpeed, v1.priorityModifier + v2.priorityModifier);
}

class ZoneNode {
public:
    int congestionLevel;
    ZoneNode* next;
    
    ZoneNode(int level) : congestionLevel(level), next(nullptr) {}
};

int main() {
    std::unordered_map<int, Vehicle> vehicleRegistry;
    vehicleRegistry[1] = Vehicle(60, 2);  // Standard car
    vehicleRegistry[2] = Vehicle(40, 3);  // Truck
    vehicleRegistry[3] = Vehicle(80, 1);  // Motorcycle
    
    // Build linked list of zones
    ZoneNode* head = new ZoneNode(3);
    head->next = new ZoneNode(5);
    head->next->next = new ZoneNode(2);
    
    int vehicleID = 2;
    int timeOfDay = 14; // 2 PM
    int finalPriorityScore = 0;
    
    if (vehicleRegistry.find(vehicleID) != vehicleRegistry.end()) {
        Vehicle v = vehicleRegistry[vehicleID];
        int basePriority = v.calculateBasePriority();
        
        ZoneNode* current = head;
        int zoneMultiplier = 1;
        
        while (current != nullptr && basePriority > 0) {
            int congestionImpact = 0;
            
            switch(current->congestionLevel) {
                case 1: case 2:
                    congestionImpact = 1;
                    break;
                case 3: case 4:
                    congestionImpact = 2;
                    break;
                case 5:
                    congestionImpact = 3;
                    break;
                default:
                    congestionImpact = 0;
            }
            
            bool isPeakHour = (timeOfDay >= 7 && timeOfDay <= 9) || (timeOfDay >= 17 && timeOfDay <= 19);
            int timeAdjustment = isPeakHour ? 2 : 1;
            
            int zoneScore = (basePriority / congestionImpact) * timeAdjustment;
            finalPriorityScore += zoneScore * zoneMultiplier;
            
            if (zoneScore > 50) {
                finalPriorityScore += 10;
                break;
            }
            
            current = current->next;
            zoneMultiplier++;
            basePriority -= 10;
        }
        
        finalPriorityScore = (finalPriorityScore > 100) ? finalPriorityScore/2 : finalPriorityScore;
    }
    
    // Clean up linked list
    while (head != nullptr) {
        ZoneNode* temp = head;
        head = head->next;
        delete temp;
    }
    
    std::cout << "Result: " << finalPriorityScore << std::endl;
    return 0;
}