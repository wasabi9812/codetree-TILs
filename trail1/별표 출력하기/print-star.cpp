#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int N;
    cin>>N;
    for (int i=0; i<N; i++){
        for(int j=0; j<=i; j++){
            cout<<"* ";
        }
        cout<<endl;

    }
    for(int i=N-2; i>=0; i--){
        for(int j =0; j<=i; j++){
            cout<<"* ";
        }
        cout<<endl;
    }

    return 0;
}