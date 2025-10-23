#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <queue>
#include <stack>

template<int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

template<>
struct Factorial<0> {
    static constexpr int value = 1;
};

constexpr int calculateCombinations(int n, int k) {
    return Factorial<n>::value / (Factorial<k>::value * Factorial<n - k>::value);
}

struct Point {
    int x, y;
    Point() : x(0), y(0) {}
    Point(int x_, int y_) : x(x_), y(y_) {}
    
    double distanceTo(const Point& other) const {
        int dx = x - other.x;
        int dy = y - other.y;
        return std::sqrt(dx*dx + dy*dy);
    }
};

struct Node {
    Point position;
    Node* next;
    Node(Point p) : position(p), next(nullptr) {}
};

int main() {
    // Initialize robot's starting position and target
    Point robot(0, 0);
    Point target(10, 10);
    
    // Create a linked list representing possible waypoints
    Node* head = new Node(Point(2, 3));
    head->next = new Node(Point(5, 5));
    head->next->next = new Node(Point(8, 7));
    head->next->next->next = new Node(Point(10, 10));
    
    // Navigation parameters
    const int totalWaypoints = 4;
    const int selectedPaths = 3;
    
    // Calculate number of possible path combinations
    int pathCombinations = calculateCombinations(totalWaypoints, selectedPaths);
    
    // Obstacle map represented as bitmask flags
    const unsigned int obstacleMap = 0b10101010;
    const unsigned int pathFlags = 0b11001100;
    
    // Check if path is clear using short-circuit evaluation
    bool pathClear = (obstacleMap & pathFlags) == 0 && (pathCombinations > 0);
    
    // Initialize navigation containers
    std::queue<Point> navigationQueue;
    std::stack<double> distanceStack;
    
    // Populate queue with waypoints
    Node* current = head;
    while (current != nullptr) {
        navigationQueue.push(current->position);
        current = current->next;
    }
    
    // Calculate distances and push to stack
    Point previousPoint = robot;
    while (!navigationQueue.empty()) {
        Point currentPoint = navigationQueue.front();
        navigationQueue.pop();
        
        double segmentDistance = previousPoint.distanceTo(currentPoint);
        distanceStack.push(segmentDistance);
        previousPoint = currentPoint;
    }
    
    // Calculate total geometric distance
    double totalGeometricDistance = 0.0;
    while (!distanceStack.empty()) {
        totalGeometricDistance += distanceStack.top();
        distanceStack.pop();
    }
    
    // Apply combinatorial factor and obstacle penalty
    int obstaclePenalty = __builtin_popcount(obstacleMap & pathFlags); // Count set bits
    
    // Final path cost calculation
    int finalPathCost = 0;
    if (pathClear || (pathCombinations > 5 && obstaclePenalty < 3)) {
        finalPathCost = static_cast<int>(totalGeometricDistance * pathCombinations) - (obstaclePenalty * 10);
    } else {
        finalPathCost = static_cast<int>(totalGeometricDistance * pathCombinations) + (obstaclePenalty * 20);
    }
    
    // Clean up linked list
    current = head;
    while (current != nullptr) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }
    
    std::cout << "Result: " << finalPathCost << std::endl;
    return 0;
}