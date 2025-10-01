#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    Point points[3];
    int count;
} Polygon;

int calculate_area(Polygon* poly) {
    int area = 0;
    for(int i=0; i<poly->count; i++) {
        area += poly->points[i].x * poly->points[(i+1)%poly->count].y;
        area -= poly->points[i].y * poly->points[(i+1)%poly->count].x;
    }
    return abs(area) / 2;
}

int main() {
    Polygon shape;
    shape.count = 3;
    
    // Initialize points
    shape.points[0].x = 0;
    shape.points[0].y = 0;
    shape.points[1].x = 4;
    shape.points[1].y = 0;
    shape.points[2].x = 2;
    shape.points[2].y = 3;
    
    int base_area = calculate_area(&shape);
    
    char buffer[MAX_LEN];
    snprintf(buffer, MAX_LEN, "%d", base_area);
    int len = strlen(buffer);
    
    // Perform some bitwise operations
    int mask = (1 << len) - 1;
    int shifted = base_area << 2;
    int masked_result = shifted & mask;
    
    // Apply mathematical transformations
    double sqrt_val = sqrt((double)masked_result);
    int final_int = (int)ceil(sqrt_val);
    
    // Combine with string length in a complex expression
    int result = ((final_int * len) + (base_area ^ len)) & 0xFF;
    
    printf("Result: %d\n", result);
    return 0;
}