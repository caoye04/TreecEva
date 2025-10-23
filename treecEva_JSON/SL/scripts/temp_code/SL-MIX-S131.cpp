#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <memory>

struct Waypoint {
    double x, y;
    Waypoint(double x, double y) : x(x), y(y) {}
};

class Robot {
public:
    int navigation_score = 0;
    
    void processWaypoints(std::shared_ptr<Waypoint> points[], int size) {
        for (int i = 0; i < size; ++i) {
            int quadrant = determineQuadrant(points[i]->x, points[i]->y);
            switch(quadrant) {
                case 1:
                    navigation_score += static_cast<int>(std::ceil(points[i]->x + points[i]->y));
                    break;
                case 2:
                    navigation_score += static_cast<int>(std::floor(points[i]->y - points[i]->x));
                    break;
                case 3:
                    navigation_score += static_cast<int>(std::round(points[i]->x * points[i]->y));
                    break;
                case 4:
                    navigation_score += static_cast<int>(std::abs(points[i]->x) + std::abs(points[i]->y));
                    break;
                default:
                    navigation_score -= 10; // Penalty for origin or axis
            }
        }
    }
    
private:
    int determineQuadrant(double x, double y) {
        if (x > 0 && y >= 0) return 1;
        if (x <= 0 && y > 0) return 2;
        if (x < 0 && y <= 0) return 3;
        if (x >= 0 && y < 0) return 4;
        return 0; // Origin or axis
    }
};

int main() {
    auto wp1 = std::make_shared<Waypoint>(3.5, 4.2);
    auto wp2 = std::make_shared<Waypoint>(-2.1, 3.7);
    auto wp3 = std::make_shared<Waypoint>(-1.8, -5.3);
    auto wp4 = std::make_shared<Waypoint>(4.0, -1.2);
    auto wp5 = std::make_shared<Waypoint>(0.0, 0.0);
    
    std::shared_ptr<Waypoint> waypoints[] = {wp1, wp2, wp3, wp4, wp5};
    
    Robot robot;
    robot.processWaypoints(waypoints, 5);
    
    std::cout << "Result: " << robot.navigation_score << std::endl;
    return 0;
}