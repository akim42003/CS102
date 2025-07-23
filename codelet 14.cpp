#include <iostream>
#include <string>

using namespace std;

string reverse(string word) {
    if (word.length() == 1) {
        return word;
    }
    char x = word[0];
    word = word.substr(1, word.length());
    return reverse(word) + x;
}

int main() {
    string word;
    cout << "Enter a word: ";
    cin >> word;
    cout << "Reversed: " << reverse(word) << endl;
    return 0;
}
