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

struct Polygon {
    struct Point vertices[MAX_SIZE];
    int count;
};

struct ComplexShape {
    struct Polygon outer;
    struct Polygon inner[MAX_SIZE];
    int inner_count;
};

// Function to calculate distance between two points
double distance(struct Point a, struct Point b) {
    return sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2));
}

// Function to calculate perimeter of a polygon
double perimeter(struct Polygon p) {
    if (p.count < 2) return 0;
    double perim = 0;
    for (int i = 0; i < p.count; i++) {
        int next = (i + 1) % p.count;
        perim += distance(p.vertices[i], p.vertices[next]);
    }
    return perim;
}

// Function to calculate area using shoelace formula
double area(struct Polygon p) {
    if (p.count < 3) return 0;
    double a = 0;
    for (int i = 0; i < p.count; i++) {
        int next = (i + 1) % p.count;
        a += p.vertices[i].x * p.vertices[next].y;
        a -= p.vertices[next].x * p.vertices[i].y;
    }
    return fabs(a) / 2;
}

int main() {
    struct ComplexShape shape;
    
    // Initialize outer polygon (a square)
    shape.outer.count = 4;
    shape.outer.vertices[0].x = 0; shape.outer.vertices[0].y = 0;
    shape.outer.vertices[1].x = 4; shape.outer.vertices[1].y = 0;
    shape.outer.vertices[2].x = 4; shape.outer.vertices[2].y = 4;
    shape.outer.vertices[3].x = 0; shape.outer.vertices[3].y = 4;
    
    // Initialize inner polygons
    shape.inner_count = 2;
    
    // First inner polygon (a triangle)
    shape.inner[0].count = 3;
    shape.inner[0].vertices[0].x = 1; shape.inner[0].vertices[0].y = 1;
    shape.inner[0].vertices[1].x = 2; shape.inner[0].vertices[1].y = 1;
    shape.inner[0].vertices[2].x = 1.5; shape.inner[0].vertices[2].y = 2;
    
    // Second inner polygon (a rectangle)
    shape.inner[1].count = 4;
    shape.inner[1].vertices[0].x = 2.5; shape.inner[1].vertices[0].y = 2.5;
    shape.inner[1].vertices[1].x = 3.5; shape.inner[1].vertices[1].y = 2.5;
    shape.inner[1].vertices[2].x = 3.5; shape.inner[1].vertices[2].y = 3.5;
    shape.inner[1].vertices[3].x = 2.5; shape.inner[1].vertices[3].y = 3.5;
    
    // Calculate metrics
    double outer_perimeter = perimeter(shape.outer);
    double outer_area = area(shape.outer);
    
    double total_inner_perimeter = 0;
    double total_inner_area = 0;
    
    for (int i = 0; i < shape.inner_count; i++) {
        total_inner_perimeter += perimeter(shape.inner[i]);
        total_inner_area += area(shape.inner[i]);
    }
    
    // Perform complex calculations
    double ratio = outer_area / total_inner_area;
    double diff = outer_perimeter - total_inner_perimeter;
    
    // Bitwise operations
    int bitwise_a = (int)(ratio * 100);
    int bitwise_b = (int)(diff * 10);
    int bitwise_result = (bitwise_a << 2) ^ (bitwise_b >> 1);
    
    // Mathematical operations
    double log_val = log10(ratio);
    double exp_val = exp(log_val);
    double trig_val = sin(M_PI / 4) * cos(M_PI / 4);
    
    // Final calculation
    int final_result = (int)((exp_val * 1000) + (trig_val * 100) + bitwise_result);
    
    printf("Result: %d\n", final_result);
    return 0;
}