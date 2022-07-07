// { Driver Code Starts
// Initial template for C++

#include <iostream> // <bits/stdc++.h>
#include <vector>

using namespace std;

 // } Driver Code Ends
// User function template for C++

class Solution{
    
 public:
    int search(vector<int>& arr, int N, int X) // find element if found return index else -1
    {
        // Your code here
        int i;
        for (i = 0; i < N; i++) {
            // if founded return i
            if(arr[i] == X) {
                return i;
            }
        }
        // if not return -1 
        return -1;
    }
    
    int MissingNumber(vector<int>& array, int n) {
        // Your code goes here
        for(int i = 1; i <= n; i++){
            // if i between 1 - (n-1) not in array return i
            if (search(array, n-1, i) == -1) { 
                return i;
            }
        }
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> array(n - 1);
        for (int i = 0; i < n - 1; ++i) cin >> array[i];
        Solution obj;
        cout << obj.MissingNumber(array, n) << "\n";
    }
    return 0;
}  // } Driver Code Ends