class Solution {
    int maxSubarraySum(int[] arr) {
        int mini=arr[0];
        int maxi=arr[0];
        
        for(int i=1;i<arr.length;i++){
            mini=Math.max(arr[i],mini+arr[i]);
            maxi=Math.max(maxi,mini);
        }
        return maxi;
    }
}
