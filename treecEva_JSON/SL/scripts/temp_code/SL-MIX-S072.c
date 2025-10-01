#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_ITERATIONS 5
#define MULTIPLIER 3

struct Point {
    double x;
    double y;
};

struct DataContainer {
    struct Point points[3];
    int count;
    double weights[3];
};

double calculateDistance(struct Point p1, struct Point p2) {
    double dx = p1.x - p2.x;
    double dy = p1.y - p2.y;
    return sqrt(dx*dx + dy*dy);
}

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    struct DataContainer container;
    container.count = 3;
    
    // Initialize points
    container.points[0].x = 1.0; container.points[0].y = 2.0;
    container.points[1].x = 4.0; container.points[1].y = 6.0;
    container.points[2].x = 7.0; container.points[2].y = 3.0;
    
    // Initialize weights
    container.weights[0] = 0.5;
    container.weights[1] = 1.2;
    container.weights[2] = 0.8;
    
    double distances[3];
    double weighted_sum = 0.0;
    int i, j;
    
    // Calculate distances between consecutive points
    for (i = 0; i < container.count - 1; i++) {
        distances[i] = calculateDistance(container.points[i], container.points[i+1]);
    }
    
    // Add distance from last to first point
    distances[2] = calculateDistance(container.points[2], container.points[0]);
    
    // Calculate weighted sum
    for (i = 0; i < container.count; i++) {
        weighted_sum += distances[i] * container.weights[i];
    }
    
    // Perform iterative transformation
    double accumulator = weighted_sum;
    for (i = 1; i <= MAX_ITERATIONS; i++) {
        accumulator = (accumulator * MULTIPLIER) - (double)factorial(i % 4);
        if (i % 2 == 0) {
            accumulator = fabs(accumulator) / 2.0;
        }
    }
    
    // Apply final transformation using bit operations
    int int_part = (int)accumulator;
    int xor_result = int_part ^ 0xF0F0;
    int shifted = xor_result << 2;
    
    double final_result = (double)shifted + fmod(accumulator, 1.0) * 100.0;
    
    printf("Result: %.2f\n", final_result);
    return 0;
}