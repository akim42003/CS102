#include <iostream>
#include <vector>

using namespace std;

class Node {
private:
    Node() = delete;
public:
    int key;
    Node* left;
    Node* right;
    Node* parent;
    Node(int new_key, Node* new_parent);
};

Node::Node(int new_key, Node* new_parent) {
    key = new_key;
    left = nullptr;
    right = nullptr;
    parent = new_parent;
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
    Node* locate(int key);
    Node* recursive_locate(int key, Node* current);
    Node* largest_to_left(Node* n);
    void JR_remove(Node* n);
    void remove(int key);
    Node* minValueNode(Node* node);
    int height();
    int recursive_height(Node* node);

};

Binary_Search_Tree::Binary_Search_Tree() {
    root = nullptr;
}

bool Binary_Search_Tree::empty() {
    return root == nullptr;
}

void Binary_Search_Tree::insert(int new_key) {
    if (empty()) {
        root = new Node(new_key, nullptr);
        display();
        return;
    }
    recursive_insert(root, new_key);
    display();
}

void Binary_Search_Tree::recursive_insert(Node* current, int new_key) {
    if (current->key > new_key) {
        if (current->left == nullptr) {
            current->left = new Node(new_key, current);
            return;
        }
        recursive_insert(current->left, new_key);
    } else {
        if (current->right == nullptr) {
            current->right = new Node(new_key, current);
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
    cout << "key: " << current->key << " parent: ";
    if (current->parent != nullptr) {
        cout << current->parent->key << endl;
    } else {
        cout << "none" << endl;
    }
    if (current->left != nullptr) {
        recursive_display(current->left);
    }  
    if (current->right != nullptr) {
        recursive_display(current->right);
    } 
}

// Thanks to Joe S and Rance X for these next three methods:

Node* Binary_Search_Tree::locate(int key) {
    return recursive_locate(key, root);
}

Node* Binary_Search_Tree::recursive_locate(int key, Node* current) {
    if (current == nullptr) {
        return nullptr;
    }
    if (current->key == key) {
        return current;
    } else if (current->key > key) {
        Node* value = recursive_locate(key, current->left);
        return value;
    } else {
        Node* value = recursive_locate(key, current->right);
        return value;
    }
}

Node* Binary_Search_Tree::largest_to_left(Node* n) {
    if (n->left == nullptr) {
        return nullptr;
    }
    Node* current = n->left;
    while (current->right != nullptr) {
        current = current->right;
    }
    return current;
}
void Binary_Search_Tree::JR_remove(Node* n){
    Node* left_biggest = largest_to_left(n);
    left_biggest->right = n->right;
    n->right->parent = left_biggest;
    if (n->parent == nullptr){
    n->left->parent = nullptr;
    root = n->left;
    return;
    }
    if (n->key > n->parent->key){
        n->parent->right = n->right;
        n->right->parent = n->parent;
    }
    else{
        n->parent->left = n->left;
        n->left->parent = n->parent;
    }
    return;

}

void Binary_Search_Tree::remove(int key) {
    Node* node_to_remove = locate(key);
    if (node_to_remove == nullptr) {
        return; // Node not found, do nothing
    }

    if (node_to_remove->left == nullptr && node_to_remove->right == nullptr) {
        // Case 1: Node with no children
        if (node_to_remove->parent == nullptr) {
            root = nullptr;
        } else if (node_to_remove == node_to_remove->parent->left) {
            node_to_remove->parent->left = nullptr;
        } else {
            node_to_remove->parent->right = nullptr;
        }
    } else if (node_to_remove->left == nullptr || node_to_remove->right == nullptr) {
        // Case 2: Node with one child
        Node* child = (node_to_remove->left != nullptr) ? node_to_remove->left : node_to_remove->right;
        if (node_to_remove->parent == nullptr) {
            root = child;
            child->parent = nullptr;
        } else if (node_to_remove == node_to_remove->parent->left) {
            node_to_remove->parent->left = child;
            child->parent = node_to_remove->parent;
        } else {
            node_to_remove->parent->right = child;
            child->parent = node_to_remove->parent;
        }
    } else {
        // Case 3: Node with two children
        Node* successor = minValueNode(node_to_remove->right);
        node_to_remove->key = successor->key;
        remove(successor->key);
    }
}

Node* Binary_Search_Tree::minValueNode(Node* node) {
    Node* current = node;
    while (current->left != nullptr) {
        current = current->left;
    }
    return current;
}

int Binary_Search_Tree::height() {
    return recursive_height(root);
}

int Binary_Search_Tree::recursive_height(Node* node) {
    if (node == nullptr) {
        return 0;
    }
    int left_height = recursive_height(node->left);
    int right_height = recursive_height(node->right);
    return max(left_height, right_height) + 1;
}


int main() {
    Binary_Search_Tree bst;
    vector<int> keys = {400, 300, 600, 500, 550, 350, 450, 625, 650, 325};

    for (int key : keys) {
        bst.insert(key);
    }

    cout << "Original tree:" << endl;
    bst.display();
    cout << "Tree height: " << bst.height() << endl;

    int node_to_remove = 500;
    cout << "Removing node with key " << node_to_remove << " using JR_remove():" << endl;
    Node* jr_node_to_remove = bst.locate(node_to_remove);
    bst.JR_remove(jr_node_to_remove);
    bst.display();
    cout << "Tree height: " << bst.height() << endl;

    // Re-insert the removed node to test the other remove() method
    bst.insert(node_to_remove);
    cout << "Re-inserting node with key " << node_to_remove << ":" << endl;
    bst.display();
    cout << "Tree height: " << bst.height() << endl;

    cout << "Removing node with key " << node_to_remove << " using remove():" << endl;
    bst.remove(node_to_remove);
    bst.display();
    cout << "Tree height: " << bst.height() << endl;

    return 0;
}
