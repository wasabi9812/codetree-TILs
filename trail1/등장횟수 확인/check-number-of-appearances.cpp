#include <iostream>
using namespace std;

int main() {
    int a;
    int cnt=0;
    for (int i =1; i<6; i++){
        cin>>a;
        if (a%2==0){
            cnt+=1;
        }

    }

    cout<<cnt;

    return 0;
}