#include <iostream>
using namespace std;

class Node {
private:
    Node() = delete; // this means we cannot use a default constructor
public:
    int key;
    Node* prev;
    Node* next;
    Node(int new_key);
};

Node::Node(int new_key) {
    key = new_key;
    prev = nullptr;
    next = nullptr;
}

int main() {
    Node n(99);
    Node p(100);
    Node q(101);
    n.next = &p;
    p.prev = &n; 
    p.next = &q;
    q.prev = &p;
    cout << q.prev->prev->key << endl;
}