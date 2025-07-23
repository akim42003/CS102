#include <iostream>
#include <string>

using namespace std;

void getNames(string *names, int n) {
    cout << "The names are: " << endl;
    for (int i = 0; i < n; i++) {
        cout << names[i] << endl;
    }
}

int main() {
    int num;
    cout << "Enter the number of names: ";
    cin >> num;

    string *names = new string[num];

    cin.ignore();
    for (int i = 0; i < num; i++) {
        cout << "Enter name " << i + 1 << ": ";
        getline(cin, names[i]);
    }

    getNames(names, num);

    return 0;
}
