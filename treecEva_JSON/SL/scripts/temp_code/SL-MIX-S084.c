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
    Point p1 = t->points[0];
    Point p2 = t->points[1];
    Point p3 = t->points[2];
    
    // Calculate side lengths
    double a = sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
    double b = sqrt(pow(p3.x - p2.x, 2) + pow(p3.y - p2.y, 2));
    double c = sqrt(pow(p1.x - p3.x, 2) + pow(p1.y - p3.y, 2));
    
    // Semi-perimeter
    double s = (a + b + c) / 2;
    
    // Heron's formula
    return sqrt(s * (s - a) * (s - b) * (s - c));
}

// Function to perform bit manipulation
int bit_operation(int a, int b) {
    return (a & b) ^ ((a | b) << 1);
}

int main() {
    // Initialize triangle data
    Triangle t = {
        .points = {{0, 0}, {3, 0}, {0, 4}},
        .count = 3
    };
    
    // Perform area calculation
    double area = triangle_area(&t);
    
    // Perform bit operations on calculated values
    int val1 = (int)(area * 2);  // Should be 12
    int val2 = (int)(area * 3);  // Should be 18
    int bit_result = bit_operation(val1, val2);
    
    // String manipulation
    char buffer[MAX_LEN];
    snprintf(buffer, MAX_LEN, "Area: %.2f", area);
    int str_len = strlen(buffer);
    
    // Complex mathematical expression
    double expr1 = pow(area, 1.5) + log(area + 1);
    double expr2 = sin(area) * cos(area/2);
    
    // Final calculation combining all results
    int result = (int)((bit_result * str_len) + expr1 - expr2 * 100);
    
    printf("Result: %d\n", result);
    
    return 0;
}