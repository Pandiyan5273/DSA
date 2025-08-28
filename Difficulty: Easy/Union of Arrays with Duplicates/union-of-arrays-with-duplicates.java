class Solution {
    public static ArrayList<Integer> findUnion(int[] a, int[] b) {
        // code here
        Set<Integer> s= new HashSet<>();
        for(int i:a){
            s.add(i);
        }
        for(int i:b){
            s.add(i);
        }
        return new ArrayList<>(s);
    }
}