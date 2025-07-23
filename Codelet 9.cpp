#include <iostream>

using namespace std;

const int INITIAL_CAPACITY = 20;

class Stack {
private:
    int size;
    int capacity;
    int* data;
    void resize();
    void display();
public:
    Stack();
    Stack(int size, int capacity);
    int top();
    void push(int new_data);
    int pop();
    bool empty();
    int get_size();
};

void Stack::resize() {
    // you do not need to write this
}

void Stack::display() {
    if (empty()) {
        cout << ">>> The stack is empty! \n";
        return; 
    }
    cout << ">>> The stack is: ";
    for (int i = 0; i < size; i++) {
        cout << data[i] << ' ';
    }
    cout << endl;
}

Stack::Stack() {
    size = 0;
    capacity = INITIAL_CAPACITY;
    data = new int[capacity];
}

Stack::Stack(int initial_size, int initial_capacity) {
    size = initial_size;
    capacity = initial_capacity;
    data = new int[capacity];
}

int Stack::top() {
    return data[size-1];
}

void Stack::push(int new_data) {
    if (size == capacity) {
        resize();
    }
    cout << "Pushed: " << new_data << endl;
    data[size] = new_data;
    size++;
    display();
}

int Stack::pop() {
    if (empty()) {
        cout << "Cannot pop: the stack is empty!" << endl;
        return 0;
    }
    int top_data = top();
    size--;
    cout << "Popped: " << top_data << endl;
    display();
    return top_data;
}

bool Stack::empty() {
    return size == 0;
}

int Stack::get_size() {
    return size;
}

int main() {
    Stack s(0, INITIAL_CAPACITY);
    s.push(11);
    s.push(12);
    s.pop();
}
