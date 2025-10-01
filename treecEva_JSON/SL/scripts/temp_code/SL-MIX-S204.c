#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 10

struct Point {
    int x;
    int y;
};

struct Shape {
    struct Point vertices[MAX_LEN];
    int vertex_count;
    double area;
};

struct Container {
    struct Shape shapes[5];
    int shape_count;
    int indices[3][3];
};

int calculate_sum_of_products(int arr[][3], int rows) {
    int sum = 0;
    for(int i=0; i<rows; i++) {
        sum += arr[i][0] * arr[i][1] * arr[i][2];
    }
    return sum;
}

int main() {
    struct Container container;
    container.shape_count = 3;
    
    // Initialize indices array
    int values[] = {2, 3, 5, 7, 11, 13, 17, 19, 23};
    int k = 0;
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            container.indices[i][j] = values[k++];
        }
    }
    
    // Initialize shapes
    for(int i=0; i<container.shape_count; i++) {
        container.shapes[i].vertex_count = i+3;
        for(int j=0; j<container.shapes[i].vertex_count; j++) {
            container.shapes[i].vertices[j].x = (i+1)*(j+1);
            container.shapes[i].vertices[j].y = (i+1)+(j+1);
        }
    }
    
    // Calculate areas using cross product method for polygons
    for(int i=0; i<container.shape_count; i++) {
        double area = 0.0;
        int n = container.shapes[i].vertex_count;
        for(int j=0; j<n; j++) {
            int j1 = (j+1) % n;
            area += (container.shapes[i].vertices[j].x * container.shapes[i].vertices[j1].y);
            area -= (container.shapes[i].vertices[j1].x * container.shapes[i].vertices[j].y);
        }
        container.shapes[i].area = fabs(area) / 2.0;
    }
    
    // Perform complex calculation
    int product_result = 1;
    for(int i=0; i<container.shape_count; i++) {
        product_result *= (int)container.shapes[i].area;
    }
    
    int sum_indices = calculate_sum_of_products(container.indices, 3);
    
    // Bitwise operations
    int bitwise_result = (product_result & 0xFF) | ((sum_indices >> 2) ^ 0xF0);
    
    // Final calculation
    int target_value = ((bitwise_result * 17) % 1000) + (int)sqrt(sum_indices);
    
    printf("Result: %d\n", target_value);
    return 0;
}