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

double computeDistance(struct Point p1, struct Point p2) {
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
    for(int i=0; i<container.count-1; i++) {
        distances[i] = computeDistance(container.points[i], container.points[i+1]);
    }
    
    double accumulator = 0.0;
    for(int i=0; i<container.count-1; i++) {
        accumulator += distances[i] * container.weights[i];
    }
    
    int iterations = MAX_ITERATIONS;
    double transformed_value = accumulator;
    
    while(iterations > 0) {
        transformed_value = sin(transformed_value) * MULTIPLIER;
        if(transformed_value < 0) {
            transformed_value = fabs(transformed_value);
        }
        iterations--;
    }
    
    int fact_result = factorial(4);
    double final_result = pow(transformed_value, 1.5) + fact_result - (int)(transformed_value) % 7;
    
    printf("Result: %.6f\n", final_result);
    return 0;
}