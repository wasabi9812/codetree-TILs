#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int a;
    cin>>a;
    int arr[a];
    for (int i=0; i<a; i++){
        cin>>arr[i];
    }
    for (int i=a-1; i>=0; i--){
        int temp = arr[i];
        if(temp%2!=0){
            continue;
        }
        else{
            cout<<arr[i]<<" ";
        }
    }
    return 0;
}