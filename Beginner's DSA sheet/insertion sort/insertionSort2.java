import java.util.Scanner;

public class insertionSort2 {

    static void printArray(int arr[],int size)
	{
		int i;
		for(i=0;i<size;i++)
		System.out.print(arr[i]+" ");
	    System.out.println();
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t= sc.nextInt();
		while(t>0)
		{
			int n = sc.nextInt();
			int a[] = new int[n];
		
			for(int i=0;i<n;i++)
			a[i]= sc.nextInt();
			
			 new Solution().insertionSort(a,n);
			 printArray(a,n);
			
		t--;
		}
		
	}
}

class Solution
{
    static void insert(int arr[],int i)
    {
        // Your code here
        int currentValue = arr[i];
        int pos = i;

        while(pos > 0 && arr[pos-1] > currentValue) {
            arr[pos] = arr[pos-1];
            pos--;
        }

        arr[pos] = currentValue;
    }
  //Function to sort the array using insertion sort algorithm.
    public void insertionSort(int arr[], int n)
    {
        //code here
        for (int i = 1; i < arr.length; i++) {
            insert(arr, i);
        }
    }
}

