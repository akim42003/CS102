#include <iostream>
const int NUM_CATS = 4;

using namespace std;

int main() {
    int remaining_lives[NUM_CATS] = {6, 3, 2, 5};
    for (int i = 0; i<NUM_CATS; i++){
        cout<<"Cat "<<i<<" has "<<remaining_lives[i]<<" lives remaining"<<"\n";
    }
    return 0;

}