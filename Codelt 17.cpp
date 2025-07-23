#include <iostream>
using namespace std;

class Node {
private:
    Node() = delete;  // the default constructor may never be used
public:
    int key;
    Node* next;
    Node* prev;
    Node(int new_key);
};

Node::Node(int new_key) {
    key = new_key;
}

class DoublyLinkedList {
private:
    Node* head;
    Node* tail;
public:
    DoublyLinkedList();
    bool empty();
    void append(int new_key);
    void display();
    void delete_key(int key_to_delete);
};

DoublyLinkedList::DoublyLinkedList() {
    head = nullptr;
    tail = nullptr;
}

bool DoublyLinkedList::empty() {
    return tail == nullptr;
}

void DoublyLinkedList::append(int new_key) {
    Node* address_of_new_node = new Node(new_key);
    if (empty()) {
        head = address_of_new_node;
        tail = address_of_new_node;
        display();
        return;
    }
    tail->next = address_of_new_node;
    address_of_new_node->prev = tail;
    tail = address_of_new_node;
    display();
}

void DoublyLinkedList::display() {
    cout << "The SLL is: ";
    Node* current = head;
    while (current != nullptr) {
        cout << current->key << ' ';
        current = current->next;
    }
    cout << endl;
}

void DoublyLinkedList::delete_key(int key_to_delete) {
    Node* current = head;
    while (current != nullptr) {
        if (current->key == key_to_delete) {
            // found the node to delete
            if (current == head) {
                // node to delete is the head
                head = current->next;
                if (head != nullptr) {
                    head->prev = nullptr;
                } else {
                    tail = nullptr;
                }
            } else if (current == tail) {
                // node to delete is the tail
                tail = current->prev;
                if (tail != nullptr) {
                    tail->next = nullptr;
                } else {
                    head = nullptr;
                }
            } else {
                // node to delete is in the middle
                current->prev->next = current->next;
                current->next->prev = current->prev;
            }
            delete current;
            return;
        }
        current = current->next;
    }
    // key not found in list
    cout << "Key not found in list" << endl;
}

int main() {
    DoublyLinkedList sll;
    sll.append(12);
    sll.append(13);
    sll.append(14);
    sll.delete_key(14);
    sll.display();
}