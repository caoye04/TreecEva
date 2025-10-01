#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_SIZE 10

struct Point {
    double x;
    double y;
};

struct CalculationContext {
    struct Point points[MAX_SIZE];
    int count;
    double factors[3];
    char identifier[20];
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
    struct CalculationContext ctx;
    
    // Initialize points
    ctx.points[0].x = 3.0;
    ctx.points[0].y = 4.0;
    ctx.points[1].x = 0.0;
    ctx.points[1].y = 0.0;
    ctx.points[2].x = 5.0;
    ctx.points[2].y = 12.0;
    ctx.count = 3;
    
    // Set factors
    ctx.factors[0] = 2.5;
    ctx.factors[1] = -1.5;
    ctx.factors[2] = 0.5;
    
    strcpy(ctx.identifier, "COMPLEX_CALC");
    
    // Perform calculations
    double distances[3];
    distances[0] = calculateDistance(ctx.points[0], ctx.points[1]);
    distances[1] = calculateDistance(ctx.points[1], ctx.points[2]);
    distances[2] = calculateDistance(ctx.points[0], ctx.points[2]);
    
    double sum_of_distances = 0;
    for (int i = 0; i < ctx.count; i++) {
        sum_of_distances += distances[i];
    }
    
    // Apply factors with bit operations
    int mask = 0xF0;  // 240 in decimal
    int shifted = mask >> 2;  // Right shift by 2 positions
    
    double weighted_sum = 0;
    for (int i = 0; i < 3; i++) {
        int factor_multiplier = (i+1) << (i%2);  // Left shift based on index
        weighted_sum += ctx.factors[i] * factorial(factor_multiplier);
    }
    
    // Final computation
    double intermediate = pow(sum_of_distances, 1.5) + sin(M_PI/4);
    long long result = (long long)(intermediate * weighted_sum) ^ shifted;  // XOR with shifted value
    
    printf("Result: %lld\n", result);
    return 0;
}