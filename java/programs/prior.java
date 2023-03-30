import java.util.*;

class Solution{
    public void  sorter(int[] arr){
        PriorityQueue<Integer> pq=new PriorityQueue<Integer>();
        for(int i=0;i<arr.length;i++){
            pq.add(arr[i]);
        }
        System.out.println(pq);
    }
    public static void main(String[]args){
        Solution s=new Solution();
        int [] a={2,5,6,8,3,1,9,-2,0};
        s.sorter(a);
    }
}