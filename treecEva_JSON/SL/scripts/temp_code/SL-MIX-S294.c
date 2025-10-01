#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define M_PI 3.14159265358979323846

int main() {
    // Initialize complex nested data structure
    struct Point {
        double x, y;
    };
    
    struct Triangle {
        struct Point vertices[3];
        int id;
    };

    struct Triangle t = {
        {{1.0, 2.0}, {4.0, 6.0}, {7.0, 3.0}},
        42
    };

    // Perform calculations
    double side1 = sqrt(pow(t.vertices[1].x - t.vertices[0].x, 2) + pow(t.vertices[1].y - t.vertices[0].y, 2));
    double side2 = sqrt(pow(t.vertices[2].x - t.vertices[1].x, 2) + pow(t.vertices[2].y - t.vertices[1].y, 2));
    double side3 = sqrt(pow(t.vertices[0].x - t.vertices[2].x, 2) + pow(t.vertices[0].y - t.vertices[2].y, 2));
    
    double perimeter = side1 + side2 + side3;
    
    // Calculate area using Heron's formula
    double s = perimeter / 2;
    double area = sqrt(s * (s - side1) * (s - side2) * (s - side3));
    
    // Perform bitwise operations
    int bitwise_result = (t.id << 2) ^ (int)(perimeter) & 0xFF;
    
    // Trigonometric calculations
    double angle1 = acos((side2*side2 + side3*side3 - side1*side1) / (2 * side2 * side3));
    double angle2 = acos((side1*side1 + side3*side3 - side2*side2) / (2 * side1 * side3));
    double angle3 = M_PI - angle1 - angle2;
    
    double sin_sum = sin(angle1) + sin(angle2) + sin(angle3);
    
    // Pointer manipulation
    double *p_area = &area;
    int *p_id = &t.id;
    
    // Complex calculation combining all results
    long long intermediate = (long long)(*p_area * 1000) + (*p_id * 100) + (int)(sin_sum * 100);
    
    // Bitwise manipulation on intermediate result
    int shifted = (int)(intermediate >> 3);
    int masked = shifted & 0x1FF;
    
    // Final calculation
    int result = masked ^ bitwise_result;
    
    // TARGET_POINT
    printf("Result: %d\n", result);
    
    return 0;
}