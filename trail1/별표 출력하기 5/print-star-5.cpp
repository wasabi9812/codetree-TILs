#include <iostream>
using namespace std;

int main() {
    int a;
    cin>>a;

    for (int i=a; i>0; i--){
        for (int j=0; j<i; j++){
            for (int k=0; k<i; k++){
                cout<<"*";
            }
            cout<<" ";
        }
        cout<<endl;
    }



    return 0;
}