public class Solution
{

    public int maxnum(int [] arr){
        int low=0;
        int high=arr.length-1;
        int mid=0;
        while(low<=high){
            mid=(low+high)/2;
            if(arr[low]>arr[mid]){
                high=mid-1;
            }else{
                low=mid+1;
            }
        }return arr[high];}

   public static void main(String[]args){
        int nums[]={6,7,8,1,2,3,4,5};
       Solution obj = new Solution();
        System.out.println(obj.maxnum(nums));
        
    }

}
