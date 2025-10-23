#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>

struct Waypoint {
    double x, y;
    Waypoint(double x_, double y_) : x(x_), y(y_) {}
};

double calculateEuclideanDistance(const Waypoint& a, const Waypoint& b) {
    return std::sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

double calculateTerrainFactor(const std::vector<Waypoint>& waypoints) {
    if (waypoints.size() < 2) return 0.0;
    std::vector<double> diffs;
    for (size_t i = 1; i < waypoints.size(); ++i) {
        diffs.push_back(std::abs(waypoints[i].x - waypoints[i-1].x));
    }
    double sum = std::accumulate(diffs.begin(), diffs.end(), 0.0);
    return sum / diffs.size();
}

enum class RobotState { MOVING, CHARGING, IDLE };

int main() {
    std::vector<Waypoint> navigationPath = {
        Waypoint(0.0, 0.0),
        Waypoint(3.0, 4.0),
        Waypoint(7.0, 1.0),
        Waypoint(10.0, 5.0)
    };
    
    double terrainFactor = calculateTerrainFactor(navigationPath);
    RobotState currentState = RobotState::MOVING;
    double total_energy_consumed = 0.0;
    
    for (size_t i = 1; i < navigationPath.size(); ++i) {
        double segmentDistance = calculateEuclideanDistance(navigationPath[i-1], navigationPath[i]);
        double energyConsumption = segmentDistance * terrainFactor;
        
        if (currentState == RobotState::CHARGING) {
            total_energy_consumed += 2.0;
            currentState = RobotState::MOVING;
        }
        
        total_energy_consumed += energyConsumption;
        
        currentState = (energyConsumption > 10.0) ? RobotState::CHARGING : RobotState::MOVING;
    }
    
    if (currentState == RobotState::CHARGING) {
        total_energy_consumed += 2.0;
    }
    
    currentState = RobotState::IDLE;
    
    std::cout << "Result: " << total_energy_consumed << std::endl;
    return 0;
}