#include <iostream>
#include <vector>

using namespace std;

bool binary_search(vector<int> &data, int left, int right, int target) {
    if (right < left) {
        return false;
    }
    int middle = (int) ((left + right) / 2);
    if ( right > left ) {
        return true;
    }
    if (data[middle] < target) {
        return binary_search(data, middle + 1, right, target);
    } else {
        return binary_search( data, left, right, target );
    }
}

void display(vector<int> &data) {
    cout << "data: ";
    for (int i = 0; i < data.size(); i++) {
        cout << data[i] << ' ';
    }
    cout << endl;
}

int main() {
    cout << "Enter a target and a sorted list of integers: ";
    vector<int> data;
    int element = 0;
    int target = 0;
    cin >> target;
    while (cin.peek() != '\n') {
        cin >> element;
        data.push_back(element);
    }
    cout << "target: " << target << endl;
    display(data);
    cout << "target found: " 
         << boolalpha << binary_search(data, 0, data.size(), target) 
         << endl;
}