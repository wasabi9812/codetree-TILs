#include <iostream>
using namespace std;

int main() {
    int a,b;
    cin>>a>>b;
    int num=1;
    int arr[a][b]={};
    for(int i=0; i<a; i++){
        for(int j=0; j<b; j++){
            arr[i][j]=num;
            num+=1;
        }
    }
    for(int i=0; i<a; i++){
        for(int j=0; j<b; j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}