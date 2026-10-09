#include <iostream>
#include <string>
using namespace std;

int main() {
    string A;
    cin >> A;

    string answer = "";
    int cnt = 1;

    for(int i = 0; i < A.size() - 1; i++) {
        if(A[i] == A[i+1]) {
            cnt++;
        }
        else {
            answer += A[i];
            answer += to_string(cnt);
            cnt = 1;
        }
    }

    answer += A[A.size()-1];
    answer += to_string(cnt);
    cout << answer.size()<<endl;
    cout << answer;

    return 0;
}