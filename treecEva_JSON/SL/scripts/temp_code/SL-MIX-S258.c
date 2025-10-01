#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    double x;
    double y;
};

struct Triangle {
    struct Point vertices[3];
};

struct DataContainer {
    int values[5];
    struct Triangle shape;
    char label[20];
};

int complex_operation(int a, int b) {
    return (a * b) + (a ^ b) - (a << 1) + (b >> 2);
}

double calculate_area(struct Triangle t) {
    struct Point p1 = t.vertices[0];
    struct Point p2 = t.vertices[1];
    struct Point p3 = t.vertices[2];
    
    double area = 0.5 * fabs((p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)));
    return area;
}

int main() {
    struct DataContainer container;
    
    // Initialize values
    for(int i = 0; i < 5; i++) {
        container.values[i] = i * i + 3 * i - 2;
    }
    
    // Set up triangle vertices
    container.shape.vertices[0].x = 0.0;
    container.shape.vertices[0].y = 0.0;
    container.shape.vertices[1].x = 5.0;
    container.shape.vertices[1].y = 0.0;
    container.shape.vertices[2].x = 0.0;
    container.shape.vertices[2].y = 4.0;
    
    strcpy(container.label, "TestShape");
    
    // Perform complex calculations
    int intermediate = complex_operation(container.values[2], container.values[4]);
    
    // Bitwise manipulation
    int mask = 0xF0;
    intermediate = (intermediate & mask) | ((intermediate >> 4) & 0x0F);
    
    // Mathematical operations
    double area = calculate_area(container.shape);
    double sqrt_area = sqrt(area);
    
    // String processing
    int label_length = strlen(container.label);
    int char_sum = 0;
    for(int i = 0; i < label_length; i++) {
        char_sum += container.label[i];
    }
    
    // Final complex computation
    int final_result = (int)(sqrt_area * 100) + (intermediate ^ char_sum) - (container.values[1] << 2);
    
    printf("Result: %d\n", final_result);
    return 0;
}