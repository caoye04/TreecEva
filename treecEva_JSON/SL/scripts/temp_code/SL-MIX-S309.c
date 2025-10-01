#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_SIZE 10

struct Point {
    double x;
    double y;
};

struct Triangle {
    struct Point vertices[3];
};

double calculate_distance(struct Point p1, struct Point p2) {
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

double triangle_perimeter(struct Triangle t) {
    return calculate_distance(t.vertices[0], t.vertices[1]) + 
           calculate_distance(t.vertices[1], t.vertices[2]) + 
           calculate_distance(t.vertices[2], t.vertices[0]);
}

int main() {
    struct Triangle triangles[MAX_SIZE];
    
    // Initialize triangle coordinates
    for(int i = 0; i < MAX_SIZE; i++) {
        triangles[i].vertices[0].x = i * 2.5;
        triangles[i].vertices[0].y = i * 3.7;
        triangles[i].vertices[1].x = i * 4.1 + 5.5;
        triangles[i].vertices[1].y = i * 2.8 + 3.3;
        triangles[i].vertices[2].x = i * 3.3 + 1.2;
        triangles[i].vertices[2].y = i * 4.4 + 2.7;
    }
    
    double perimeters[MAX_SIZE];
    double sum_perimeters = 0;
    
    // Calculate perimeters
    for(int i = 0; i < MAX_SIZE; i++) {
        perimeters[i] = triangle_perimeter(triangles[i]);
        sum_perimeters += perimeters[i];
    }
    
    double avg_perimeter = sum_perimeters / MAX_SIZE;
    
    // Perform bit operations on the integer part of average perimeter
    int int_part = (int)avg_perimeter;
    int bit_result = (int_part << 2) ^ (int_part >> 1);
    
    // Apply trigonometric transformation
    double trig_result = sin(bit_result) * cos(bit_result);
    
    // Combine results with logarithmic scaling
    double log_scale = log10(fabs(trig_result) + 1);
    
    // Final computation involving string-like manipulation through ASCII values
    char buffer[50];
    sprintf(buffer, "%.2f", log_scale);
    int ascii_sum = 0;
    for(int i = 0; buffer[i] != '\0'; i++) {
        ascii_sum += (int)buffer[i];
    }
    
    // Final result combines all transformations
    double result = round((bit_result * trig_result + ascii_sum) * 1000) / 1000;
    
    printf("Result: %.3f\n", result);
    return 0;
}