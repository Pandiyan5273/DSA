class Solution {
    boolean isPalindrome(String s) {
        int l=0;
        int r=s.length()-1;
        while (l<r){
            if(s.charAt(l)==s.charAt(r)){
                l+=1;
                r-=1;
            }
            else{
                return false;
            }
        }
        return true;
        
    }
}