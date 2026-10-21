#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin>>n;
    int sum =0;
    for(int i=0; i<n; i++){
        int temp=0;
        cin>>temp;
        sum+=temp;
    }

    string answer = to_string(sum);
    answer = answer.substr(1) + answer[0];
    cout<<answer;
    return 0;
}