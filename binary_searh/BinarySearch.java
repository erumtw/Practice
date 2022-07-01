package binary_searh;

// { Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

  public class BinarySearch {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        // int T = sc.nextInt();
        // while (T > 0) {
            int n = sc.nextInt();
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            int key = sc.nextInt();
            Solution g = new Solution();
            System.out.println(g.binarysearch(arr, n, key));
            // T--;
        // }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    int binSearch(int arr[], int low, int high, int k){
        int mid = (int)Math.ceil((low + high)/2);
        if(low > high)
            return -1;
        else {
            if (arr[mid] == k) {
                return mid;
            } 
            else if(k > arr[mid]) {
                return this.binSearch(arr, mid+1, high, k);
            } 
            else {
                return this.binSearch(arr, low, mid-1, k);
            }
        }
        
    }
    
    int binarysearch(int arr[], int n, int k) {
        // code here
        return binSearch(arr, 0, n-1, k);
    }
}

