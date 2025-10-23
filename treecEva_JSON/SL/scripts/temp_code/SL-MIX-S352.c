#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define MOD_VALUE 1000007

typedef struct Point {
    int x;
    int y;
} Point;

typedef struct QuadTreeNode {
    Point sw_corner; // Southwest corner
    Point ne_corner; // Northeast corner
    Point* point_data;
    struct QuadTreeNode *nw, *ne, *sw, *se;
} QuadTreeNode;

QuadTreeNode* create_node(Point sw, Point ne) {
    QuadTreeNode* node = (QuadTreeNode*)malloc(sizeof(QuadTreeNode));
    node->sw_corner = sw;
    node->ne_corner = ne;
    node->point_data = NULL;
    node->nw = node->ne = node->sw = node->se = NULL;
    return node;
}

void insert_point(QuadTreeNode* node, Point p) {
    if (p.x < node->sw_corner.x || p.x > node->ne_corner.x ||
        p.y < node->sw_corner.y || p.y > node->ne_corner.y) {
        return; // Point out of bounds
    }
    
    if (node->point_data == NULL && node->nw == NULL) {
        node->point_data = (Point*)malloc(sizeof(Point));
        *(node->point_data) = p;
        return;
    }
    
    if (node->nw == NULL) {
        // Subdivide the node
        int mid_x = (node->sw_corner.x + node->ne_corner.x) / 2;
        int mid_y = (node->sw_corner.y + node->ne_corner.y) / 2;
        
        node->nw = create_node((Point){node->sw_corner.x, mid_y+1}, (Point){mid_x, node->ne_corner.y});
        node->ne = create_node((Point){mid_x+1, mid_y+1}, node->ne_corner);
        node->sw = create_node(node->sw_corner, (Point){mid_x, mid_y});
        node->se = create_node((Point){mid_x+1, node->sw_corner.y}, (Point){node->ne_corner.x, mid_y});
        
        // Re-insert existing point
        Point old_point = *(node->point_data);
        free(node->point_data);
        node->point_data = NULL;
        insert_point(node, old_point);
    }
    
    // Insert the new point into a child
    int mid_x = (node->sw_corner.x + node->ne_corner.x) / 2;
    int mid_y = (node->sw_corner.y + node->ne_corner.y) / 2;
    
    if (p.x <= mid_x) {
        if (p.y <= mid_y) {
            insert_point(node->sw, p);
        } else {
            insert_point(node->nw, p);
        }
    } else {
        if (p.y <= mid_y) {
            insert_point(node->se, p);
        } else {
            insert_point(node->ne, p);
        }
    }
}

// Global accumulator for energy
long long accumulator_energy = 0;

// Recursive traversal: SE -> SW -> NE -> NW (a specific order)
void traverse_and_calculate(QuadTreeNode* node) {
    if (!node) return;
    
    // Visit SE child first
    traverse_and_calculate(node->se);
    
    // Then SW
    traverse_and_calculate(node->sw);
    
    // Process current node
    if (node->point_data) {
        int px = node->point_data->x;
        int py = node->point_data->y;
        // Energy calculation: (x^2 + y^2) mod MOD_VALUE
        long long energy_contribution = ((long long)(px * px) % MOD_VALUE + (long long)(py * py) % MOD_VALUE) % MOD_VALUE;
        accumulator_energy = (accumulator_energy + energy_contribution) % MOD_VALUE;
        // Geometric calculation: area of bounding box
        long long width = (long long)(node->ne_corner.x - node->sw_corner.x);
        long long height = (long long)(node->ne_corner.y - node->sw_corner.y);
        long long area = (width * height) % MOD_VALUE;
        accumulator_energy = (accumulator_energy * (area + 1)) % MOD_VALUE; // Multiply by (area+1)
    }
    
    // Then NE
    traverse_and_calculate(node->ne);
    
    // Finally NW
    traverse_and_calculate(node->nw);
}

int main() {
    QuadTreeNode* root = create_node((Point){0, 0}, (Point){100, 100});
    
    Point points[] = {{10, 90}, {50, 50}, {90, 10}, {30, 70}, {70, 30}};
    int num_points = sizeof(points)/sizeof(points[0]);
    
    for (int i = 0; i < num_points; i++) {
        insert_point(root, points[i]);
    }
    
    traverse_and_calculate(root);
    
    printf("Result: %lld\n", accumulator_energy);
    return 0;
}