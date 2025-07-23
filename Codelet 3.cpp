#include <iostream>
#include <string>
using namespace std;

const int NUM_NAMES = 3;

// Returns the index of the first space that appears in the given string,
// and returns -1 is no space is found (we wrote this last time):
int get_index_of_space(string s) {  
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            return i;
        }
    }
    return -1;
}

string get_surname(string name) {
    int index_of_space = get_index_of_space(name);
    string surname;
    for(int i=0; i<name.length(); i++){
      if(i<index_of_space){
        surname = surname;
      }
      else{
        surname += name[i];
      }
      
    }  
    return surname;
}

void grab_surnames(string names[], string surnames[]) {
    // you write the missing loop here
    for (int i=0; i < NUM_NAMES; i++){
        string surname = get_surname(names[i]);;
        surnames[i] = surname;
    }
    // and call get_surname() from within the loop
}

int main() {
    string names[NUM_NAMES] = {"Giles Snyder", "Korva Coleman", "Lakshmi Singh"};
    string surnames[NUM_NAMES];
    grab_surnames(names, surnames);
    for (int i = 0; i < NUM_NAMES; i++) {
        cout << surnames[i] << '\n';
    }
}