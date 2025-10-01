#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    double x;
    double y;
};

struct Polygon {
    struct Point vertices[4];
    int count;
};

struct DataContainer {
    struct Polygon shapes[2];
    int active;
    double* dynamic_values;
};

double calculate_distance(struct Point* a, struct Point* b) {
    double dx = a->x - b->x;
    double dy = a->y - b->y;
    return sqrt(dx*dx + dy*dy);
}

int process_polygon(struct Polygon* poly, double* values) {
    int i;
    double perimeter = 0.0;
    for (i = 0; i < poly->count - 1; i++) {
        perimeter += calculate_distance(&poly->vertices[i], &poly->vertices[i+1]);
    }
    perimeter += calculate_distance(&poly->vertices[poly->count-1], &poly->vertices[0]);
    
    int count = 0;
    for (i = 0; i < poly->count; i++) {
        if (poly->vertices[i].x > 0 && poly->vertices[i].y > 0) {
            values[count++] = perimeter * (poly->vertices[i].x + poly->vertices[i].y);
        }
    }
    return count;
}

int main() {
    struct DataContainer container;
    double static_values[8];
    double dynamic_array[10];
    
    // Initialize first polygon (square)
    container.shapes[0].vertices[0].x = 1.0; container.shapes[0].vertices[0].y = 1.0;
    container.shapes[0].vertices[1].x = 1.0; container.shapes[0].vertices[1].y = 3.0;
    container.shapes[0].vertices[2].x = 3.0; container.shapes[0].vertices[2].y = 3.0;
    container.shapes[0].vertices[3].x = 3.0; container.shapes[0].vertices[3].y = 1.0;
    container.shapes[0].count = 4;
    
    // Initialize second polygon (triangle)
    container.shapes[1].vertices[0].x = 0.0; container.shapes[1].vertices[0].y = 0.0;
    container.shapes[1].vertices[1].x = 4.0; container.shapes[1].vertices[1].y = 0.0;
    container.shapes[1].vertices[2].x = 2.0; container.shapes[1].vertices[2].y = 3.0;
    container.shapes[1].count = 3;
    
    container.active = 1;
    container.dynamic_values = dynamic_array;
    
    double collected_values[16];
    int total_collected = 0;
    
    int i, j;
    for (i = 0; i <= container.active; i++) {
        double temp_values[8];
        int count = process_polygon(&container.shapes[i], temp_values);
        for (j = 0; j < count; j++) {
            collected_values[total_collected++] = temp_values[j];
        }
    }
    
    // Perform bit operations on collected data
    unsigned int bit_mask = 0xF0F0;
    unsigned int shifted_mask = bit_mask << 3;
    unsigned int xor_result = shifted_mask ^ 0xAAAA;
    
    // Calculate statistical measures
    double sum = 0.0;
    double product = 1.0;
    for (i = 0; i < total_collected; i++) {
        sum += collected_values[i];
        product *= (collected_values[i] > 0) ? collected_values[i] : 1.0;
    }
    
    double mean = sum / total_collected;
    
    // Apply trigonometric transformations
    double angle = mean / 10.0;
    double sin_val = sin(angle);
    double cos_val = cos(angle);
    
    // Pointer manipulations
    double* ptr1 = &sum;
    double* ptr2 = &mean;
    double diff = *ptr1 - *ptr2;
    
    // Complex calculation chain
    double intermediate = pow(sin_val, 3) + sqrt(fabs(cos_val)) + log10(fabs(diff) + 1);
    
    // Bitwise operations combined with arithmetic
    long long int_part = (long long)intermediate;
    int_part = (int_part & 0xFF) | ((int_part >> 4) & 0xF0);
    
    // Final calculation sequence
    double result = 0.0;
    for (i = 0; i < 5; i++) {
        double term = (i % 2 == 0) ? pow(intermediate, i/2.0) : sqrt(fabs(intermediate)) * i;
        if (i & 1) {
            result += term;
        } else {
            result -= term / 2.0;
        }
    }
    
    // TARGET ASSIGNMENT
    result = result * int_part + xor_result - product / 1000.0;
    
    printf("Result: %.6f\n", result);
    return 0;
}