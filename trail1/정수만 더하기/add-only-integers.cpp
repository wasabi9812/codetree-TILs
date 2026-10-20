#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    string a;
    cin>>a;
    int sum=0;
    for(int i=0; i<a.size(); i++){
        if(a[i]>='0'&&a[i]<='9'){
            int t = a[i]-'0';
            sum+=t;
        }
    }
    cout<<sum;
    return 0;
}