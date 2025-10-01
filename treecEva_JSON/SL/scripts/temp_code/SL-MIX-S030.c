#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

typedef struct {
    int x;
    int y;
    double magnitude;
} Point;

typedef struct {
    Point points[3];
    int count;
} Polygon;

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

double distance(Point a, Point b) {
    int dx = a.x - b.x;
    int dy = a.y - b.y;
    return sqrt(dx*dx + dy*dy);
}

int process_polygon(Polygon* poly) {
    double perimeter = 0;
    for(int i = 0; i < poly->count - 1; i++) {
        perimeter += distance(poly->points[i], poly->points[i+1]);
    }
    perimeter += distance(poly->points[poly->count-1], poly->points[0]);
    return (int)floor(perimeter);
}

int main() {
    Polygon shape;
    shape.count = 3;
    
    // Initialize points
    shape.points[0].x = 0;
    shape.points[0].y = 0;
    shape.points[1].x = 3;
    shape.points[1].y = 4;
    shape.points[2].x = 4;
    shape.points[2].y = 0;
    
    // Calculate magnitudes
    for(int i = 0; i < shape.count; i++) {
        shape.points[i].magnitude = sqrt(shape.points[i].x * shape.points[i].x + shape.points[i].y * shape.points[i].y);
    }
    
    // Perform complex calculation
    int perimeter_value = process_polygon(&shape);
    int sum_magnitudes = 0;
    for(int i = 0; i < shape.count; i++) {
        sum_magnitudes += (int)round(shape.points[i].magnitude);
    }
    
    // Bitwise and arithmetic operations
    int a = 0xF0;  // 240 in decimal
    int b = 0x0F;  // 15 in decimal
    int bitwise_result = (a & b) | ((a << 2) ^ (b >> 1));
    
    // Mathematical operations
    double trig_result = sin(M_PI/2) + cos(0) + tan(M_PI/4);
    int trig_int = (int)round(trig_result * 100);
    
    // Final calculation
    int factorial_result = factorial(5);
    int final_result = (perimeter_value + sum_magnitudes) * bitwise_result + trig_int - factorial_result;
    
    printf("Result: %d\n", final_result);
    return 0;
}