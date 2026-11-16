#include <iostream>
#include <vector>
using namespace std;

int n;
int arr[100000];
vector<vector<int>> bucket(10);
int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    int digits = 1;
    for(int i=0; i<6; i++){
        for(int j =0; j<n; j++){
            int digit = (arr[j]/digits)%10;
            bucket[digit].push_back(arr[j]);
        }

        int idx = 0;
        for(int j=0; j<10; j++){
            for(int k=0; k<bucket[j].size(); k++){
                arr[idx++]=bucket[j][k];
            }
        }

        for(int j=0; j<10; j++){
            bucket[j].clear();
        }

        digits *=10;
    }

    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }


    return 0;
}
