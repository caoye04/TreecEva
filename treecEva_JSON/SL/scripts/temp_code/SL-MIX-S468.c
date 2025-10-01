#define M_PI 3.14159265358979323846
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

int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

double calculate_distance(Point a, Point b) {
    return sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2));
}

int main() {
    Polygon shape;
    shape.count = 3;
    
    // Initialize points
    shape.points[0].x = 1;
    shape.points[0].y = 1;
    shape.points[0].z = 2.5;
    
    shape.points[1].x = 4;
    shape.points[1].y = 5;
    shape.points[1].z = 3.7;
    
    shape.points[2].x = 7;
    shape.points[2].y = 2;
    shape.points[2].z = 1.9;
    
    // Perform calculations
    double distances[3];
    distances[0] = calculate_distance(shape.points[0], shape.points[1]);
    distances[1] = calculate_distance(shape.points[1], shape.points[2]);
    distances[2] = calculate_distance(shape.points[2], shape.points[0]);
    
    double perimeter = distances[0] + distances[1] + distances[2];
    
    // Bitwise operations
    int a = 29;  // Binary: 11101
    int b = 15;  // Binary: 01111
    int bitwise_result = (a & b) | ((a ^ b) << 2);
    
    // Mathematical operations
    double angle = 45.0;
    double radians = angle * M_PI / 180.0;
    double trig_result = sin(radians) * cos(radians) * 100;
    
    // String operations
    char str1[MAX_LEN] = "Hello";
    char str2[MAX_LEN] = "World";
    strcat(str1, str2);
    int str_length = strlen(str1);
    
    // Complex calculation combining all results
    int factorial_result = factorial(5);
    double weighted_sum = (perimeter * 2.5) + (bitwise_result * 1.8) + 
                         (trig_result * 3.2) + (str_length * 4.1);
    
    int final_result = (int)(weighted_sum + factorial_result) % 1000;
    
    printf("Result: %d\n", final_result);
    return 0;
}