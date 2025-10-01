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
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

double distance(Point a, Point b) {
    return sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2));
}

int process_polygon(Polygon* poly) {
    int i;
    double perimeter = 0;
    for (i = 0; i < poly->count - 1; i++) {
        perimeter += distance(poly->points[i], poly->points[i+1]);
    }
    perimeter += distance(poly->points[poly->count-1], poly->points[0]);
    return (int)(perimeter * 100); // Convert to cents
}

int main() {
    Polygon shape;
    int i, j;
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int temp_matrix[3][3];
    int determinant = 0;
    double angles[5] = {0, M_PI/6, M_PI/4, M_PI/3, M_PI/2};
    double trig_sum = 0;
    char buffer[MAX_LEN];
    int final_result = 0;
    
    // Initialize polygon
    shape.count = 3;
    shape.points[0].x = 0; shape.points[0].y = 0; shape.points[0].z = 0;
    shape.points[1].x = 3; shape.points[1].y = 4; shape.points[1].z = 0;
    shape.points[2].x = 6; shape.points[2].y = 0; shape.points[2].z = 0;
    
    // Calculate determinant of matrix
    for (i = 0; i < 3; i++) {
        determinant += (matrix[0][i] * (matrix[1][(i+1)%3] * matrix[2][(i+2)%3] - matrix[1][(i+2)%3] * matrix[2][(i+1)%3]));
    }
    
    // Transpose matrix
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            temp_matrix[j][i] = matrix[i][j];
        }
    }
    
    // Calculate sum of trigonometric functions
    for (i = 0; i < 5; i++) {
        trig_sum += sin(angles[i]) * cos(angles[i]);
    }
    
    // Process polygon
    int perimeter_cents = process_polygon(&shape);
    
    // Bitwise operations
    int bitwise_result = (determinant & 0xF) | ((int)(trig_sum * 100) ^ 0xAA);
    
    // String operations
    sprintf(buffer, "%d", perimeter_cents);
    int str_length = strlen(buffer);
    
    // Complex calculation
    final_result = factorial(str_length) + (bitwise_result << 2) - (perimeter_cents % 17);
    
    printf("Result: %d\n", final_result);
    return 0;
}