class Solution {
    boolean twoSum(int arr[], int target) {
        Map<Integer,Integer> m=new HashMap<>();
		for(int i=0;i<arr.length;i++){
		    int diff=target-arr[i];
		    if(m.containsKey(diff)){
		        return true;
		    }
		    m.put(arr[i],i);
		}
		return false;
    }
}