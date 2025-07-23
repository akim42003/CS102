#include <iostream>
using namespace std;

class Node {
private:
    Node() = delete;  // the default constructor may never be used
public:
    int key;
    Node* next;
    Node(int new_key);
};

Node::Node(int new_key) {
    key = new_key;
}

class SinglyLinkedList {
private:
    Node* head;
    Node* tail;
public:
    SinglyLinkedList();
    bool empty();
    void append(int new_key);
    void display();
    void delete_last();
};

SinglyLinkedList::SinglyLinkedList() {
    head = nullptr;
    tail = nullptr;
}

bool SinglyLinkedList::empty() {
    return tail == nullptr;
}

void SinglyLinkedList::append(int new_key) {
    Node* address_of_new_node = new Node(new_key);
    if (empty()) {
        head = address_of_new_node;
        tail = address_of_new_node;
        display();
        return;
    }
    tail->next = address_of_new_node;
    tail = address_of_new_node;
    display();
}

void SinglyLinkedList::display() {
    cout << "The SLL is: ";
    Node* current = head;
    while (current != nullptr) {
        cout << current->key << ' ';
        current = current->next;
    }
    cout << endl;
}

void SinglyLinkedList::delete_last() {
    if (empty()){
      return;
    }
    if (head == tail) {
        delete tail;
        head = nullptr;
        tail = nullptr;
        return;
    }
    Node* current = head;
    while (current->next != tail) {
        current = current->next;
    }
    delete tail;
    tail = current;
    tail->next = nullptr;
}

int main() {
    SinglyLinkedList sll;
    sll.append(12);
    sll.append(13);
    sll.append(14);
    sll.delete_last();
    sll.display();
  
    return 0;
}