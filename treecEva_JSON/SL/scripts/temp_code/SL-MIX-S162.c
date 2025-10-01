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
    char tag[20];
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
    
    strcpy(ctx.tag, "COMPUTE");
    
    // Perform calculations
    double distances[3];
    distances[0] = computeDistance(ctx.points[0], ctx.points[1]);
    distances[1] = computeDistance(ctx.points[1], ctx.points[2]);
    distances[2] = computeDistance(ctx.points[0], ctx.points[2]);
    
    // Apply factors
    double weighted_sum = 0;
    for (int i = 0; i < 3; i++) {
        weighted_sum += distances[i] * ctx.factors[i];
    }
    
    // Bitwise operations
    int bit_pattern = ((int)(weighted_sum * 10)) & 0xFF;
    int shifted = bit_pattern << 2;
    int masked = shifted & 0xF0;
    
    // Mathematical operations
    double trig_result = sin(M_PI / 6) * cos(M_PI / 3);
    int fact_result = factorial(5);
    
    // Final computation
    double result = (weighted_sum + masked + trig_result * fact_result) / 2.0;
    
    // Adjust based on tag
    if (strcmp(ctx.tag, "COMPUTE") == 0) {
        result = result * 1.5 - 10;
    } else {
        result = result / 2.0 + 5;
    }
    
    printf("Result: %.2f\n", result);
    return 0;
}