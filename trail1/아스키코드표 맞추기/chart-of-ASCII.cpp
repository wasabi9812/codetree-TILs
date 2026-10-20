#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int temp[5]={};
    
    for(int i=0; i<5; i++){

        cin>>temp[i];

    }

    for(int i=0; i<5; i++){

        char C = (char)temp[i];
        cout<<C<<" ";
    }

    return 0;
}