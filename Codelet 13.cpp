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

class Stack {
private:
    Node* head;
public:
    Stack();
    bool empty();
    void push(int new_key);
    int pop();
    void display();
};

Stack::Stack() {
    head = nullptr;
}

bool Stack::empty() {
    return head == nullptr;
}

void Stack::push(int new_key) {
    Node* new_node = new Node(new_key);
    new_node->next = head;
    head = new_node;
    display();
}

int Stack::pop() {
    if (empty()) {
        cout << "Stack is empty!" << endl;
        return 0; 
    }
    int item = head->key;
    head = head->next;
    return item;
}

void Stack::display() {
    cout << "The stack is: ";
    Node* current = head;
    while (current != nullptr) {
        cout << current->key << ' ';
        current = current->next;
    }
    cout << endl;
}

int main() {
    Stack s;
    s.push(101);
    s.push(102);
    s.push(103);
    s.push(104);
    cout << "popped: " << s.pop() << endl;
    cout << "popped: " << s.pop() << endl;
    s.display();
}