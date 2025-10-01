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
    Point* points;
    int count;
} Polygon;

int compute_hash(const char* str) {
    int hash = 0;
    for (int i = 0; i < strlen(str); i++) {
        hash = (hash << 5) - hash + str[i]; // hash * 31 + str[i]
    }
    return hash;
}

int determinant(Point p1, Point p2, Point p3) {
    return (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y);
}

int main() {
    // Initialize polygon data
    Point vertices[] = {{0, 0}, {4, 0}, {4, 3}, {0, 3}};
    Polygon poly;
    poly.points = vertices;
    poly.count = sizeof(vertices)/sizeof(vertices[0]);

    // Compute perimeter using Euclidean distance
    double perimeter = 0.0;
    for(int i=0; i<poly.count; i++) {
        Point p1 = poly.points[i];
        Point p2 = poly.points[(i+1)%poly.count];
        double dx = p2.x - p1.x;
        double dy = p2.y - p1.y;
        perimeter += sqrt(dx*dx + dy*dy);
    }

    // Calculate area using shoelace formula
    int area = 0;
    for(int i=0; i<poly.count; i++) {
        Point p1 = poly.points[i];
        Point p2 = poly.points[(i+1)%poly.count];
        area += (p1.x * p2.y - p2.x * p1.y);
    }
    area = abs(area) / 2;

    // Perform bitwise transformations
    int hash_val = compute_hash("rectangle");
    int transformed = ((hash_val & 0xFF) ^ (hash_val >> 8)) | (area << 4);

    // Apply mathematical operations
    double log_area = log((double)area + 1);
    int final_shift = (int)(perimeter * sin(log_area));
    
    // Final computation combining all factors
    int result = (transformed & 0xFFFF) + (final_shift << 2) - (int)perimeter;
    
    printf("Result: %d\n", result);
    return 0;
}