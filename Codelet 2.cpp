#include <iostream>
#include <string>

using namespace std;

// int get_index_of_space(string s) {  
//     for (int i = 0; i < s.length(); i++) {
//         if (s[i] == ' ') {
//             return i;
//         }
//     }
//     return -1;
// }

int get_index_of_char(string s, char c) {
    int i = 0;
    while (c != s[i] ){
      i ++;
      if (s[i] == ' '){
          return i;
      }
    }
    return -1;
}

int main() {
    string name;
    name = "Celia Munoz";
    cout << name << '\n';
    cout << get_index_of_char(name, ' ') << '\n';
}