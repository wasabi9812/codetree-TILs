#include <iostream>
using namespace std;




int main() {
    string arr[3];
    for(int i=0; i<3; i++){
        cin>>arr[i];
    }   
    int maxLen = arr[0].size();

    for (int i = 1; i < 3; i++) {
        if (arr[i].size() > maxLen) {
            maxLen = arr[i].size();
        }
    }
    int minLen = arr[0].size();

    for (int i = 1; i < 3; i++) {
        if (arr[i].size() < minLen) {
            minLen = arr[i].size();
        }
    }

    cout<<maxLen-minLen;

    return 0;
}