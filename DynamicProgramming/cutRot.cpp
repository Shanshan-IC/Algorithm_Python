#include <iostream>

using namespace std;
int a[2000], c[2000], s[2000];
int main() {
    int n, i, j;
    cin >> n;
    for (i=1; i<n; i++)
        cin >> a[i];
    for (i=1; i<n; i++)
        for (j=1; j<=i; j++)
            if (c[i] < a[j] + c[i-j]) {
                c[i] = a[j] + c[i-j];
                s[i] = j; //记录长度为j的第一个切割的长度
            }
    while (n>0) {
        cout << s[n] << endl;
        n = n-s[n];
    }
    return 0;
}
