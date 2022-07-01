package find_min_max;

// { Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class pair  
{  
    private long first, second;  

    public pair(long first, long second)  
    {  
        this.first = first;  
        this.second = second;  
    }  

    public long getFirst(){
        return this.first;
    }

    public long getSecond(){
        return this.second;
    }
}

class Min_max {
	public static void main(String[] args) throws IOException
	{
        
	        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        // int t =
        //     Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        // while(t-->0)
        // {
            long n = Long.parseLong(br.readLine().trim());
            long a[] = new long[(int)(n)];
            // long getAnswer[] = new long[(int)(n)];
            String inputLine[] = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(inputLine[i]);
            }
            
            Compute obj = new Compute();
            pair product = obj.getMinMax(a, n); 
            System.out.println("min = "+ product.getFirst() +" :: "+ "max = " + product.getSecond());
            
        // }
	}
}

// } Driver Code Ends

//User function Template for Java

/*
 class pair  
{  
    long first, second;  
    public pair(long first, long second)  
    {  
        this.first = first; min  
        this.second = second;  max
    }  
} */

class Compute 
{
    static pair getMinMax(long a[], long n)  
    {
        //Write your code here
        // long min = a[0];
        // long max = a[0];

        // for (int i = 0; i < n; i++) {
        //     if(a[i] < min)
        //         min = a[i];
        //     if(a[i] > max)
        //         max = a[i];
        // }
        // return new pair(min, max);

        // slower than above method but short
        TreeSet<Long> ts = new TreeSet<>();
        for (Long temp : a) {
            ts.add(temp);
        }
        return new pair(ts.first(), ts.last());
    }
}
