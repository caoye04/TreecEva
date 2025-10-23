#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>

struct Point {
    double x, y;
};

struct Circle {
    Point center;
    double radius;
};

// Function to calculate Euclidean distance between two points
double euclidean_distance(const Point& a, const Point& b) {
    return std::sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y));
}

// Check if line segment intersects circle
bool intersects(const Point& p1, const Point& p2, const Circle& circle) {
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    double a = dx*dx + dy*dy;
    double b = 2*(dx*(p1.x - circle.center.x) + dy*(p1.y - circle.center.y));
    double c = (p1.x - circle.center.x)*(p1.x - circle.center.x) + 
               (p1.y - circle.center.y)*(p1.y - circle.center.y) - 
               circle.radius*circle.radius;
    double discriminant = b*b - 4*a*c;
    return discriminant >= 0;
}

int main() {
    // Waypoints
    std::vector<Point> waypoints = {{0,0}, {3,4}, {7,1}, {10,5}};
    std::vector<double> energy_costs = {1.2, 2.5, 1.8, 3.0};
    
    // Obstacles
    std::vector<Circle> obstacles = {{{5, 3}, 1.0}};
    
    // Calculate distances
    std::vector<double> distances;
    for(size_t i=0; i<waypoints.size()-1; ++i){
        distances.push_back(euclidean_distance(waypoints[i], waypoints[i+1]));
    }
    
    // Mean of distances
    double sum_distances = std::accumulate(distances.begin(), distances.end(), 0.0);
    double mean_distance = sum_distances / distances.size();
    
    // Variance of energy costs
    double mean_energy = std::accumulate(energy_costs.begin(), energy_costs.end(), 0.0) / energy_costs.size();
    double sq_sum = std::inner_product(energy_costs.begin(), energy_costs.end(), energy_costs.begin(), 0.0);
    double variance_energy = sq_sum / energy_costs.size() - mean_energy * mean_energy;
    
    // Check for intersections
    bool collision = false;
    for(const auto& obs : obstacles){
        for(size_t i=0; i<waypoints.size()-1; ++i){
            if(intersects(waypoints[i], waypoints[i+1], obs)){
                collision = true;
                break;
            }
        }
        if(collision) break;
    }
    
    // Compute path efficiency
    double path_efficiency = mean_distance - variance_energy;
    if(collision){
        path_efficiency *= 0.5; // Apply penalty
    }
    
    std::cout << "Result: " << path_efficiency << std::endl;
    return 0;
}