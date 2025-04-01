//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int findElement(vector<int> &arr) {
        int n = arr.size();
        if (n < 3) return -1;

        vector<int> l(n), r(n);

        // Fill left max array
        l[0] = INT_MIN;
        for (int i = 1; i < n; i++) {
            l[i] = max(l[i - 1], arr[i - 1]);
        }

        // Fill right min array
        r[n - 1] = INT_MAX;
        for (int i = n - 2; i >= 0; i--) {
            r[i] = min(r[i + 1], arr[i + 1]);
        }

        // Find the valid element
        for (int i = 1; i < n - 1; i++) {
            if (l[i] < arr[i] && arr[i] < r[i]) {
                return arr[i];
            }
        }
        return -1;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        int ans = ob.findElement(arr);
        cout << ans << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends