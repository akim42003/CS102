#include <iostream>
using namespace std;

class Node {
private:
public:
    int key;
    Node* next;
    Node();
    Node(int new_key);
    void display();
};

Node::Node() {
    key = 0;
    next = nullptr;
}

Node::Node(int new_key) {
    key = new_key;
    next = nullptr;
}

void Node::display() {
    cout << "\nI am a Node!" << endl
         << "My key is " << key << " and my key lives at " << &key
         << endl
         << "and my next points at " << next << " and lives at " << &next
         << endl << endl;
}

int main() {
    Node n(99);
    n.display();
}