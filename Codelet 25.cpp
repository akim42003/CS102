#include <iostream>

using namespace std;

class Node {
private:
    Node() = delete;
public:
    int key;
    Node* left;
    Node* right;
    Node(int new_key);
};

Node::Node(int new_key) {
    key = new_key;
    left = nullptr;
    right = nullptr;
}

class Binary_Search_Tree {
private:
    Node* root;
public:
    Binary_Search_Tree();
    bool empty();
    void insert(int new_key);
    void recursive_insert(Node* current, int new_key);
    void display();
    void recursive_display(Node* current);
    Node* peek(Node* current, int new_key);
};

Binary_Search_Tree::Binary_Search_Tree() {
    root = nullptr;
}

bool Binary_Search_Tree::empty() {
    return root == nullptr;
}

void Binary_Search_Tree::insert(int new_key) {
    if (empty()) {
        root = new Node(new_key);
        display();
        return;
    }
    recursive_insert(root, new_key);
    display();
}

void Binary_Search_Tree::recursive_insert(Node* current, int new_key) {
    if (current->key > new_key) {
        if (peek(current, new_key) == nullptr) {
            current->left = new Node(new_key);
            return;
        }
        recursive_insert(current->left, new_key);
    } else {
        if (peek(current, new_key) == nullptr) {
            current->right = new Node(new_key);
            return;
        }
        recursive_insert(current->right, new_key);
    }
}

void Binary_Search_Tree::display() {
    recursive_display(root);
    cout << endl;
}

void Binary_Search_Tree::recursive_display(Node* current) {
    cout << current->key << ' ';
    if (current->left != nullptr) {
        recursive_display(current->left);
    }  
    if (current->right != nullptr) {
        recursive_display(current->right);
    } 
}

Node* Binary_Search_Tree::peek(Node* current, int new_key) {
    if (current->key > new_key) {
        return current->left;
    } else {
        return current->right;
    }
}

int main() {
    Binary_Search_Tree bst;
    bst.insert(7);
    bst.insert(11);
    bst.insert(3);
    bst.insert(2);
    bst.insert(17);
    bst.insert(5);
}
