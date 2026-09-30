#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int a;

    cin>>a;

    bool comb = false;
    for (int i=2; i<a; i++){
        int temp = a;
        if (temp%i==0){
            comb = true;
        }
    }

    if (comb){
        cout<<"C";
    }
    else{
        cout<<"N";
    }

    return 0;
}