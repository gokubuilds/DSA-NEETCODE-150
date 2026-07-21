class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set <Integer> set=new HashSet<>();
        for (int i:nums){
            if (set.size()!=0 && set.contains(i)){
                return true;
            }set.add(i);
        }
        return false;
        
    }
}