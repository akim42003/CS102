//Strings work like arrays when being passed by reference.

#include <iostream>
#include <string>

using namespace std;


void bar(string data) {
    cout << "Address of data is: " << &data << '\n';
    data = "Here it is!";
}

int main() {
    // int m = 9;
    // cout << "Address of m is: " << &m << '\n';
    // m = foo(m);
    // cout << "m is now: " << m << '\n';
    string data = "Where is this?";
    cout << data;
    cout << "Address of data is: " << &data << '\n';
    bar(data);
    cout << '\n';
}