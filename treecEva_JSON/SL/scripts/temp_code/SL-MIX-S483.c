#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

typedef struct {
    double x;
    double y;
} Point;

typedef struct {
    Point points[3];
    int count;
} Triangle;

// Function to calculate area of triangle using Heron's formula
double triangle_area(Triangle* t) {
    Point a = t->points[0];
    Point b = t->points[1];
    Point c = t->points[2];
    
    double side_a = sqrt(pow(b.x - c.x, 2) + pow(b.y - c.y, 2));
    double side_b = sqrt(pow(a.x - c.x, 2) + pow(a.y - c.y, 2));
    double side_c = sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
    
    double s = (side_a + side_b + side_c) / 2;
    return sqrt(s * (s - side_a) * (s - side_b) * (s - side_c));
}

// Function to perform bit manipulation on an integer
int bit_transform(int value) {
    int xor_result = value ^ 0xFF;
    int shifted = (xor_result << 2) | (xor_result >> 3);
    return shifted & 0xFFFF;
}

int main() {
    // Initialize triangle
    Triangle t;
    t.count = 3;
    t.points[0].x = 0;
    t.points[0].y = 0;
    t.points[1].x = 3;
    t.points[1].y = 0;
    t.points[2].x = 0;
    t.points[2].y = 4;
    
    // Calculate base area
    double area = triangle_area(&t);
    
    // Perform bit operations on a derived value
    int derived_int = (int)(area * 100);
    int transformed = bit_transform(derived_int);
    
    // Perform complex mathematical computation
    double angle_rad = atan2(t.points[2].y, t.points[1].x);
    double sin_val = sin(angle_rad);
    double cos_val = cos(angle_rad);
    
    // Use string operations to create a key
    char buffer[MAX_LEN];
    snprintf(buffer, MAX_LEN, "%.0f-%d", area, transformed);
    int str_len = strlen(buffer);
    
    // Final calculation combining all values
    double result = (area * 1000) + (transformed / 100.0) + 
                   (sin_val * cos_val * 10000) + (str_len * M_PI);
    
    // Convert to integer and apply final transformation
    int final_int = (int)round(result);
    result = final_int ^ 0xABC;
    
    printf("Result: %.0f\n", result);
    return 0;
}