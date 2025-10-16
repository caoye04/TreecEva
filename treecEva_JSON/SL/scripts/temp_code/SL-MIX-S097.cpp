#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <cmath>

struct TriangleNode {
    int id;
    double area;
    std::shared_ptr<TriangleNode> left;
    std::shared_ptr<TriangleNode> right;
    int height;
    
    TriangleNode(int triangle_id, double triangle_area) : id(triangle_id), area(triangle_area), left(nullptr), right(nullptr), height(1) {}
};

class TriangleTree {
private:
    std::shared_ptr<TriangleNode> root;
    
    int getHeight(std::shared_ptr<TriangleNode> node) {
        if (!node) return 0;
        return node->height;
    }
    
    double getArea(std::shared_ptr<TriangleNode> node) {
        if (!node) return 0.0;
        return node->area;
    }
    
    std::shared_ptr<TriangleNode> rotateRight(std::shared_ptr<TriangleNode> y) {
        std::shared_ptr<TriangleNode> x = y->left;
        std::shared_ptr<TriangleNode> T2 = x->right;
        
        x->right = y;
        y->left = T2;
        
        y->height = std::max(getHeight(y->left), getHeight(y->right)) + 1;
        x->height = std::max(getHeight(x->left), getHeight(x->right)) + 1;
        
        return x;
    }
    
    std::shared_ptr<TriangleNode> rotateLeft(std::shared_ptr<TriangleNode> x) {
        std::shared_ptr<TriangleNode> y = x->right;
        std::shared_ptr<TriangleNode> T2 = y->left;
        
        y->left = x;
        x->right = T2;
        
        x->height = std::max(getHeight(x->left), getHeight(x->right)) + 1;
        y->height = std::max(getHeight(y->left), getHeight(y->right)) + 1;
        
        return y;
    }
    
    int getBalance(std::shared_ptr<TriangleNode> node) {
        if (!node) return 0;
        return getHeight(node->left) - getHeight(node->right);
    }
    
    std::shared_ptr<TriangleNode> insert(std::shared_ptr<TriangleNode> node, int id, double area) {
        if (!node) {
            return std::make_shared<TriangleNode>(id, area);
        }
        
        if (area < node->area) {
            node->left = insert(node->left, id, area);
        } else if (area > node->area) {
            node->right = insert(node->right, id, area);
        } else {
            node->id = id; // Update id if area already exists
            return node;
        }
        
        node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));
        
        int balance = getBalance(node);
        
        // Left Left Case
        if (balance > 1 && area < getArea(node->left)) {
            return rotateRight(node);
        }
        
        // Right Right Case
        if (balance < -1 && area > getArea(node->right)) {
            return rotateLeft(node);
        }
        
        // Left Right Case
        if (balance > 1 && area > getArea(node->left)) {
            node->left = rotateLeft(node->left);
            return rotateRight(node);
        }
        
        // Right Left Case
        if (balance < -1 && area < getArea(node->right)) {
            node->right = rotateRight(node->right);
            return rotateLeft(node);
        }
        
        return node;
    }
    
public:
    void addTriangle(int id, double area) {
        root = insert(root, id, area);
    }
    
    int getRootId() {
        return root ? root->id : -1;
    }
};

double calculateTriangleArea(const std::vector<std::pair<double, double>>& vertices) {
    if (vertices.size() != 3) return 0.0;
    
    // Using the cross-product formula: Area = 0.5 * |det([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])|
    // Which simplifies to: Area = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
    double x1 = vertices[0].first, y1 = vertices[0].second;
    double x2 = vertices[1].first, y2 = vertices[1].second;
    double x3 = vertices[2].first, y3 = vertices[2].second;
    
    return 0.5 * std::abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2));
}

int main() {
    TriangleTree tree;
    
    // Define triangle vertices for our mesh
    std::vector<std::vector<std::pair<double, double>>> mesh_triangles = {
        {{0, 0}, {4, 0}, {0, 3}},  // Triangle 100
        {{1, 1}, {5, 1}, {1, 4}},  // Triangle 200
        {{2, 2}, {6, 2}, {2, 5}},  // Triangle 300
        {{3, 3}, {7, 3}, {3, 6}},  // Triangle 400
        {{0, 0}, {2, 0}, {0, 2}}   // Triangle 500
    };
    
    std::vector<int> triangle_ids = {100, 200, 300, 400, 500};
    
    // Insert triangles into the tree based on their calculated areas
    for (size_t i = 0; i < mesh_triangles.size(); ++i) {
        double area = calculateTriangleArea(mesh_triangles[i]);
        tree.addTriangle(triangle_ids[i], area);
    }
    
    // After all insertions and automatic rebalancing
    int final_root_id = tree.getRootId();
    
    std::cout << "Result: " << final_root_id << std::endl;
    
    return 0;
}