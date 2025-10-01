#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

typedef struct {
    int x;
    int y;
    double z;
} Point;

typedef struct {
    Point points[3];
    int count;
} Polygon;

int complex_operation(int a, int b) {
    return (a * b) + (a ^ b) - (a << 1) + (b >> 2);
}

double calculate_distance(Point p1, Point p2) {
    double dx = p1.x - p2.x;
    double dy = p1.y - p2.y;
    return sqrt(dx*dx + dy*dy);
}

int main() {
    Polygon shape;
    shape.count = 3;
    
    // Initialize points
    shape.points[0].x = 5;
    shape.points[0].y = 12;
    shape.points[0].z = 3.14;
    
    shape.points[1].x = shape.points[0].x * 2;
    shape.points[1].y = shape.points[0].y - 5;
    shape.points[1].z = shape.points[0].z * 2.0;
    
    shape.points[2].x = complex_operation(shape.points[0].x, shape.points[1].x);
    shape.points[2].y = shape.points[0].y | shape.points[1].y;
    shape.points[2].z = pow(shape.points[0].z, 3);
    
    // Perform calculations
    double distances[3];
    distances[0] = calculate_distance(shape.points[0], shape.points[1]);
    distances[1] = calculate_distance(shape.points[1], shape.points[2]);
    distances[2] = calculate_distance(shape.points[2], shape.points[0]);
    
    // String manipulation
    char buffer[MAX_LEN];
    snprintf(buffer, MAX_LEN, "P1:(%d,%d) P2:(%d,%d) P3:(%d,%d)", 
             shape.points[0].x, shape.points[0].y,
             shape.points[1].x, shape.points[1].y,
             shape.points[2].x, shape.points[2].y);
    
    int str_len = strlen(buffer);
    
    // Final calculation
    int sum_coords = 0;
    for(int i = 0; i < shape.count; i++) {
        sum_coords += shape.points[i].x + shape.points[i].y;
    }
    
    double perimeter = distances[0] + distances[1] + distances[2];
    
    int final_result = ((int)perimeter) ^ (sum_coords & 0xFF) ^ str_len;
    
    printf("Result: %d\n", final_result);
    return 0;
}