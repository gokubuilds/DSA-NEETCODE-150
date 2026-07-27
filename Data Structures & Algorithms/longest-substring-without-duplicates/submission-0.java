class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()==0 ||s.length()==1){
            return s.length();
        }
        Set <Character> set=new HashSet<>();
        int left=0;
        int right=0;
        int res=0;
        while(right<s.length()){
            while(set.contains(s.charAt(right))){
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            res=Math.max(res,(right-left)+1);
            right++;
            
        }
        return res;
        
    }
}
