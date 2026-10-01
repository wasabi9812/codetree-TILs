#include <iostream>
using namespace std;

int main() {
    int a;
    cin>>a;
    int arr[a][a];
    int num=1;
    for(int i = 0; i < a; i++)
        for(int j = 0; j < a; j++)
            arr[j][i] = num++;

    for(int i = 0; i < a; i++) {
        for(int j = 0; j < a; j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }

    return 0;
}