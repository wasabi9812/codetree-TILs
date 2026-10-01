#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[11]={};
    int max =0;
    for (int i=1; i<=10; i++){
        cin>>arr[i];
    }
    for (int i=1; i<=10; i++){
        if(arr[i]>=max){
            max=arr[i];
        }
    }
    cout<<max;
    return 0;
}